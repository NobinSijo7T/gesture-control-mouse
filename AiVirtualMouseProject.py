import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

##########################
wCam, hCam = 640, 480
frameR = 100 # Frame Reduction
smoothening = 7
#########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

# Try different camera indices with better error handling
def initialize_camera():
    for camera_index in [0, 1, 2]:
        print(f"Trying camera index {camera_index}...")
        cap = cv2.VideoCapture(camera_index)
        if cap.isOpened():
            # Test if we can actually read a frame
            ret, test_frame = cap.read()
            if ret and test_frame is not None:
                print(f"Successfully opened camera {camera_index}")
                return cap
            else:
                cap.release()
                print(f"Camera {camera_index} opened but cannot read frames")
        else:
            print(f"Cannot open camera {camera_index}")
    
    print("Error: Could not open any camera. Please check your camera connection.")
    return None

cap = initialize_camera()
if cap is None:
    exit()

cap.set(3, wCam)
cap.set(4, hCam)

# Add a small delay to let camera stabilize
time.sleep(1)

detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
print(f"Screen resolution: {wScr} x {hScr}")

frame_count = 0

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    frame_count += 1
    
    # Check if frame is captured successfully
    if not success or img is None:
        print(f"Error: Failed to capture frame {frame_count} from camera")
        break
    
    # Add frame size validation
    if img.shape[0] == 0 or img.shape[1] == 0:
        print("Error: Empty frame received")
        continue
    
    try:
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        
        # 2. Get the tip of the index and middle fingers
        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
        
            # 3. Check which fingers are up
            fingers = detector.fingersUp()
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
            (255, 0, 255), 2)
            
            # 4. Only Index Finger : Moving Mode
            if fingers[1] == 1 and fingers[2] == 0:
                # 5. Convert Coordinates
                x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                # 6. Smoothen Values
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
            
                # 7. Move Mouse
                autopy.mouse.move(wScr - clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY
                
            # 8. Both Index and middle fingers are up : Clicking Mode
            if fingers[1] == 1 and fingers[2] == 1:
                # 9. Find distance between fingers
                length, img, lineInfo = detector.findDistance(8, 12, img)
                # 10. Click mouse if distance short
                if length < 40:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]),
                    15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click()
        
        # 11. Frame Rate
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
        (255, 0, 0), 3)
        
        # 12. Display
        cv2.imshow("Image", img)
        
    except Exception as e:
        print(f"Error processing frame {frame_count}: {e}")
        continue
    
    # Add exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

# Clean up
print("Cleaning up...")
cap.release()
cv2.destroyAllWindows()
print("Program ended.")
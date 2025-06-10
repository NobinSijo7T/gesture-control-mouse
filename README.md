# Gesture Control Mouse

A Python application that allows you to control your mouse cursor using hand gestures through your webcam. This project uses computer vision and machine learning to track hand movements and translate them into mouse actions.

## Features

- **Mouse Movement**: Control cursor movement with your index finger
- **Mouse Clicking**: Click by bringing index and middle fingers together
- **Real-time Hand Tracking**: Uses MediaPipe for accurate hand landmark detection
- **Smooth Movement**: Implements smoothening algorithm for fluid cursor control
- **Visual Feedback**: Real-time camera feed with hand tracking visualization

## Demo

The application creates a virtual boundary on your screen where hand movements are mapped to cursor movements. Simply raise your index finger to move the cursor, and bring your index and middle fingers together to click.

## Requirements

- Python 3.8 or higher
- Webcam/Camera
- Windows, macOS, or Linux

## Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/NobinSijo7T/gesture-control-mouse.git
cd gesture-control-mouse
```

### Step 2: Create a Python Virtual Environment

#### On Windows:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 3: Upgrade pip (Optional but Recommended)
```bash
python -m pip install --upgrade pip
```

### Step 4: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Verify Installation
```bash
# Check if all packages are installed correctly
pip list
```

## Usage

### Step 1: Ensure Your Virtual Environment is Active
Make sure you see `(venv)` at the beginning of your command prompt.

### Step 2: Run the Application
```bash
python AiVirtualMouseProject.py
```

### Step 3: Using the Application

1. **Position yourself**: Sit comfortably in front of your webcam
2. **Camera window**: A window will open showing your camera feed
3. **Hand detection**: Place your hand in front of the camera
4. **Mouse control**:
   - **Move cursor**: Raise only your index finger and move your hand
   - **Click**: Raise both index and middle fingers, then bring them close together

### Step 4: Exit the Application
- Press `q` in the camera window to quit
- Or press `Ctrl+C` in the terminal

## Troubleshooting

### Camera Issues
If you encounter camera-related errors:
```bash
# The application will automatically try different camera indices (0, 1, 2)
# If no camera is detected, check:
# 1. Camera permissions
# 2. Camera is not being used by another application
# 3. Camera drivers are properly installed
```

### Import Errors
If you get import errors:
```bash
# Make sure virtual environment is activated
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Reinstall requirements
pip install -r requirements.txt
```

### Performance Issues
If the application runs slowly:
- Ensure good lighting conditions
- Close other applications using the camera
- Try reducing the camera resolution in the code

## Configuration

You can modify these parameters in `AiVirtualMouseProject.py`:

```python
wCam, hCam = 640, 480    # Camera resolution
frameR = 100             # Frame reduction (boundary margin)
smoothening = 7          # Mouse movement smoothening factor
```

## Project Structure

```
gesture-control-mouse/
│
├── AiVirtualMouseProject.py    # Main application file
├── HandTrackingModule.py       # Hand tracking module
├── requirements.txt            # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                # Git ignore file
```

## Dependencies

- **opencv-python**: Computer vision library for camera handling
- **mediapipe**: Google's ML framework for hand tracking
- **numpy**: Numerical computing library
- **autopy**: Cross-platform GUI automation library

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand tracking technology
- [OpenCV](https://opencv.org/) for computer vision capabilities
- [AutoPy](https://github.com/msanders/autopy) for cross-platform mouse control

## Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Make sure your environment meets all requirements

---

**Note**: This application requires camera permissions and may trigger security software warnings due to mouse control functionality.

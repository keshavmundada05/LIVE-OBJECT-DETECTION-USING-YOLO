# Live Object Detection with YOLO and OpenCV

This project demonstrates real-time object detection using YOLO (You Only Look Once) on a webcam feed, implemented with Python and OpenCV. The Ultralytics YOLOv5 library is used for efficient and accurate object detection.

---

## Overview

This project utilizes the YOLO object detection algorithm to perform real-time object detection on a live webcam feed. It detects and annotates various objects in the frame with bounding boxes and labels, providing a seamless visual representation of detected objects and their confidence scores.

---

## Dependencies

Ensure you have the following dependencies installed:

- `cv2` (OpenCV for Python)
- `cvzone` (CVZone library for utilities like `cornerRect` and `putTextRect`)
- `math` (Standard Python library)
- `ultralytics.yolov5` (Ultralytics YOLOv5 library for object detection)

## Setup

To run this project locally:

1. **Clone the repository:**
   ```
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```


## Usage

- Ensure your webcam is connected and accessible.
- Run the script, which will open a window displaying real-time object detection on the webcam feed.
- Detected objects will be annotated with labels and confidence scores.

---

## Dataset

The YOLO model used in this project is pretrained. No specific dataset is required for running the demo, as it uses a pretrained model for inference.

---

## Notes

- This implementation uses a pretrained YOLO model from Ultralytics, which supports a wide range of object classes.
- Make sure your environment has GPU support if aiming for real-time performance with higher resolution streams.
- Feel free to explore and modify the code to suit different applications or use cases.


## Credits

- YOLOv5 by Ultralytics: https://github.com/ultralytics/yolov5
- OpenCV: https://github.com/opencv/opencv

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

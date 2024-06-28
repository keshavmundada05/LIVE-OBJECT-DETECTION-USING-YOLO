import cvzone
from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov8l.pt')
results = model("object images/download.jpeg", show=True)
cv2.waitKey(0)


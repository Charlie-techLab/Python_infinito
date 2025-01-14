import cv2
from win32api import GetSystemMetrics
import datetime
from PIL import ImageGrab
import numpy as np

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'output_{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Error: Could not open webcam.")
    exit()

print(width, height)

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    ret, frame = webcam.read()
    if not ret:
        print("Error: Failed to capture image")
        break
    fr_height, fr_width, _ = frame.shape
    img_final[0:fr_height, 0: fr_width, :] = frame[0: fr_height, 0: fr_width]
    print(fr_height, fr_width)
    cv2.imshow('Secret Capture', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break

webcam.release()
captured_video.release()
cv2.destroyAllWindows()

from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

video_path = './video.mp4'
capture = cv2.VideoCapture(video_path)

ret = True

while ret:
    ret, frame = capture.read()
    # print(frame)
    results = model.track(frame, persist=True)

    frame_ = results[0].plot()

    cv2.imshow('frame', frame_)
    if cv2.waitKey(55) & 0xFF == ord('q'):
        break
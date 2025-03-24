import cv2

video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) == ord('q'):
        break
video_capture.release()
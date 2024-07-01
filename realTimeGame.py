import cv2 
from ultralytics import YOLO
import numpy as np
from helper import winner_decide

# loading yolo model for rock paper scissor detection
model = YOLO("models/rps.pt")

# cam capture object cv2
video = cv2.VideoCapture(0)


while True:
    ret, frame  = video.read()

    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)
    cols, rows, _ = frame.shape # get the size of the frame

    # draw a line in the center 
    cv2.line(frame, (int(rows/2), 0), (int(rows/2), cols), (200, 210, 220), 2)

    # make prediction on frame
    results = model(frame)

    # Imp parameters
    classes = results[0].names  # dict of classes
    obj_detected = results[0].boxes.cls  # object detected
    obj_cordinates_float = results[0].boxes.xyxy.tolist() # cordinates of obj

    classes_detected = [classes[int(obj)] for obj in obj_detected]

    obj_cordinates_int = []
    for cordinates in obj_cordinates_float:
        temp = [[int(cordinates[i]), int(cordinates[i+1])] for i in range(0, len(cordinates), 2)]
        obj_cordinates_int.append(temp)

    winner = winner_decide(classes_detected, frame, rows)

    for i, cordinates in enumerate(obj_cordinates_int):
        if classes_detected[i] == winner:
            cv2.rectangle(frame, cordinates[0], cordinates[1], (0, 255, 0), 2)
            cv2.putText(frame, classes_detected[i], cordinates[0], 1, cv2.FONT_HERSHEY_COMPLEX, (0, 255, 0), 2)
        else:
            cv2.rectangle(frame, cordinates[0], cordinates[1], (0, 0, 255), 2)
            cv2.putText(frame, classes_detected[i], cordinates[0], 1, cv2.FONT_HERSHEY_COMPLEX, (0, 0, 255), 2)

    cv2.imshow("frame", frame)
    if cv2.waitKey(25) & 0xff == 27:
        break

video.release()
cv2.destroyAllWindows()
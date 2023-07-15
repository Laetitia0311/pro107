#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 22:21:23 2023

@author: tish9an
"""


import cv2

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3, 1)
    cv2.putText(img, "Tracking", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

def goal_track():
    video = cv2.VideoCapture("footvolleyball.mp4")  
    tracker = cv2.TrackerCSRT_create() 

    while True:
        check, img = video.read()
        success, bbox = tracker.update(img)

        if success:
            drawBox(img, bbox)
        else:
            cv2.putText(img, "LOST", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("Tracking", img)
        key = cv2.waitKey(1)

        if key == ord('q'):
            print("Closing")
            break

    video.release()
    cv2.destroyAllWindows()

goal_track()

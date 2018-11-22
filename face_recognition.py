# -*- coding: utf-8 -*-
import cv2
import time
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
while True:
   ret,img = cap.read()
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   faces = face_cascade.detectMultiScale(gray, 1.3, 5)
   for (x,y,w,h) in faces:
     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
     cv2.namedWindow("img", 0)
     cv2.imshow('img',img)

   if len(faces):
    count = len(faces)
    print "找到 {0} 个脸!".format(len(faces))

   else:
    print "没有人脸!"
   time.sleep(3)
   if cv2.waitKey(1) &0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()

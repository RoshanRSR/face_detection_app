import cv2

#load haar cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#  start ccamera
cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  #convert  to  grayscale
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # detect face
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

  #draw rectangle
  for(x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y),(x+w, y+h), (255,0,0), 2)
  cv2.imshow("Face detection", frame)
  # press q to exit
  if cv2.waitKey(1) & 0xFF ==ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
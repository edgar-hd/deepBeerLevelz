desc = '''Script to produce glass volume in real time.

Press 'q' to quit.

'''

from keras.models import load_model
import cv2
import numpy as np
from random import choice

model = load_model("deepBeerLevelz.h5")

cap = cv2.VideoCapture(0)           # Start camera
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # turn the autofocus off
cap.set(28, 560) 

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # rectangle for user to play
    cv2.rectangle(frame, (320, 000), (640, 500), (255, 255, 255), 2)

    # extract the region of image within the user rectangle
    roi = frame[000:500, 320:640]   # Define ROI to match drawing,
    img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (227, 227))


    # predict the move made
    pred = model.predict(np.array([img]))
    move_code = pred[0,0]

    # display the information
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Volume: " + str(move_code) + "ml",
                (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Test", frame)

    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

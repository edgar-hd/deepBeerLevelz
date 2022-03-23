desc = '''Script to gather data images with a particular label.

Usage: python gather_images.py <label_name> <num_samples>

The script will collect <num_samples> number of images and store them
in its own directory.

Only the portion of the image within the box displayed
will be captured and stored.

Press 'a' to start/pause the image collecting process.
Press 'q' to quit.

'''

import cv2
import os
import sys

try:
    label_name = sys.argv[1]        # Inputs, name to classify and number of samples
    num_samples = int(sys.argv[2])
except:
    print("Arguments missing.")
    print(desc)
    exit(-1)

IMG_SAVE_PATH = 'image_data'        # Where to save the images
IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, label_name)

try:
    os.mkdir(IMG_SAVE_PATH)         # Make the directory for all data
except FileExistsError:             # Unless it already exists
    pass
try:
    os.mkdir(IMG_CLASS_PATH)        # Make the directory for this data
except FileExistsError:             # Unless it already exists
    print("{} directory already exists.".format(IMG_CLASS_PATH))
    print("All images gathered will be saved along with existing items in this folder")

cap = cv2.VideoCapture(0)           # Start camera
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # turn the autofocus off
cap.set(28, 600) 

start = False
count = 0

while True:         # I guess just captures every possible frame, no?
    ret, frame = cap.read()
    if not ret:     #Unclear, probably to make sure camera is active
        continue

    if count == num_samples:    #If sample number is collected, then finish
        break

    #Make rectangle frame for image, on what, coordinates, colour and thickness
    cv2.rectangle(frame, (320, 000), (640, 500), (255, 255, 255), 2)

    if start:
        roi = frame[000:500, 320:640]   # Define ROI to match drawing,
        save_path = os.path.join(IMG_CLASS_PATH, '{}.jpg'.format(count + 1))
        cv2.imwrite(save_path, roi)     # Where to write and increase counter
        count += 1

    font = cv2.FONT_HERSHEY_SIMPLEX     # Define font of numbers
    cv2.putText(frame, "Collecting {}".format(count),   # Writes text of collecting #
            (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Collecting images", frame)

    k = cv2.waitKey(10)
    if k == ord('a'):       # Start if 'a'
        start = not start

    if k == ord('q'):       # Quit if 'q'
        break

print("\n{} image(s) saved to {}".format(count, IMG_CLASS_PATH))
cap.release()   # stop recording
cv2.destroyAllWindows() # close recording window

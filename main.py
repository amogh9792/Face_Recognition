import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Initialize video capture from default camera (0)
video_capture = cv2.VideoCapture(0)

# Load known faces
amoghs_image = face_recognition.load_image_file("faces/amogh.jpg")
amogh_encoding = face_recognition.face_encodings(amoghs_image)[0]

akshay_image = face_recognition.load_image_file("faces/akshay.jpg")
akshay_encoding = face_recognition.face_encodings(akshay_image)[0]

known_face_encodings = [amogh_encoding, akshay_encoding]
known_face_names = ["Amogh", "Akshay"]

# List of expected students
students = known_face_names.copy()

# Get the current date and time
now = datetime.now()
current_date = datetime.now().strftime("%Y_%m_%d")

# Create and open a CSV file for writing
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Adds a text if the person is present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])

    cv2.imshow("Attendance", frame)

    # Check for the 'q' key press to break the loop
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release video capture and close all windows
video_capture.release()
cv2.destroyAllWindows()

# Close the CSV file
f.close()

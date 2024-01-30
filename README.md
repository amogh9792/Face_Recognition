```markdown
# Face Recognition Attendance System

This repository contains code for a simple face recognition attendance system using Python and OpenCV.

## Requirements

- Python 3.x
- OpenCV
- face_recognition
- numpy
- csv

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your_username/face-recognition-attendance.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure that your webcam is connected and working properly.

2. Run the script `attendance_system.py`:

   ```bash
   python attendance_system.py
   ```

3. The system will capture live video from your webcam and attempt to recognize faces in the frame.

4. If a recognized face matches one of the known faces in the database, it will mark the attendance in a CSV file named with the current date.

5. Press the 'q' key to exit the program.

## How it works

- The script captures video frames from the webcam and uses the `face_recognition` library to detect and recognize faces.
- It compares the detected face encodings with the known face encodings stored in the system.
- If a match is found, it marks the attendance and records the student's name and current time in a CSV file.
- The attendance record is saved in a CSV file with the format `YYYY_MM_DD.csv`.

## Contributors

- [Your Name](https://github.com/your_username)

Feel free to contribute to this project by submitting bug fixes, enhancements, or new features.

## License

This project is licensed under the [MIT License](LICENSE).
```

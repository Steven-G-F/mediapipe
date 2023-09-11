# A default setup for hand tracking

import cv2
import mediapipe as mp

# Setup

# Get video capture
vid=cv2.VideoCapture(0)

# Get hands data
mp_hands=mp.solutions.hands
hands=mp_hands.Hands()
mp_drawing=mp.solutions.drawing_utils

# Loop
while True:
    # Get the current frame and if it is visible
    ret, frame=vid.read()

    # Exit program if no image is displayed
    if not ret: 
        break
    
    # Resize the frame
    scale=1.5
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    frame=cv2.flip(cv2.resize(frame, (width,height)),1)

    # Draw the hand trackers
    analysis=hands.process(frame)

    if analysis.multi_hand_landmarks:
        for landmarks in analysis.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)


    # Display frame
    cv2.imshow("Frame", frame)
    key=cv2.waitKey(1) & 0xFF

    # Quit if q is pressed
    if key==ord('q'):
        break

    

vid.release()
cv2.destroyAllWindows()
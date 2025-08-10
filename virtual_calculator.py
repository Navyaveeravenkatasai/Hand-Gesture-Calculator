import cv2
import numpy as np
import time
import math
import mediapipe as mp

# === Mediapipe Setup ===
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)

# === Button Class ===
class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, frame, hover=False):
        x, y = self.pos
        color = (0, 255, 0) if hover else (0, 0, 0)
        cv2.rectangle(frame, self.pos, (x + self.width, y + self.height), color, cv2.FILLED)
        cv2.rectangle(frame, self.pos, (x + self.width, y + self.height), (50, 50, 50), 3)
        cv2.putText(frame, self.value, (x + 25, y + 55), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

    def is_hover(self, x, y):
        bx, by = self.pos
        return bx < x < bx + self.width and by < y < by + self.height

# === Calculator Layout ===
keys = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

button_list = []
button_width = 100
button_height = 80
start_x = 50
start_y = 150

for i in range(4):
    for j in range(4):
        xpos = j * button_width + start_x
        ypos = i * button_height + start_y
        button_list.append(Button((xpos, ypos), button_width, button_height, keys[i][j]))

expression = ""
last_click_time = 0
click_delay = 1

# Set webcam resolution to fit layout
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    h, w, c = frame.shape

    # Draw all buttons
    for button in button_list:
        button.draw(frame)

    # Display the current expression
    cv2.rectangle(frame, (start_x, 50), (start_x + 4 * button_width, 130), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, expression, (start_x + 10, 115), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        lm_list = []
        for id, lm in enumerate(hand_landmarks.landmark):
            cx, cy = int(lm.x * w), int(lm.y * h)
            lm_list.append((cx, cy))

        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Check for pinch (thumb tip & index tip)
        if lm_list:
            x1, y1 = lm_list[4]   # Thumb tip
            x2, y2 = lm_list[8]   # Index tip
            length = math.hypot(x2 - x1, y2 - y1)

            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            current_time = time.time()

            if length < 40 and (current_time - last_click_time) > click_delay:
                for button in button_list:
                    if button.is_hover(cx, cy):
                        selected = button.value

                        if selected == "C":
                            expression = ""
                        elif selected == "=":
                            try:
                                expression = str(eval(expression))
                            except:
                                expression = "Error"
                        else:
                            expression += selected

                        last_click_time = current_time

                # Visual feedback
                cv2.circle(frame, (cx, cy), 15, (0, 255, 255), cv2.FILLED)

    cv2.imshow("Virtual Calculator - Day 7", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

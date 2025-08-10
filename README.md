
# Hand Gesture Calculator 🖐️➕➖✖️➗

A virtual calculator that detects **hand gestures** via a webcam to perform mathematical calculations. Built with **Python**, **OpenCV**, and **MediaPipe**, this project allows you to interact with on-screen calculator buttons without physically touching a device — making it a fun and innovative demonstration of computer vision and gesture control.

---

## 📌 Features

* **Hand Gesture Recognition** – Uses your webcam to detect hand movements and gestures.
* **Interactive On-Screen Buttons** – Click calculator buttons using finger hover/tap gestures.
* **Real-Time Processing** – Immediate visual feedback and calculation results.
* **Customizable UI** – Adjustable button positions, colors, and calculator layout.
* **Touchless Control** – No physical contact needed — perfect for contactless tech demos.

---

## 🛠️ Tech Stack

* **Programming Language:** Python 3.x
* **Libraries:**

  * [OpenCV](https://opencv.org/) – for video capture and image processing
  * [MediaPipe](https://developers.google.com/mediapipe) – for hand tracking
  * NumPy – for numerical operations
  * Math – for calculation logic

---

## 📂 Project Structure

```
📁 HandGestureCalculator
 ├── calculator.py        # Main program file
 ├── README.md            # Project documentation
 └── requirements.txt     # List of dependencies
```

**Core Components:**

* **Button Class** (`Button`) – Manages position, size, hover effects, and drawing of calculator buttons.
* **Hand Tracking** – Tracks fingertip coordinates to detect button interactions.
* **Calculation Logic** – Processes clicked values and displays results.

---

## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/HandGestureCalculator.git
cd HandGestureCalculator
```

### 2️⃣ Install Dependencies

Make sure you have Python installed. Then run:

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
opencv-python
mediapipe
numpy
```

### 3️⃣ Run the Program

```bash
python calculator.py
```

---

## 📸 Usage Instructions

1. **Position yourself** in front of your webcam.
2. **Move your index finger** to hover over a button.
3. **Tap gesture** or keep your finger inside the button area to "click".
4. Perform operations as you would on a normal calculator.

---

## 🎯 Example Gesture Workflow

* Hover finger over **`7`**
* Tap to select → Display updates with `7`
* Hover over **`+`**
* Tap to select → Display updates with `7+`
* Hover over **`3`** and tap → `7+3`
* Hover over **`=`** and tap → Result `10` displayed

---

## 🔮 Future Improvements

* Add **scientific calculator** functions (sin, cos, tan, log, etc.)
* Multi-hand support for advanced gestures
* Improve **gesture accuracy** with better filtering
* Touchless keyboard integration

---

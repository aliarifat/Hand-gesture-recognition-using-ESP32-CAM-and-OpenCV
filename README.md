# 🤖 ESP32-CAM-Based Hand Gesture Detector  

Hello, friends! I hope you're doing well. Today, we are building an exciting image processing project using the ESP32-CAM. Gesture-controlled systems are widely used today—from smartphones that capture photos using hand gestures to robots controlled without touch.  

In this project, we will create a real-time hand gesture detector using the ESP32-CAM and Python. The ESP32-CAM captures images and serves them over Wi-Fi, while a Python application processes those images using OpenCV and MediaPipe to detect and classify hand gestures.  

The system can recognize the following gestures:  
- Open Hand  
- Fist  
- Thumbs Up  
- Index Up  

---

## 🚀 Applications  
- Gesture-controlled robots  
- Sign language assistance systems  
- Human-computer interaction  
- Smart home control systems  
- Body language analysis  

---

## 🧩 System Architecture  

This system is divided into two main parts:

### ESP32-CAM (Image Capture Layer)  
- Captures images at 800×600 resolution  
- Hosts an HTTP server  
- Serves images via:  
http://<ESP32_IP>/cam-hi.jpg  

### Python Processing System  
- Fetches images over Wi-Fi  
- Uses OpenCV for image processing  
- Uses MediaPipe for hand tracking  
- Detects gestures using custom logic  
- Displays output in real time  

### Workflow  
ESP32-CAM → WiFi HTTP Server → Python Script → OpenCV → MediaPipe → Gesture Detection → Display Output  

---

## 🧰 Hardware Requirements  

ESP32-CAM Module – 1  
FTDI USB-to-Serial Converter – 1  
Jumper Wires – ~5  
Micro USB Cable – 1  

---

## 🔌 Circuit Connections  

ESP32-CAM → FTDI  
VCC → 5V  
GND → GND  
U0R → TX  
U0T → RX  
IO0 → GND (for flashing)  

After uploading the code, disconnect IO0 from GND and press reset.  

---

## 💻 Project Files  

ESP32 Code: esp32_cam_basic.ino  
Python Script: hand_gesture_ESP32CAM.py  

---
## 📦 Installing Required Libraries  

Before running the project, make sure the required Python libraries are installed. These libraries are used for image processing, hand tracking, and handling data.

Install the following libraries:

- mediapipe → for hand detection and landmark tracking  
- numpy → for handling image data and arrays  
- urllib → used to fetch images from the ESP32-CAM (built-in, no installation required)  

Run the following commands in your terminal:

pip install mediapipe  
pip install numpy  

Note: urllib comes pre-installed with Python, so you don’t need to install it separately.

## ⚙️ Setup Instructions  

### 1. ESP32-CAM Setup  
- Install ESP32 board in Arduino IDE  
- Upload esp32_cam_basic.ino  
- Open Serial Monitor  
- Copy IP address  

### 2. Python Environment  
- Create a virtual environment  
- Install required libraries:  
  opencv-python  
  mediapipe  
  numpy  

### 3. Run the Project  
- Update ESP32-CAM URL in hand_gesture_esp32.py  
- Run the Python script  

---

## 📸 Demo  

- Place your hand in front of the camera  
- The system detects hand landmarks  
- Gesture name is displayed in real time  

---

## ⚡ Performance Tips  

- Use good lighting  
- Keep hand clearly visible  
- Avoid complex backgrounds  
- Maintain proper distance  

---

## 🔧 Possible Improvements  

- Add more gestures  
- Control devices using gestures  
- Build a web dashboard  
- Optimize performance  
- Integrate with IoT systems  

---

## 🧪 Testing  

- Power up ESP32-CAM  
- Run Python script  
- Show different gestures  
- Verify detection  

---

## 🛠️ Troubleshooting  

- No image: Check IP address and Wi-Fi  
- Camera fail: Check connections and power  
- Upload issue: Press RST button  
- MediaPipe error: Install dependencies properly  
- Poor detection: Improve lighting  

---

## ⚠️ Limitations  

- Depends on lighting conditions  
- Limited gesture set  
- Requires a computer for processing  
- Accuracy varies with hand position  

---

## 📌 Conclusion  

This project combines ESP32-CAM, OpenCV, and MediaPipe to create a real-time hand gesture recognition system. It demonstrates how embedded systems and computer vision can work together to build interactive applications.  

---

## 📚 References  

ESP32-CAM documentation  
OpenCV documentation  
MediaPipe documentation  
FTDI drivers  
CP210x drivers  

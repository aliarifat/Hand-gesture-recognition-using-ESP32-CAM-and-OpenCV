import cv2
import mediapipe as mp
import numpy as np
import urllib.request

# Replace this with your ESP32-CAM URL
ESP32_CAM_URL = "http://192.168.1.103/cam-hi.jpg"

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def get_frame():
    try:
        img_resp = urllib.request.urlopen(ESP32_CAM_URL)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        img = cv2.imdecode(imgnp, cv2.IMREAD_COLOR)  # make sure image is color
        return img
    except Exception as e:
        print(f"Error getting frame: {e}")
        return None

def detect_gesture(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]

    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    index_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]

    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    middle_pip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]

    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    ring_pip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP]

    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    pinky_pip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP]

    fingers = {
        "thumb": thumb_tip.y < thumb_mcp.y,
        "index": index_tip.y < index_pip.y,
        "middle": middle_tip.y < middle_pip.y,
        "ring": ring_tip.y < ring_pip.y,
        "pinky": pinky_tip.y < pinky_pip.y,
    }

    if not any(fingers.values()):
        return "Fist"
    elif fingers["thumb"] and not fingers["index"] and not fingers["middle"] and not fingers["ring"] and not fingers["pinky"]:
        return "Thumbs Up"
    elif fingers["index"] and not fingers["middle"] and not fingers["ring"] and not fingers["pinky"]:
        return "Index Up"
    elif all([fingers["index"], fingers["middle"], fingers["ring"], fingers["pinky"]]):
        return "Open Hand"
    else:
        return "Unknown Gesture"

while True:
    frame = get_frame()
    if frame is None:
        continue  # skip this loop if error fetching frame

    frame = cv2.flip(frame, 1)  # Flip horizontally
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture_name = detect_gesture(hand_landmarks)
            cv2.putText(frame, gesture_name, (30, 60), cv2.FONT_HERSHEY_SIMPLEX,
                        1.2, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(5) & 0xFF == 27:  # ESC to exit
        break

cv2.destroyAllWindows()

import streamlit as st
import av
from streamlit_webrtc import webrtc_streamer

st.title("Live Face Detection App")

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")  # Convert frame to OpenCV format
    
    # Convert to grayscale (example processing)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    return av.VideoFrame.from_ndarray(img, format="bgr24")

# Start WebRTC-based video stream
webrtc_streamer(key="face-detection", video_frame_callback=video_frame_callback)

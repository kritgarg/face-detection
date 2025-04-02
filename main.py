import cv2
import streamlit as st
from PIL import Image
import numpy as np

st.title("Live Webcam Stream")

video_capture = cv2.VideoCapture(0)
frame_placeholder = st.empty()

while True:
    ret, frame = video_capture.read()
    if not ret:
        st.write("Failed to capture video")
        break
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame, channels="RGB")

video_capture.release()

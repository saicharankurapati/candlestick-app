import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title('Candlestick Pattern Detector')

uploaded_file = st.file_uploader('Upload candlestick chart image', type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_np = np.array(image)
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if 5 < w < 30 and h > 20:
            cv2.rectangle(img_np, (x, y), (x + w, y + h), (0, 255, 0), 2)
    st.image(img_np, caption='Detected Candles', use_container_width=True)


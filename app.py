import streamlit as st

st.set_page_config(page_title="Candlestick Predictor", layout="centered")

st.title("📈 Candlestick Next Candle Predictor")
st.markdown("Enter the last candlestick's OHLC data below:")

# Input fields
open_price = st.number_input("Open Price", format="%.2f")
high_price = st.number_input("High Price", format="%.2f")
low_price = st.number_input("Low Price", format="%.2f")
close_price = st.number_input("Close Price", format="%.2f")

def predict_candle(open_p, high_p, low_p, close_p):
    body = abs(close_p - open_p)
    upper_wick = high_p - max(open_p, close_p)
    lower_wick = min(open_p, close_p) - low_p

    if close_p > open_p and body > upper_wick and body > lower_wick:
        return "📗 Bullish Candle - Possible uptrend"
    elif open_p > close_p and body > upper_wick and body > lower_wick:
        return "📕 Bearish Candle - Possible downtrend"
    elif upper_wick > body and upper_wick > lower_wick:
        return "📘 Shooting Star - Possible bearish reversal"
    elif lower_wick > body and lower_wick > upper_wick:
        return "📙 Hammer - Possible bullish reversal"
    else:
        return "🔍 Indecisive or neutral candle (Doji or Spinning Top)"

if st.button("Predict Next Candle"):
    if high_price >= max(open_price, close_price) and low_price <= min(open_price, close_price):
        result = predict_candle(open_price, high_price, low_price, close_price)
        st.success(f"Prediction: {result}")
    else:
        st.error("⚠️ High must be ≥ open/close and Low must be ≤ open/close")

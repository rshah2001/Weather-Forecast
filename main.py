import streamlit as st

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:")

forecast = st.slider("Forecast Days: ", min_value=1, max_value=5, help="Select the number of forcasted days")

data_to_view = st.selectbox(label="Select Data to view",options=["Temperature", "Sky"])

st.subheader(f"{data_to_view} for the next {forecast} day(s) in {place}")

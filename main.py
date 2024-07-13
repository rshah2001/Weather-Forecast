import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:")

forecast = st.slider("Forecast Days: ", min_value=1, max_value=5, help="Select the number of forcasted days")

data_to_view = st.selectbox(label="Select Data to view",options=["Temperature", "Sky"])

st.subheader(f"{data_to_view} for the next {forecast} day(s) in {place}")

def get_data(forecast):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10,11,15]
    temperatures = [forecast * i for i in temperatures]
    return dates, temperatures


d, t = get_data(forecast)

figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperatures(C)"})
st.plotly_chart(figure)

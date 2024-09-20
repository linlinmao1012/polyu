
import json
import requests
import streamlit as st
#open the file
with open('weather.json') as f:
    temperature = json.load(f)  
#将读取到的数据转换为字典
temperature_dict = json.loads(temperature.text)

#让用户通过选择框选择地区
location = st.selectbox("Select a location", temperature_dict["temperature"]["data"])
#根据用户选择的地区显示该地区的温度
st.write("Temperature:", location["value"] + "°C")
#以柱形图的方式显示所有地区温度
st.bar_chart([float(location["value"]) for location in temperature_dict["temperature"]["data"]])


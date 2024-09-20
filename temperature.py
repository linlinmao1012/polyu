import json
import streamlit as st

with open('weather.json') as f:
    temperature = json.load(f)

#读取temperature里的所有place作为key，对应的温度作为其value，生成一个字典
places = {region['place']: region['value'] for region in temperature['temperature']['data']}
#将页面分成左右两边 

left_column, right_column = st.columns(2)

#在页面的左半边生成一个初始选择框，显示框内包含所有地区,默认选中第一个地区
with left_column:
     region = st.selectbox("Select a region", list(places.keys()), index=0)
#显示所选地区的温度
     st.write("Temperature in", region, "is", places[region],"°C")

with right_column:
#生成一个柱状图，显示所有地区的温度
      st.write("Temperature distribution:")
      st.bar_chart(places)







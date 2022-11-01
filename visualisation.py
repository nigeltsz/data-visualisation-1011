import streamlit as st
import plotly_express as px
import pandas as pd
import streamlit.components.v1 as components
import json
import time as time

st.set_page_config(layout = 'wide')
st.title("Dangerous Driving Behavior Identification Application")   

def get_data() :
    url = 'http://127.0.0.1:5000/' 
    df = pd.read_json(url)
    return df

placeholder = st.empty()
placeholder2 = st.empty()


while True:
    df = get_data()
    print(df)

    #Layout
    with placeholder.container():
        firstCol, secondCol=st.columns([3,1])

        with firstCol:
            firstCol.subheader("Map")
            p = open("map.html")
            components.html(p.read())
        dangerous=df._get_value(10, 'safety_value')

        with secondCol:
            secondCol.subheader("Verdict")
            if dangerous == 1:
                st.error('🚨 Dangerous driver 🚨')
            elif dangerous == 0 :
                st.success('Safe driver')

    with placeholder2.container():
        firstCol2,secondCol2=st.columns(2)

        with firstCol2:
            firstCol2.subheader("Charts 1")
            acceleration_x_plot = px.line(df, x=df.index, y="acceleration_x", color=None, title="Acceleration of x")
            st.write(acceleration_x_plot)

            acceleration_y_plot = px.line(data_frame=df, x=df.index, y="acceleration_y", color=None, title="Acceleration of y")
            st.write(acceleration_y_plot)

            acceleration_z_plot = px.line(data_frame=df, x=df.index, y="acceleration_z", color=None, title="Acceleration of z")
            st.write(acceleration_z_plot)
            
            accuracy_plot = px.line(data_frame=df, x=df.index, y="accuracy", color=None, title="Accuracy")
            st.write(accuracy_plot)

            bearing_plot = px.line(data_frame=df, x=df.index, y="bearing", color=None, title="Bearing")
            st.write(bearing_plot)

        with secondCol2:
            secondCol2.subheader("Charts 2")
            gyro_x_plot = px.line(data_frame=df, x=df.index, y="gyro_x", color=None, title="Gyro of x")
            st.write(gyro_x_plot)

            gyro_y_plot = px.line(data_frame=df, x=df.index, y="gyro_y", color=None, title="Gyro of y")
            st.write(gyro_y_plot)

            gyro_z_plot = px.line(data_frame=df, x=df.index, y="gyro_z", color=None, title="Gyro of z")
            st.write(gyro_z_plot)

            second_plot = px.line(data_frame=df, x=df.index, y="second", color=None, title="second")
            st.write(second_plot)

            speed_plot = px.line(data_frame=df, x=df.index, y="speed", color=None, title="Speed")
            st.write(speed_plot)
    time.sleep(5)

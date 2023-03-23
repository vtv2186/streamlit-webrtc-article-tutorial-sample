#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:38:03 2023

@author: sirishalanka
"""
import streamlit as st
import av
import cv2
from streamlit_webrtc import webrtc_streamer

st.title("my first streamlit app")
st.write("hellow,world")

threshold1 = st.slider("threshold", min_value =0, max_value=1000,step=1,value=100)
threshold2 = st.slider("Threshold2", min_value=0, max_value=1000, step=1, value=200)

def callback(frame):
    img = frame.to_ndarray(format="bgr24")

    img = cv2.cvtColor(cv2.Canny(img, threshold1, threshold2), cv2.COLOR_GRAY2BGR)

    return av.VideoFrame.from_ndarray(img, format="bgr24")


class VideoProcessor:
    def __init__(self) -> None:
        self.threshold1 = 100
        self.threshold2 = 200

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        img = cv2.cvtColor(cv2.Canny(img, self.threshold1, self.threshold2), cv2.COLOR_GRAY2BGR)

        return av.VideoFrame.from_ndarray(img, format="bgr24")




ctx=webrtc_streamer(key="example",
                video_processor_factory=VideoProcessor,
                rtc_configuration={  # Add this line
      # "iceServers": [{"urls": ["stun:stun4.l.google.com:19302"]}]
       "iceServers": [{   "urls": [ "stun:ws-turn1.xirsys.com" ]}, {   "username": "_gOvGuKm6kPUXW7I78axfsf8e7hlY2VaJziOfzYjFnnEZqUb50vvQhQQzevloqKTAAAAAGQc1ox2aXNobnV0ZWph",   "credential": "6b2aa7c4-c9cc-11ed-b509-0242ac140004",   "urls": [       "turn:ws-turn1.xirsys.com:80?transport=udp",       "turn:ws-turn1.xirsys.com:3478?transport=udp",       "turn:ws-turn1.xirsys.com:80?transport=tcp",       "turn:ws-turn1.xirsys.com:3478?transport=tcp",       "turns:ws-turn1.xirsys.com:443?transport=tcp",       "turns:ws-turn1.xirsys.com:5349?transport=tcp"   ]}]
    }
    )

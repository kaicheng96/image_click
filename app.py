import os
import time
import comtypes
import cv2
# import pyperclip
# import pyautogui
from uiautomation import WindowControl, MenuControl
import gradio as gr
import numpy as np
import os
os.environ['DISPLAY'] = ':0'
def mouseClick(img):
    location = pyautogui.locateCenterOnScreen(img, confidence=0.8)
    if location is not None:
        pyautogui.click(location.x, location.y, clicks=1, interval=0.2, duration=0.2, button="left")
        return True;
    else:
        return False;

def doTask(task):
    if task["type"] == "单击图片":
        img = task["content"];
        return mouseClick(img);
# define core fn, which returns a generator {steps} times before returning the image
def myfunction(image1,image2,steps):
        time.sleep(1)
        taskList = [
            {"type": "单击图片", "content": image1},
            {"type": "单击图片", "content": image2},
        ]

        for n in range(steps):
            i = 0;
            while i<len(taskList):
                if(doTask(taskList[i])):
                    i += 1;
                    time.sleep(2)
                else:
                    time.sleep(100)
            text = "Running"
        return text

demo = gr.Interface(fn=myfunction,
                    inputs=["image","image",gr.Slider(1, 50, 1, step=1)],
                    outputs=None,)

demo.launch()



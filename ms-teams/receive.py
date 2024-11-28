import os
import time
import cv2
import pyautogui
import numpy as np
import subprocess
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator

def open_teams():
    try:
        #os.system("C:/Users/PRKOTE/AppData/Local/Microsoft/Teams/current/Teams.exe")
        teams_url = "https://teams.live.com/"
        path="C:/Program Files/Google/Chrome/Application/chrome.exe"
        subprocess.Popen([path, teams_url])
        time.sleep(10)  # Wait for Teams to open for 10 seconds
    except Exception as e:
        print(e)

def get_center_coordinates(box):
    x_min, y_min, x_max, y_max = box.xyxy[0]
    center_x = (x_min + x_max) / 2
    center_y = (y_min + y_max) / 2
    return center_x, center_y

def detect_and_click_search_rotation(model, teams_window, classname):
    clicked = False  # Variable to track if 'searchrotation' icon is clicked
    while True:
        # Capture the Teams window screenshot
        screenshot = pyautogui.screenshot(region=teams_window)

        # Convert the screenshot to OpenCV format
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Perform object detection
        results = model.predict(img, conf=0.25)

        # Process detections
        for r in results:
            boxes = r.boxes
            for box in boxes:
                b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
                c = box.cls
                class_name = model.names[int(c)]

                # Check if the detected class is "searchrotation" and it's not clicked before
                if class_name == classname and not clicked:
                    # Get center coordinates
                    center_x, center_y = get_center_coordinates(box)

                    # Perform a click action on the 'searchrotation' icon
                    pyautogui.click(teams_window[0] + center_x, teams_window[1] + center_y)
                    print("Clicked on 'searchrotation' icon")
                    clicked = True  # Set search_clicked to True
                    break  # Break out of the loop after clicking once

        if clicked:
            break  # Break out of the loop if 'searchrotation' icon is clicked

        # Wait for a short duration before capturing the next screenshot
        time.sleep(1)

# Open Teams
open_teams()

screen_width, screen_height = pyautogui.size()

# Define the Teams window region (full screen)
teams_window = (0, 0, screen_width, screen_height)  

# Load YOLO model
model_path = r"C:\Users\username\Downloads\best.pt"
model = YOLO(model_path)


#detect_and_click_search_rotation(model, teams_window, 'chatrotation')
time.sleep(1)
detect_and_click_search_rotation(model, teams_window, 'call-accept-audiorotation')
time.sleep(15)
detect_and_click_search_rotation(model, teams_window, 'call-leaverotation')
time.sleep(2)
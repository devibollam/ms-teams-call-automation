# MS Teams Automation
This Python project automates tasks within Microsoft Teams using YOLO object detection and pyautogui to interact with the Teams interface. The automation script performs several actions, including opening Teams, detecting specific icons within the Teams window, and interacting with the interface (such as clicking buttons and entering text).

# Prerequisites
Make sure you have the following libraries installed:
pyautogui
numpy
opencv-python
ultralytics (YOLOv8)
subprocess
time
os
# Setup
Microsoft Teams: This script opens Microsoft Teams via a URL or directly using the Teams application path. You can modify the path if required to point to your installation.

YOLO Model: This script uses a custom-trained YOLO model (best.pt) to detect specific items in the Teams window. Ensure the model is trained to detect the desired icons (e.g., "chatrotation", "searchrotation", etc.).

Environment: Update the model_path variable with the correct path to your YOLO model. Additionally, if necessary, adjust the teams_url or application path in the open_teams() function.

# Functions
open_teams()
Opens Microsoft Teams in a browser (via Google Chrome) or the installed application. It waits for a few seconds to ensure the application is loaded before starting further automation tasks.

get_center_coordinates(box)
Given the coordinates of a bounding box, this function calculates the center of the box, which is used for performing a click action on the detected object.

detect_and_click_search_rotation(model, teams_window, classname)
This function captures a screenshot of the Teams window, performs object detection using YOLO, and clicks on the detected item if it matches the specified classname (e.g., "chatrotation", "searchrotation"). It loops until the item is clicked, ensuring that it only clicks once.

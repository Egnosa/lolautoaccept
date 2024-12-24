# Version 2.5

import pygetwindow as gw
import time
import pyautogui
import win32gui

def bring_league_client_to_front():
    try:
        league_window = win32gui.FindWindow(None, "League of Legends")
        if league_window != 0:
            win32gui.ShowWindow(league_window, 5)  # SW_SHOW
            win32gui.SetForegroundWindow(league_window)
            return True
        else:
            print(get_timestamp(), "League of Legends client window not found.")
            return False
    except:
        print(get_timestamp(), "Error while bringing the League of Legends client to the front.")
        return False

def get_league_window_top_left():
    try:
        league_window = gw.getWindowsWithTitle("League of Legends")[0]
        if league_window:
            top_left = (league_window.left, league_window.top)
            print(get_timestamp(), f"Top-left corner of League window: {top_left}")
            return top_left
        else:
            print(get_timestamp(), "League of Legends client window not found.")
            return None
    except:
        print(get_timestamp(), "Error while getting the League of Legends window coordinates.")
        return None

def check_pixel_color(base_x, base_y):
    print(get_timestamp(), "Checking pixel color...")
    pixel_color = pyautogui.pixel(base_x + 574, base_y + 683)
    accepted_colors = [(30, 35, 40), (6, 7, 8)]
    if pixel_color == accepted_colors[0]:
        print(get_timestamp(), "Normal match search detected.")
        return True
    elif pixel_color == accepted_colors[1]:
        print(get_timestamp(), "Accept screen detected.")
        return True
    else:
        print(get_timestamp(), "No matching color found. Skipping.")
        return False

def perform_click(base_x, base_y):
    print(get_timestamp(), "Performing click at adjusted coordinates...")
    pyautogui.click(base_x + 634, base_y + 554)

def get_timestamp():
    return "[" + time.strftime("%Y-%m-%d %H:%M:%S") + "]"

print("Version 2.4")

while True:
    if bring_league_client_to_front():
        while True:
            top_left = get_league_window_top_left()
            if top_left:
                base_x, base_y = top_left
                if check_pixel_color(base_x, base_y):
                    perform_click(base_x, base_y)
                    time.sleep(5)  # Additional delay after performing click
                else:
                    time.sleep(5)
            else:
                print(get_timestamp(), "Unable to determine League of Legends window position.")
                break
    else:
        print(get_timestamp(), "League of Legends client not found. Retrying in 15 seconds.")
        time.sleep(15)

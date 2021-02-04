# Script by Muhamad Arsyad	
# Github : github.com/arsyadbruh	
# pip install pyautogui
# after running, it only has 3 seconds to enter the dank memer channel on discord
# change time on time.sleep(s)

import pyautogui
import time
import random

time.sleep(3)
listMeme = ['f','r','i','c','k','k','k','f','k','k']

while True:
    pyautogui.typewrite("pls hunt")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.typewrite("pls fish")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.typewrite("pls beg")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.typewrite("pls pm")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.typewrite(random.choice(listMeme))
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.typewrite("pls dep all")
    pyautogui.press("enter")
    time.sleep(52)

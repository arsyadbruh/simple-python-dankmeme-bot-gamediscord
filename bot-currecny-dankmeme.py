# Script by Muhamad Arsyad
# Github : github.com/arsyadbruh
# uncomment random untuk memakai random choice post meme
# pip install pyautogui
# setelah run, hanya punya waktu 3 detik untuk klik channel discord untuk dankmeme currency
# ubah aturan waktu pada time.sleep()

import pyautogui
import time
#import random

#listMeme = ['n','e','r','d']
time.sleep(3)
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
    # uncomment dibawah ini jika ingin menggunakan random choice post meme
    #pyautogui.typewrite(random.choice(listMeme)) 
    pyautogui.typewrite('r') #comment line ini jika ingin menggunakan random choice
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.typewrite("pls dep all")
    pyautogui.press("enter")
    time.sleep(52)

#have fun waktu di set selama +-1 menit

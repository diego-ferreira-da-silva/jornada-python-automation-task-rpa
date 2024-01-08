import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=735, y=373)
pyautogui.write("emailfake@email.com")
pyautogui.press("tab")
pyautogui.write("senhafake")
pyautogui.click(x=965, y=532)
time.sleep(3)
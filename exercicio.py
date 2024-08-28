import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=289, y=647)

time.sleep(1)

pyautogui.write("hashtagtreinamentos.com")
pyautogui.press("enter")
time.sleep(5)

pyautogui.moveTo(x=887, y=123, duration=1)
pyautogui.click(x=781, y=300)
time.sleep(3)

pyautogui.scroll(-300)

pyautogui.click(x=408, y=460)

pyautogui.write("Alan")
pyautogui.press("tab")
pyautogui.write("alanimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")





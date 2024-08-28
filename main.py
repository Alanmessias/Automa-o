import pyautogui
import time

pyautogui.PAUSE = 0.3

# Funções do mouse e tela
print(pyautogui.position())
print(pyautogui.size())

#Funções do mouse

time.sleep(5)
#pyautogui.click(x=738, y=134) clica em algum lugar
pyautogui.moveTo(x=954, y=124, duration=1)
pyautogui.click(x=855, y=266)
pyautogui.scroll(-200) #numero negativo = scroll para baixo

#Funções do teclado
pyautogui.write("Só Aprendendo")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")


import pyautogui
import time

print("dodo")
print(pyautogui.size())
time.sleep(2)
x, y = pyautogui.position()

while True :
    
    print(x, y)
    pyautogui.keyDown("command")
    pyautogui.press("r")
    pyautogui.keyUp("command")
    pyautogui.press("enter")
    time.sleep(0.6)
    for i in range(0, 5):
        pyautogui.click(x=x, y=y+i*4)
    for i in range(0, 5):
        pyautogui.click(x=x, y=y+i*4)
    

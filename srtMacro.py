import pyautogui
import time

print("dodo")
print(pyautogui.size())
time.sleep(2)
x, y = pyautogui.position()
print("loca : ", x, y)
ver = input("put version ( 1 : one pick 2 : 3 pick)")
offset=16
while True :
    
    print(x, y)
    pyautogui.keyDown("command")
    pyautogui.press("r")
    pyautogui.keyUp("command")
    pyautogui.press("enter")
    time.sleep(0.9)
    if ver == "1":
        for i in range(0, 5):
       	    pyautogui.click(x=x, y=y+i*6)
        for i in range(0, 5):
            pyautogui.click(x=x, y=y+i*6)
    
    if ver == "2":
        for i in range(0,5):
            pyautogui.click(x=x, y=y+i*4)
        for i in range(offset+0,offset+5):
            pyautogui.click(x=x, y=y+i*4)
        for i in range(offset*2+0,offset*2+5):
            pyautogui.click(x=x, y=y+i*4)



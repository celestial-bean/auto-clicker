import os

try:
    import win32api
except ImportError:
    os.system("pip install win32api")
    import win32api

try:
    import win32con
except ImportError:
    os.system("pip install win32con")
    import win32con

try:
    import time

except ImportError:
    os.system("pip install time")
    import time


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def wait():
    count=5
    while count>0:
        time.sleep(1)
        print(count)
        count-=1

def main():
    pos = win32api.GetCursorPos()
    while pos[0]>25 and pos[1]>25:
        time.sleep(speed)
        click()
        pos = win32api.GetCursorPos()


speed=1/int(input("clicks per second: "))

wait()
main()


print("failsafe")
quit()
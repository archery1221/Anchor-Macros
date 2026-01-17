import time
import pyautogui
import threading
import random
from pynput import keyboard

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True

def rnd():
    return random.uniform(0.08, 0.14)

def a1():
#DEĞİŞTİRİLECEK SATIRLAR
    for b1 in ['x', 'v', '"']: #<--- X=Anchor Tuşunuz V=GlowStone Yani Işıktaşı Tuşunuz ""= Totem Tuşunuz
        if b1 == 'v' and random.random() < 0.25:#<---Tırnak İçinde Verilen V Tuşu GlowStone Tuşunuz
            pyautogui.press('v')#<---GlowStone Tuşunuz
#DEĞİŞTİRİLECEK SATIRLAR
            pyautogui.click(button='right')
            time.sleep(rnd())
            continue

        pyautogui.press(b1)
        pyautogui.click(button='right')
        time.sleep(rnd())

def a2(key):
    try:
        if hasattr(key, 'char') and key.char == 'r':
            threading.Thread(target=a1).start()
        elif hasattr(key, 'vk') and key.vk == 0x52:
            threading.Thread(target=a1).start()
    except AttributeError:
        pass

with keyboard.Listener(on_press=a2) as listener:
    listener.join()

import random
import time
from pynput import mouse, keyboard
kb = keyboard.Controller()
click_time = 0  # 记录上一次点击时间
def on_click(x, y, button, pressed):
    global click_time
    if pressed and button == mouse.Button.left:
        now = time.time()
        if now - click_time < 0.3:  # 判断两次点击时间是否间隔很短（0.3秒内）
            num = str(random.randint(98, 99))
            time.sleep(0.02)
            kb.type(num)
        click_time = now
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
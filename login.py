import win32gui
import win32api
import win32con
import time
import cv2
from PIL import ImageGrab
import numpy as np



def find_window_by_title(title):
    hwnd = win32gui.FindWindow(None, title)
    return hwnd


def get_window_rect(hwnd):
    if hwnd:
        # 获取窗口在屏幕中的坐标
        rect = win32gui.GetWindowRect(hwnd)
        return rect
    else:
        return None


def click_on_screen(x, y):
    # 移动鼠标到指定位置
    win32api.SetCursorPos((x, y))
    # 模拟鼠标左键按下和释放
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)  # 短暂延迟
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# 在这里填入要点击的坐标


# # 根据窗口标题找到窗口句柄
# hwnd = find_window_by_title('梦幻西游：时空')
# rect = get_window_rect(hwnd)
# print(rect)
# # 点击指定坐标
# click_on_screen(click_x, click_y)
win_handle = win32gui.FindWindow(None, '梦幻西游：时空')
win32gui.SetForegroundWindow(win_handle)
time.sleep(1)
# win_x, xin_y, *_ = win32gui.GetWindowRect(win_handle)
click_x = 516
click_y = 470
win32api.SetCursorPos((click_x, click_y))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, click_x, click_y, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, click_x, click_y, 0, 0)
time.sleep(1)
click_x = 177
click_y = 384
win32api.SetCursorPos((click_x, click_y))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, click_x, click_y, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, click_x, click_y, 0, 0)
time.sleep(1)
click_x = 355
click_y = 218
win32api.SetCursorPos((click_x, click_y))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, click_x, click_y, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, click_x, click_y, 0, 0)
time.sleep(1)
while True:
    click_x = 336
    click_y = 338
    win32api.SetCursorPos((click_x, click_y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, click_x, click_y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, click_x, click_y, 0, 0)
    time.sleep(1)
    screen_shot = ImageGrab.grab()
    screen_shot.save("current_screen.png")
    img_b = cv2.imread('current_screen.png')
    img_a = cv2.imread('img.png')
    gray_b = cv2.cvtColor(img_b, cv2.COLOR_BGR2GRAY)
    gray_a = cv2.cvtColor(img_a, cv2.COLOR_BGR2GRAY)
    method = cv2.TM_CCOEFF_NORMED  # 或其他匹配方法
    res = cv2.matchTemplate(gray_b, gray_a, method)
    threshold = 0.8
    min_h, min_w, _ = img_a.shape

    locations = np.where(res >= threshold)

    # 查找所有超过阈值的匹配区域
    for pt in zip(*locations[::-1]):
        # 获取矩形框
        top_left = pt
        bottom_right = (pt[0] + min_w, pt[1] + min_h)

        # 判断是否完全包含
        if bottom_right[0] <= img_b.shape[1] and bottom_right[1] <= img_b.shape[0]:
            # 匹配区域完全位于图片B内，则认为图片A在B中
            print(time.strftime('%H:%M:%S'), "图片A在图片B中找到了！位置：", (top_left, bottom_right))
            break
    else:
        print("图片A未在图片B中找到。")
        exit()
    click_x = 515
    click_y = 540
    win32api.SetCursorPos((click_x, click_y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, click_x, click_y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, click_x, click_y, 0, 0)
    time.sleep(.5)
    click_x = 613
    click_y = 466
    win32api.SetCursorPos((click_x, click_y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, click_x, click_y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, click_x, click_y, 0, 0)
    time.sleep(.5)
import win32gui
import win32api
import win32con
import time
import pyautogui


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
click_x = 634
click_y = 552

# 根据窗口标题找到窗口句柄
hwnd = find_window_by_title('梦幻西游：时空')
rect = get_window_rect(hwnd)
print(rect)
# 点击指定坐标
click_on_screen(click_x, click_y)

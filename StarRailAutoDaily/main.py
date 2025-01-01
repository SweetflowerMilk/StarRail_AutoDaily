import 星标_搜索窗口
import win32gui
import time
import pyautogui
import cv2
import os
from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as MouseController, Button

def Click2(x, y):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)  # 主屏窗口
    w_left = left #+ 12  # 窗口坐标差
    w_top = top #+ 52  # 窗口坐标差
    ABSPosition = [(w_left + x), (w_top + y)]  # 在主屏上 窗口坐标差(-12,-52)
    pyautogui.moveTo(ABSPosition[0], ABSPosition[1], duration=0.05)
    pyautogui.click()
    print(f"点击了({ABSPosition})")
def Click1(x,y):
    win32gui.SetForegroundWindow(hwnd)
    pyautogui.moveTo(x, y, duration=0.05)
    pyautogui.click()
    print(f"点击了{x,y}")
def keyboard_simulation_example():
    keyboard_controller.press('a')
    keyboard_controller.release('a')
    keyboard_controller.press(Key.f9)
    keyboard_controller.release(Key.f9)
    mouse_controller.click(Button.right)
def 判断位置吻合(left, top, width, height,folder_name,tem_name,shot_name,threshold = 0.995):

    pyautogui.screenshot(region=(left, top, width, height)).save(f"./{folder_name}/{shot_name}")
    template = cv2.imread(os.path.join(folder_name,tem_name))
    image = cv2.imread(os.path.join(folder_name,shot_name))
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    threshold = threshold
    if max_val >= threshold:
        return True
    else:
        return False
def 基础判断(x0,y0,x1,y1,s1,ts=0.995):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    x, y = left + x0, top + y0
    w, h = x1 - x, y1 - y
    ff = r'1080p'
    tt = f'{s1}.png'
    ss = rf"{s1}_Check.png"
    星标_搜索窗口.聚焦窗口(hwnd)
    if 判断位置吻合(x, y, w, h, ff, tt, ss,threshold = ts):
        return True
    else:
        return False
def 判断大世界():#判断enter
    if 基础判断(85,967, 146,986, 'Enter'):
        print('在大世界')
        return True
    print('不在大世界')

def 判断是否可以再打一局():
    if 基础判断(1076,939, 1115,956, 'x40'): return True
    if 基础判断(1076,940, 1105,954, 'x1'): return True
def 判断是否战斗结束():
    if 基础判断(667,936, 760,957, 'Chafen_Exit'): return True
def 判断日活是否领完():
    if 基础判断(1588,288, 1634,366, 'v500'): return True

def 判断日活单项是否可以领取():
    if 基础判断(414,816,459,837,'LingQu',0.8): return True
def 判断日活单项可以领取几次():
    x = 0
    横差 = 912-577
    for i in range(4):
        if 基础判断(x0=414+x*横差, y0=816, x1=459+x*横差, y1=837, s1='LingQu',ts=0.8):
            x = x+1
    return x

def 判断是否体力不足刷差分():
    if 基础判断(1307,511, 1419,531, 'Tili_Enough'): return True
def 判断双倍是否体力不足刷差分():
    隧洞双倍纵差 = 330-289
    双倍纵差 = 376 - 341 #数据是之前截的,得等下一次双倍才知道1080p的纵差
    if 基础判断(1307,511+双倍纵差, 1419,531+双倍纵差, 'Tili_Enough'): return True

def Chafen_routine():
    星标_搜索窗口.聚焦窗口(hwnd)
    if 判断大世界()!=1:
        print("不在大世界, 请在大世界启动")
    else:
        time.sleep(0.1)
        keyboard_controller.press(Key.f4)
        time.sleep(0.1)
        keyboard_controller.release(Key.f4)
        time.sleep(1)
        Click2(485,215)#生存索引
        time.sleep(0.5)
        Click2(470,340)#饰品提取
        time.sleep(0.5)
        if 判断是否体力不足刷差分():
            print('体力不足进行遗器提取')
            keyboard_controller.press(Key.esc)
            keyboard_controller.release(Key.esc)
            return
        else:
            Click2(1560,525)#饥肠传送
        if 判断双倍是否体力不足刷差分():
            print('体力不足进行遗器提取')
            keyboard_controller.press(Key.esc)
            keyboard_controller.release(Key.esc)
            return
        else:
            双倍纵差 = 376 - 341
            Click2(1560,525+双倍纵差)  # 饥肠
        time.sleep(4 )
        Click2(1040,820)#支援
        time.sleep(1)
        Click2(370,235)#65希儿
        time.sleep(0.5)
        Click2(1580,975)#开始
        time.sleep(7)
        keyboard_controller.press('w')
        time.sleep(3)
        keyboard_controller.release('w')
        time.sleep(0.1)
        mouse_controller.click(Button.left)
        while True:
            time.sleep(3)
            if 判断是否战斗结束()!=1:
                pass
            else:
                if 判断是否可以再打一局():
                    Click2(1230, 945)#再来一局
                else:
                    break
        print("已刷干差分遗器")
        if 判断是否战斗结束()!=1:
            pass
        else:
            Click2(700,952)  # 退出关卡
def 领取日活奖励():
    if 判断大世界():
        星标_搜索窗口.聚焦窗口(hwnd)
        keyboard_controller.press(Key.f4)
        time.sleep(0.1)
        keyboard_controller.release(Key.f4)
        time.sleep(1)
        Click2(360,210)#每日实训
        time.sleep(0.5)

        for i in range(判断日活单项可以领取几次()):
            Click2(435, 825)  # 第一项日活领取
            time.sleep(0.5)

        Click2(1610, 310)  # 500位置领取总日活
        time.sleep(1)
        Click2(1920/2,1080/2)#点击继续
        time.sleep(1)
        if 判断日活是否领完()!=1:
            print("日活异常")
        else: print("日活500领取完成")
        time.sleep(1)
        keyboard_controller.press(Key.esc)
        keyboard_controller.release(Key.esc)
        time.sleep(3)
    else:
        print("操作异常")
def 分解四星和弃置():
    星标_搜索窗口.聚焦窗口(hwnd)
    if 判断大世界():
        keyboard_controller.press('b')
        time.sleep(0.1)
        keyboard_controller.release('b')
        time.sleep(2)
        Click2(785,65)#遗器
        time.sleep(0.5)
        Click2(1260,985)#分解
        time.sleep(1)
        Click2(1035,985)#快速选择
        time.sleep(0.5)
        Click2(700,430)#全选已弃置
        time.sleep(0.5)
        Click2(860,620)#4星及以下
        time.sleep(0.5)
        Click2(1185,755)#确认
        time.sleep(0.5)
        Click2(1670,985)#分解
        time.sleep(0.5)
        Click2(1175,825)#确认分解
        time.sleep(0.5)
        Click2(970, 690)#点击空白处
        time.sleep(0.5)
        print('分解遗器已完成.')
        keyboard_controller.press(Key.esc)
        keyboard_controller.release(Key.esc)
        time.sleep(1)
        keyboard_controller.press(Key.esc)
        keyboard_controller.release(Key.esc)
        return
    print('不在大世界')
#v0.0.2新增
from 星标_打开程序 import start_program
def 星铁启动():
    Game_Path = r'E:\Star Rail\Game\StarRail.exe'
    start_program(Game_Path)
def 启动后进入游戏并点击月卡(hwnd):
    #需要先启动
    星标_搜索窗口.聚焦窗口(hwnd)
    while 判断大世界()is None:
        Click2(300,300)
        time.sleep(2)

if __name__ == "__main__":
    exe_name = "StarRail.exe"
    窗口尺寸 = (1920, 1080)
    keyboard_controller = Controller()
    mouse_controller = MouseController()
    game_started = False
    while 星标_搜索窗口.get_window_hwnd_by_exename(exe_name) is None:
        if game_started is False:
            星铁启动()
            game_started = True
            time.sleep(5)
    hwnd = 星标_搜索窗口.get_window_hwnd_by_exename(exe_name)
    星标_搜索窗口.聚焦窗口(hwnd)
    启动后进入游戏并点击月卡(hwnd)
    time.sleep(1)
    Chafen_routine()
    time.sleep(5)
    领取日活奖励()
    time.sleep(1)
    分解四星和弃置()
    time.sleep(1)
    print('已完成')

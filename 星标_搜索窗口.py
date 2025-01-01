import psutil
import win32gui
import win32process
import win32con

def get_window_hwnd_by_exename(exe_name):
    def find_process_by_name(exe_name):
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == exe_name:
                return proc.info['pid']
        return None

    def find_window_by_pid(pid):
        def enum_window_titles(hwnd, result):
            if win32gui.IsWindowVisible(hwnd):
                _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
                if found_pid == pid:
                    result.append(hwnd)

        windows = []
        win32gui.EnumWindows(enum_window_titles, windows)
        return windows[0] if windows else None

    pid = find_process_by_name(exe_name)
    if pid:
        hwnd = find_window_by_pid(pid)
        return hwnd
    else:
        return None

def 聚焦窗口(hwnd):
    import time
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.1)

if __name__ == '__main__':
    # 示例调用
    exe_name = "cloudmusic.exe"
    hwnd = get_window_hwnd_by_exename(exe_name)
    win32gui.SetForegroundWindow(hwnd)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
import win32clipboard
import time

while True:
    win32clipboard.OpenClipboard()
    try:
        data = win32clipboard.GetClipboardData()
    except TypeError:
        data = "Non-text data in clipboard"
    finally:
        win32clipboard.CloseClipboard()
        
    with open('cliplog.txt', 'a+') as f:
        f.write(data + '\n')
        
    time.sleep(5)

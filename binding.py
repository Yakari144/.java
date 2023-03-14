#!/usr/bin/env python3
import os
import sys
import termios
import tty

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True:
    key = ord(getch())
    print(key)
    if key == 27: # Esc key
        break
    else:
        ## discover key code
        #pass
        ## any
        #os.system("echo Não é esta tecla, tenta outra vez!")
        ## for mac
        #os.system("open https://pornhub.com/")
        ## for linux
        #os.system("xdg-open https://pornhub.com/")
        pass
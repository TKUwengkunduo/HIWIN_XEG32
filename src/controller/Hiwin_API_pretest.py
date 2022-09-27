import pyrealsense2 as rs           # 版本目前不支援python3.10
from calendar import c
from operator import mod
import numpy as np
from ctypes import *
import time
import rospy
import pyrealsense2 as rs           # 版本目前不支援python3.10
import cv2


so_file = "/home/weng/HIWIN_XEG32/libmodbus/src/controller_0922/Hiwin_API.so"
modbus = CDLL(so_file)


'''
    move
    功能 : 絕對位置移動模式
    參數 : 
        dis = 位置(0~3200)
        speed = 速度(0~4800)
        flag = 旗標?(待確定)
'''
def move(dis=0, speed=1200, flag=1):
    state = 1
    modbus.move(dis, speed, flag)
    time.sleep(0.01)
    while state!='2':
        state = str(modbus.read_mode())
    print("end move")
    



if __name__ == "__main__":

    modbus.libModbus_Connect(1)

    while True:
        mode = input("(1=reset, 2=close, 3=open): ")
        if mode == '1':
            modbus.reset()
            time.sleep(25)      # 等待reset時間
        elif mode == '2':
            move(100,4800,1)      # 絕對位置移動 (0~3200)
        elif mode == '3':
            move(3200,4800,1)      # 絕對位置移動 (0~3200)
        else:
            pass


modbus.Modbus_Close()

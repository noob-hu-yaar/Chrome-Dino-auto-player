# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:43:58 2020

@author: HP
"""



import pyautogui
from PIL import Image,ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    
def isCollide(data):
    # bird
    for i in range(250,298):
            for j in range(410,561):
                if data[i,j] < 100: # kala mila
                    hit("down")
                    return True
    
    for i in range(300,415): #tree
            for j in range(561,650):
                if data[i,j] < 100: # kala mila
                    hit("up")
                    return True          
    return False
                    
    

'''def ss_lelo():
    image = ImageGrab.grab().convert('L')
    image.show()
 '''
   
if __name__ == "__main__":
    time.sleep(2)
    hit('up')
    
    while True:
        image = image = ImageGrab.grab().convert('L')
        data = image.load()
        
        '''if isCollide(data):
            hit("up")'''
        isCollide(data)
        
        '''for i in range(300,415):
            for j in range(600,650):
                data[i,j] = 0'''
                
        ''' 0 = tree
            100+ any = bird'''
    
    

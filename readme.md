#### 181228
### 酷跑游戏开发 过程及说明
#### Pygame模块之pygame.draw
pygame.draw.rect： 　　 绘制矩形
pygame.draw.polygon：  绘制任意边数的多边形
pygame.draw.circle：　　绘制圆
pygame.draw.ellipse：　 在矩形内绘制椭圆
pygame.draw.arc：　　   绘制圆弧（或者椭圆的一部分）
pygame.draw.line： 　　 绘制直线（线段）
pygame.draw.lines：　　从一个点列表中连续绘制直线段
pygame.draw.aaline：　 绘制一根平滑的线（反锯齿）
pygame.draw.aalines：  绘制一系列平滑的线

----
pygame绘制屏幕保持不闪退的代码
import pygame
import sys
from pygame.locals import *

pygame.init() # 初始化 
screen = pygame.display.set_mode((500,700),0,32) # 绘制屏幕大小，三个参数第一个是分辨率，第二个是标志位，第三个为色深，后面两个参数可以省略。可以写成set_mode（（600,500））

pygame.display.set_caption("hello,world!") # 屏幕左上角的窗口标题
"""下面的循环用于使用pycharm运行程序时不闪退，event=pygame.event.wait()    #等待事件发生，获得事件的名称"""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
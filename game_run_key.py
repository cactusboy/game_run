import sys, random, time, pygame
from pygame.locals import *
# random() 方法返回随机生成的一个实数，它在[0,1)范围内。

def print_text(font, x, y, text, color=(255, 255, 255)):

    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


# 主程序
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Keyboard Demo")
# font1 = pygame.font.Font(None, 24)
font1 = pygame.font.SysFont("C:\Windows\Fonts\simfang.ttf",24)
font2 = pygame.font.Font(None, 200)
white = 255, 255, 255
yellow = 255, 255, 0
color = 125, 100, 210

key_flag = False
correct_answer = 97
seconds = 10
score = 0
clock_start = 0
game_over = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            key_flag = True
        elif event.type == KEYUP:
            key_flag = False
# 跟踪按键
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    if keys[K_RETURN]:
        if game_over:
            game_over = False
            score = 0
            seconds = 11
            """
            # clock_start = time.clock() # Python time clock() 函数以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
            # python3.3版后推荐用time.perf_counter() 来测量执行时间
            # current = time.clock() - clock_start
            """
            clock_start = time.perf_counter()
    current = time.perf_counter() - clock_start
    speed = score * 6
    if seconds - current < 0:
        game_over = True
    elif current <= 10:
        if keys[correct_answer]:
            correct_answer = random.randint(97, 122) # Random.randint(x,y);看名字知道这个函数的作用了，它可以返回一个x~y之间的随机数。
            score += 1

    # 清屏
    screen.fill(color)

    print_text(font1, 0, 20, "继续10秒练习...")

    if key_flag:
        print_text(font1, 450, 0, "you are keying...")

    if not game_over:
        print_text(font1, 0, 80, "Time: " + str(int(seconds - current)))

    print_text(font1, 0, 100, "Speed: " + str(speed) + " letters/min")

    if game_over:
        print_text(font1, 0, 160, "Press Enter to start...")

    print_text(font2, 0, 240, chr(correct_answer - 32), yellow)

    # 更新
    pygame.display.update()
import pygame
import sys
import time
import random
import threading
import datetime

pygame.init()

intent = 10    #press-times
nght_colour = (0, 0, 0)
dy_colour = (255, 255, 255)
screen = pygame.display.set_mode((205, 205))
stats = f"Press {intent} times to open the egg. Press start (or any key)."
running = True


class Animate():
    def __init__(self):
        self.sprites, self.finish = []
        #self.mood = 'none'
    def run(self):
        self.value = 0
        while self.value <= len(self.sprites):
            press = self.sprites[int(self.value)]
            self.value += self.time
            if (self.dayOrNight()):
                self.mood = '_'
            sprite = pygame.image.load(f'assets/{press}')
            _rect = sprite.get_rect()
            screen.blit(sprite, _rect)
            pygame.display.update()
    def close(self):
        self.value = 0
        while self.value <= len(self.finish):
            ######  HOUR  ##########
            if (self.value > 19):
                self.time = -self.time
            if (self.value < 3):
                self.time = 0.01

            self.value += self.time
            press = self.finish[int(self.value)]
            sprite = pygame.image.load(f'assets/{press}')
            _rect = sprite.get_rect()
            screen.blit(sprite, _rect)
            pygame.display.update()



class Frame(Animate):
    def __init__(self):
        self.sprites = ["frame0.jpg", "frame1.jpg", "frame2.jpg", "frame3.jpg", "frame4.jpg",]
        self.finish = []
        self.time = 0.01
        self.delay = 0.0
        self.value = 0
        #self.date = datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S')
        self.hour = datetime.datetime.now().strftime('%H')

    def __str__(self):
        print(f"Your open the egg on {self.delay}")

    def init_finish(self):
        n = 0
        while n < 20:
            self.finish.append(f'end{str(n)}.jpg')
            n+=1

    def dayOrNight(self):
        if (int(self.hour)>=18):
            return False
            #print('night')
        else:
            return True

frm = Frame()
frm.init_finish()
start_time = 0
print(stats)

if (frm.dayOrNight()):
    screen.fill(nght_colour)
else:
    screen.fill(dy_colour)

# game loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if (intent >= 0):
                frm.run()
                intent -= 1
                if (intent==9):
                    start_time = time.time()

            else:
                if(intent == -1):
                    intent -= 1
                    end_time = time.time()
                    rcrd = end_time - start_time
                    frm.close()
                print(f'Your record is the {rcrd}')

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False



















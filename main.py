
####################
import pygame
import pytz
####################
import sys
import time
import datetime
import random

pygame.init()
thrw_ball = 0    #press-times
default_colour = (0, 0, 0)
screen = pygame.display.set_mode((210, 303))
statement = f"Press a key when Pikachu blink to win. Press enter to start."
running = True

class Animate():
    def __init__(self):
        self.sprites = []
    def run(self, cheat):
        self.value = 0
        while self.value <= len(self.sprites):
            press = self.sprites[int(self.value)]
            ######  LOOP  #######
            if (self.value < 0.17):
                self.time = self._frame_time
            elif (self.value < 0.2 and self.time < 0):
                break
            ######  FAKE OR NOT  #######
            if (self.value > cheat):
                self.time = -self.time
            self.value += self.time
            screen.fill(default_colour)
            sprite = pygame.image.load(f'assets/{press}')
            _rect = sprite.get_rect()
            screen.blit(sprite, _rect)
            pygame.display.update()



class Frame(Animate):
    def __init__(self):
        self.sprites = ["frame0.gif", "frame1.gif", "frame2.gif", "frame3.gif"]
        self.time = 0
        self._frame_time = 0.00284
        self.value = 0
        self.here = datetime.datetime.now().strftime('%d/%m/%y %H:%M')
        self.japan = datetime.datetime.now(tz=pytz.timezone('Asia/Tokyo')).strftime('%d/%m/%y %H:%M')  # for Japan time zone

    def __str__(self, intent):
        print(f"Your record is the {intent}")

    def init_blink(self):
        if(self.value >= 3):
            return True
        else:
            return False

    def JapanMood(self):
        if (self.here == self.japan):
            return True
        else:
            return False

print(statement)
screen.fill(default_colour)
captured = 0
frm = Frame()
while running:
    # for .... queue
    rcrd = time.process_time()
    screen.fill(default_colour)
    sprite = pygame.image.load(f'assets/frame0.gif')
    _rect = sprite.get_rect()
    screen.blit(sprite, _rect)
    pygame.display.update()
    if (int(rcrd) % 2):
        if (random.randint(0, 6) == 4):
            frm.run(3.9)
            if (captured < 0):
                mood = frm.JapanMood()
                if(mood):
                    print('トドスのキャプチャ')
                print("Pikachu was added to the pokedex!!!")
            print(f'Your intents to capture the pokemon: {thrw_ball}')
            break
        else:
            frm.run(2.9)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            thrw_ball += 1
            if (frm.init_blink()):
                captured -= 1




















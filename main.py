import random
import time

import pygame
from pygame.locals import (
    MOUSEBUTTONDOWN,
    K_r,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([1000, 500])
        self.screen.fill((0, 0, 0))
        pygame.display.flip()
        self.tab1 = [[0] * 100 for i in range(100)]
        self.tab2 = [[0] * 100 for i in range(100)]
        for x in range(100):
            for y in range(50):
                # if x==10 and (y==10 or y==11 or y==12):
                if random.randint(0, 10) == 5:
                    stan = 1
                else:
                    stan = 0
                byte = Byte(self, x, y, stan)
                self.tab1[x][y] = byte

    def run(self):
        running = True
        while running:
            for x in range(100):
                for y in range(50):
                    sum = 0
                    if x > 0:
                        sum += self.tab1[x - 1][y].stan
                    if x < 99:
                        sum += self.tab1[x + 1][y].stan
                    if y > 0:
                        sum += self.tab1[x][y - 1].stan
                    if y < 49:
                        sum += self.tab1[x][y + 1].stan
                    if x > 0 and y > 0:
                        sum += self.tab1[x - 1][y - 1].stan
                    if x > 0 and y < 49:
                        sum += self.tab1[x - 1][y + 1].stan
                    if x < 99 and y > 0:
                        sum += self.tab1[x + 1][y - 1].stan
                    if x < 99 and y < 49:
                        sum += self.tab1[x + 1][y + 1].stan
                    if self.tab1[x][y].stan == 0 and sum == 3:
                        self.tab2[x][y] = 1
                    elif self.tab1[x][y].stan == 1 and (sum == 2 or sum == 3):
                        self.tab2[x][y] = 1
                    else:
                        self.tab2[x][y] = 0
            for x in range(100):
                for y in range(50):
                    self.tab1[x][y].stan = self.tab2[x][y]
                    self.tab1[x][y].update()

            pygame.display.flip()
            time.sleep(0.5)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_r:
                        for x in range(100):
                            for y in range(50):
                                if random.randint(0, 10) == 5:
                                    self.tab1[x][y].stan = 1
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x = int(x / 10)
                    y = int(y / 10)
                    if self.tab1[x][y].stan == 1:
                        self.tab1[x][y].stan = 0
                    else:
                        self.tab1[x][y].stan = 1
                elif event.type == QUIT:
                    running = False


class Byte:
    def __init__(self, game, x, y, stan):
        self.game = game
        self.stan = stan
        self.x = x
        self.y = y


    def update(self):
        surf = pygame.Surface((10, 10))
        if self.stan == 1:
            surf.fill((0, 0, 255))
        else:
            surf.fill((0, 0, 0))
        self.game.screen.blit(surf, (self.x * 10, self.y * 10))


if __name__ == '__main__':
    game = Game()
    game.run()

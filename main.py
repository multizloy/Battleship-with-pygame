import pygame
import random
from settings import *

pygame.init()

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Battleship")

fontSize = int(blockSize // 1.5)

font = pygame.font.SysFont("notosans", fontSize)


def main():
    gameOver = False
    screen.fill(WHITE)
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

        pygame.display.update()


main()
pygame.quit()

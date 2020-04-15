import random
import pygame
import time
import sys
from pygame.locals import *

#pygame.init()

WIDTH = 600
HEIGHT = 400


class CGame:
    def __init__(self):
        self.BIG_SURF = pygame.display.set_mode((WIDTH, HEIGHT))
        self.board = CBoard(self.BIG_SURF)
        self.lock = pygame.time.Clock()


class CBoard:
    def __init__(self, surface):


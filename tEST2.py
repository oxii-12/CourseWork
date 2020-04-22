import pygame
import sys
import random
from pygame.locals import *

WIDTH   = 455
HEIGHT  = 455
DISPLAY_SURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tests :)")
font = pygame.font.Font("KOMIKAX_.ttf", 32)

class Node:
    def __init__(self, coord, flammable, colour, burnSpeed):
        self.coord = (0,0)
        self.flammable = True
        self.colour = (0, 150, 0)
        self.burnSpeed = 5


class Tree:
    pass

class Screen:
    def __init__(self, surface):
        pass

class Game:
    def __init__(self):
        self.DISPLAY_SURF = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = False

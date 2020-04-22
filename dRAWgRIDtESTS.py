import pygame
import sys
import random
from pygame.locals import *

pygame.init()

### SCREEN SET UP
WIDTH   = 455
HEIGHT  = 455
DISPLAY_SURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tests :)")
font = pygame.font.Font("KOMIKAX_.ttf", 32)
# TODO: Set window icon

DEFAULT_COLOUR      = (0, 150, 0)
HIGHLIGHT_COLOUR    = (255, 50, 0)

def mouse_pos():
    return pygame.mouse.get_pos()

def draw_grid():
    for x in range(0, 380, 5):
        pygame.draw.line(DISPLAY_SURF, (150, 150, 150), (x, 0), (x, 100), 1)

def draw_squares():
    for y in range(75):
        for x in range(75):
            if mouse_pos()[0] in range(x*5, (x+1)*5) and mouse_pos()[1] in range(y*5, (y+1)*5):
                colour = HIGHLIGHT_COLOUR
            else:
                colour = DEFAULT_COLOUR
            pygame.draw.rect(DISPLAY_SURF, colour, (x*5, y*5, 5, 5))


# def draw_squares():
#     for y in range(75):
#         for x in range(75):
#             if mouse_pos()[0] in range(x*5, (x+1)*5) and mouse_pos()[1] in range(y*5, (y+1)*5):
#                 colour = HIGHLIGHT_COLOUR
#             else:
#                 colour = DEFAULT_COLOUR
#             pygame.draw.rect(DISPLAY_SURF, colour, (x*5, y*5, 5, 5))
# DEFAULT_COLOUR      = (0, 200, 0)
# HIGHLIGHT_COLOUR    = (255, 50, 0)
# def draw_squares():
#     for y in range(75):
#         for x in range(75):
#             if mouse_pos()[0] in range(1+x*6, 6+x*6) and mouse_pos()[1] in range(1+y*6, 6+y*6):
#                 colour = HIGHLIGHT_COLOUR
#             else:
#                 colour = DEFAULT_COLOUR
#             pygame.draw.rect(DISPLAY_SURF, colour, (1+x*6, 1+y*6, 5, 5))
# def draw_squares():
#     for y in range(3):
#         for x in range(3):
#             if mouse_pos()[0] in range(5+x*150, 155+x*150) and mouse_pos()[1] in range(5+y*150, 155+y*150):
#                 colour = HIGHLIGHT_COLOUR
#             else:
#                 colour = DEFAULT_COLOUR
#             pygame.draw.rect(DISPLAY_SURF, colour, (5+x*150, 5+y*150, 145, 145))
# start with draw a square at 0,0.
# sizing, plan 3x3 so 900 is nice but then too big, decided on 150.
# drew nine squares, was just block tho so made space between, then there was space between them and
# right edge but not the left so made whole window bigger and started squares off 5 later for even
# spacing. then add highlight func. Didn't know, then thought in loop for each square just before
# draw. Then use variable for colour, defined as constants. STarted with just x column and it did
# all to the left of the mouse (just >) then made into a range. Easy to make just one square by
# adding the same thing for the y.
# Interested in simplifying the 5+x*150 but rn is functional so good for now
# Move to smaller squares. try 50,, need to actually make more squares and change the ranges for
# highlighting, try take out this 150 and now 50 so I can change squares easier, take out as
# 'dimensions'. Try make the spacing relative to number of squares. liked 5 for 150 which is a
# 30th, thats rough as a decimal (recurring), so I'll try a 20th.
# Dropped above, got abit confusing getting fracations from grid I'd made and decided to first
# eyeball a grid more like the one i'd actually use. Where it switches to highlighting the next
# square, trying to get middle was squareSize + 1.5 spaceSize. Thinking about how all squares
# and spaces would preferably add up to the tot window size (all even/ regular(, ++ as you can't
# have floats so smallest you can go anyway is 1, which is quite big when you want squares of
# around 5.  THEREFORE/ ANYWAY, this probably wasn't the best way/ what I had in mind. You'd
# be able to tell of the squares roughly by the square edges evident where neighbouring squares
# changed colour, may have added grid to help, but it would just be lines OVER nodes edges
# roughly, blitted on after theyre drawn so you don't have to worry about highlight going over
# the line.
# Made it no gaps and highlight. Grid looked ugly, lines still had to be '1' thick. Try see how
# it looks with just different colours thrown in, ye it'll probably be fine with no grid :)
# Looking at this smaller one though, I probably would want it rectangular.


running = True

while running:
    DISPLAY_SURF.fill((100, 100, 100))
    draw_squares()
    draw_grid()
    pygame.draw.rect(DISPLAY_SURF, (255, 255, 255), (100, 75, 15, 5)) #white box, test how draw/ dimensions work
    Button = pygame.draw.rect(DISPLAY_SURF, (0,0,0), (100, 200, 50   , 200))
    DISPLAY_SURF.blit(pygame.image.load("TestImage.png"), (0, 100))

    pygame.display.update()                       #  (x  , y  , width, height)


    for event in pygame.event.get(): # All events get added to the event queue, .event.get() gets the top event of the queue
        #   QUIT, top right button
        if event.type == QUIT:                  # If its a quit command
            running = False
        if event.type == MOUSEBUTTONUP:
            if Button.collidepoint(mouse_pos()):
                print("hey presto")

pygame.quit()

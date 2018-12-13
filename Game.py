import pygame
import sys
import cv2
import numpy as np

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
pygame.display.set_caption("Pro Boxer 5")
win = pygame.display.set_mode((1920,960))

player_x = 100
player_y = 660
width = 125
height = 300

bag_x = 1750
bag_y = 660

isJump = False
jumpCount = 10

isPunch = False
punchCount = 10

#Music
pygame.mixer.music.load("Music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

run = True

while run:

    pygame.time.delay(10)
    
    #Break Condtion
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #Refresh Background
    win.fill((0))
    
    #Movement for rectangle
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and player_x + width < bag_x:
        player_x += 5
    if keys[pygame.K_LEFT]:
        player_x -= 5 

    if not isPunch:
        if keys[pygame.K_UP]:
            isPunch = True
    else:
        if punchCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            armLength = (punchCount ** 2) * 3 * neg
            punchCount -= 1
            pygame.draw.rect(win,(255,0,0),(player_x + width, player_y + 100, armLength, 50))
        else:
            isPunch = False
            punchCount = 10

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            player_y -= (jumpCount ** 2) * 0.7 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    
    pygame.draw.rect(win,(0,255,0),(bag_x,bag_y,width,height))
    pygame.draw.rect(win,(255,0,0),(player_x,player_y,width,height))
    pygame.display.update()

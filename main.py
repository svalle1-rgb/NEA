from blob import Blob

import pygame
pygame.init()

screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("Natural Selection Simulator")
clock = pygame.time.Clock()
blob1 = Blob(450,300,2,50,100,1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill((30,30,30))
blob1.draw(screen)

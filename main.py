import pygame

class Blob():
    def __init__(self, x, y, speed, vision, energy, metabolism):
        self.x = x
        self.y = y
        self.speed = speed
        self.vision = vision
        self.energy = energy
        self.metabolism = metabolism

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (0,200,100),
            (int(self.x), int(self.y)),
            10
        )

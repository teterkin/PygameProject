import sys
import pygame


class Cup(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        img = pygame.image.load('coffee_cup.png').convert()
        self.image = img

        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10


pygame.init()
screen = pygame.display.set_mode((960,720))

cup = Cup()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
    screen.blit(cup.image, cup.rect)

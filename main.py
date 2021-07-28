import pygame
import os
import sys


# Functions

def game_quit():
    print("Bye!")
    pygame.quit()
    try:
        sys.exit()
    finally:
        global running
        running = False


# Objects

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.moving_along_x = 0
        self.moving_along_y = 0
        self.current_frame = 0
        self.images = []
        for index in range(1, 5):
            image_file = pygame.image.load(os.path.join('images', 'hero' + str(index) + '.png')).convert()
            image_file.convert_alpha()
            image_file.set_colorkey(ALPHA)
            self.images.append(image_file)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control_player_movement(self, x, y):
        self.moving_along_x += x
        self.moving_along_y += y

    def update_position_and_frame(self):
        # Sprite sprite position
        self.rect.x = self.rect.x + self.moving_along_x
        self.rect.y = self.rect.y + self.moving_along_y

        # Updating sprite frame

        # Moving left
        if self.moving_along_x < 0:
            self.current_frame += 1
            if self.current_frame > 3 * animation_cycles:
                self.current_frame = 0
            self.image = pygame.transform.flip(self.images[self.current_frame // animation_cycles], True, False)

        # Moving Right
        if self.moving_along_x > 0:
            self.current_frame += 1
            if self.current_frame > 3 * animation_cycles:
                self.current_frame = 0
            self.image = self.images[self.current_frame // animation_cycles]

# Variables

world_size_x = 960
world_size_y = 720

frame_rate = 40
animation_cycles = 4

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

running = True

# Setup

clock = pygame.time.Clock()

pygame.init()

world = pygame.display.set_mode([world_size_x, world_size_y])

background_image = pygame.image.load(os.path.join('images', 'stage.png'))
background_box = world.get_rect()

player = Player()
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
pixels_to_move = 10

# Main loop

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_quit()

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                game_quit()
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control_player_movement(-pixels_to_move, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control_player_movement(pixels_to_move, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print("Jump")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control_player_movement(pixels_to_move, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control_player_movement(-pixels_to_move, 0)

    world.blit(background_image, background_box)
    player.update_position_and_frame()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(frame_rate)

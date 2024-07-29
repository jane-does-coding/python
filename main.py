import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Mario Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


mario_image = pygame.image.load("mario.png")
mario_rect = mario_image.get_rect()
mario_rect.topleft = (50, 500)


platform = pygame.Rect(0, 550, 800, 50)


gravity = 0.5
mario_speed_y = 0
jump_speed = -10
on_ground = True


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        mario_rect.x += 5
    if keys[pygame.K_SPACE] and on_ground:
        mario_speed_y = jump_speed
        on_ground = False


    mario_speed_y += gravity
    mario_rect.y += mario_speed_y


    if mario_rect.colliderect(platform):
        mario_rect.bottom = platform.top
        mario_speed_y = 0
        on_ground = True


    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, platform)
    screen.blit(mario_image, mario_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()

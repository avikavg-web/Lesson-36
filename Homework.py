import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Custom Event Color Change")

COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_CHANGE_EVENT, 2000)

white = (255, 255, 255)
player_color = [0, 100, 255]
static_color = [255, 50, 50]

player_rect = pygame.Rect(100, 100, 50, 50)
player_speed = 5
static_rect = pygame.Rect(400, 300, 60, 60)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == COLOR_CHANGE_EVENT:
            player_color = [random.randint(0, 255) for _ in range(3)]
            static_color = [random.randint(0, 255) for _ in range(3)]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < SCREEN_WIDTH:
        player_rect.x += player_speed
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN] and player_rect.bottom < SCREEN_HEIGHT:
        player_rect.y += player_speed

    screen.fill(white)

    pygame.draw.rect(screen, player_color, player_rect)
    pygame.draw.rect(screen, static_color, static_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
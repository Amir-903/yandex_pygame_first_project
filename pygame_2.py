import pygame
import sys  # system
import random

WIDTH = 800
HEIGHT = 600
Display = pygame.display.set_mode((WIDTH, HEIGHT))

BG_COLOR = (19, 111, 123)
HERO_COLOR = (22, 93, 19)
BALL_COLOR = (5, 10, 193)
ENEMY_COLOR = (10, 210, 255)

SIZE_X = 100
SIZE_Y = 25
SIZE_BALL = 30

FPS = 60
FpsClock = pygame.time.Clock()


def finish():
    pygame.quit()
    sys.exit(0)


def game():
    # Тут будет создание игровых объектов
    hero = pygame.Rect(WIDTH / 2 - SIZE_X / 2, HEIGHT - 40 - SIZE_Y, SIZE_X, SIZE_Y)
    enemy = pygame.Rect(WIDTH / 2 - SIZE_X / 2, 40 - SIZE_Y, SIZE_X, SIZE_Y)
    ball = pygame.Rect(WIDTH / 2 - SIZE_BALL / 2, HEIGHT / 2, SIZE_BALL, SIZE_BALL)
    while True:  # А ложь - False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            enemy.move_ip(-1, 0)
        if keys[pygame.K_RIGHT]:
            enemy.move_ip(5, 0)

        Display.fill(BG_COLOR)
        # Прорисовка
        pygame.draw.rect(Display, HERO_COLOR, hero)
        pygame.draw.rect(Display, ENEMY_COLOR, enemy)
        pygame.draw.rect(Display, BALL_COLOR, ball)

        pygame.display.update()
        FpsClock.tick(FPS)


if name == "main":
    game()

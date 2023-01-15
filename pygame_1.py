import pygame
import sys
import random
import time

pygame.font.init()
fontScore = pygame.font.Font('scootchover-sans.ttf', 24)
startTime = time.time()

W = 800  # WIDTH
H = 600  # HEIGHT
Display = pygame.display.set_mode((W, H))
pygame.display.set_caption("Игра змейка")
pygame.mouse.set_visible(False)

target = pygame.image.load("star.png")
targetPos = target.get_rect()
targetPos.centerx = random.randint(32, W - 32)
targetPos.centery = random.randint(32, H - 32)

LINE_COLOR = (0, 0, 0)
BG_COLOR = (145, 66, 243)


def finish():
    pygame.quit()
    sys.exit(0)


x = 0
y = 0

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish()
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                score -= 1
                bullet = pygame.Rect(x, y, 1, 1)
                if bullet.colliderect(targetPos):
                    targetPos.centerx = random.randint(32, W - 32)
                    targetPos.centery = random.randint(32, H - 32)
                    score += 2

    if time.time() - startTime > 60:
        print("Score: " + str(score))
        finish()

    Display.fill(BG_COLOR)
    Display.blit(target, targetPos)
    scoreText = fontScore.render("Score: " + str(score), 1, LINE_COLOR)
    Display.blit(scoreText, (0, 0))
    pygame.draw.line(Display, LINE_COLOR, (0, y), (W, y))
    pygame.draw.line(Display, LINE_COLOR, (x, H), (x, 0))
    pygame.display.update()

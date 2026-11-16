import pygame
import random
from settings import *

class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 40, 40)
        self.speed = PLAYER_SPEED
        self.health = INITIAL_HEALTH
        self.score = 0

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)


class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(100, 100, 45, 45)
        self.dx = ENEMY_SPEED
        self.dy = ENEMY_SPEED

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Αναπήδηση στα όρια της οθόνης
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.dx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)


class Coin:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 25, 25)
        self.respawn()

    def respawn(self):
        self.rect.x = random.randint(30, WIDTH - 55)
        self.rect.y = random.randint(30, HEIGHT - 55)

    def draw(self, screen):
        pygame.draw.ellipse(screen, GOLD, self.rect)

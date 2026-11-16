import pygame
import sys
from settings import *
from sprites import Player, Enemy, Coin

def draw_text(screen, text, size, color, x, y):
    font = pygame.font.SysFont("arial", size, bold=True)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Coin Collector - Εργασία Python")
    clock = pygame.time.Clock()

    player = Player()
    enemy = Enemy()
    coin = Coin()

    game_over = False
    win = False

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not game_over:
            keys = pygame.key.get_pressed()
            player.move(keys)
            enemy.update()

            # Έλεγχος σύγκρουσης με νόμισμα
            if player.rect.colliderect(coin.rect):
                player.score += 10
                coin.respawn()
                if player.score >= WIN_SCORE:
                    win = True
                    game_over = True

            # Έλεγχος σύγκρουσης με εχθρό
            if player.rect.colliderect(enemy.rect):
                player.health -= 2
                if player.health <= 0:
                    player.health = 0
                    win = False
                    game_over = True

        # Σχεδίαση οθόνης
        screen.fill(BLACK)
        player.draw(screen)
        enemy.draw(screen)
        coin.draw(screen)

        # Εμφάνιση σκορ και ζωής
        draw_text(screen, f"Score: {player.score} / {WIN_SCORE}", 24, WHITE, 20, 15)
        draw_text(screen, f"Health: {player.health}%", 24, GREEN, WIDTH - 180, 15)

        if game_over:
            if win:
                draw_text(screen, "ΣΥΓΧΑΡΗΤΗΡΙΑ! ΚΕΡΔΙΣΕΣ!", 40, GOLD, WIDTH // 2 - 230, HEIGHT // 2 - 20)
            else:
                draw_text(screen, "GAME OVER! ΕΧΑΣΕΣ!", 40, RED, WIDTH // 2 - 190, HEIGHT // 2 - 20)

        pygame.display.flip()

if __name__ == "__main__":
    main()

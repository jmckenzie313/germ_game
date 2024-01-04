import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Germ")

BG = pygame.transform.scale(pygame.image.load("bg.png"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 25
PLAYER_HEIGHT = 25

SMALL_GERM_WIDTH = 25
SMALL_GERM_HEIGHT = 25

MED_GERM_WIDTH = 40
MED_GERM_HEIGHT = 40

LARGE_GERM_WIDTH = 60
LARGE_GERM_HEIGHT = 60

PLAYER_VEL = 5


def draw(player, enemy_1, enemy_2, enemy_3):
    WIN.blit(BG, (0, 0))

    pygame.draw.circle(WIN, (34, 139, 34), [player.x, player.y], PLAYER_WIDTH, PLAYER_HEIGHT)
    pygame.draw.circle(WIN, (124, 252, 0), [enemy_1.x, enemy_2.y], SMALL_GERM_WIDTH, SMALL_GERM_HEIGHT)
    pygame.draw.circle(WIN, (255, 165, 0), [enemy_2.x, enemy_2.y], MED_GERM_WIDTH, MED_GERM_HEIGHT)
    pygame.draw.circle(WIN, (148, 0, 211), [enemy_3.x, enemy_3.y], LARGE_GERM_WIDTH, LARGE_GERM_HEIGHT)

    pygame.display.update()


def enemyMove(enemy_1, enemy_2, enemy_3):
    enemies = [enemy_1, enemy_2, enemy_3]

    for enemy in enemies:
        direction = random.choice(['left', 'right', 'up', 'down'])

        if direction == "up":
            enemy.y -= 1
        elif direction == "down":
            enemy.y += 1
        elif direction == "left":
            enemy.x -= 1
        elif direction == "right":
            enemy.x += 1

            # Check if the enemy is off the screen
        if enemy.x < 0 or enemy.x > WIDTH or enemy.y < 0 or enemy.y > HEIGHT:
            # If the enemy is off the screen, reset its position
            enemy.x = random.randint(0, WIDTH)
            enemy.y = random.randint(0, HEIGHT)

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    enemy_1 = pygame.Rect(750, 900, SMALL_GERM_WIDTH, SMALL_GERM_HEIGHT)
    enemy_2 = pygame.Rect(500, 250, MED_GERM_WIDTH, MED_GERM_HEIGHT)
    enemy_3 = pygame.Rect(900, 50, LARGE_GERM_WIDTH, LARGE_GERM_HEIGHT)

    enemies = [enemy_1, enemy_2, enemy_3]

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        elif keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        elif keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        elif keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL


        enemyMove(enemy_1, enemy_2, enemy_3)

        draw(player, enemy_1, enemy_2, enemy_3)


        distance_x = player.x - enemy_1.x
        distance_y = player.y - enemy_1.y
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

        # Move the enemy toward the player
        speed = 2

        for enemy in enemies:

            if distance != 0:
                enemy.x += speed * distance_x / distance
                enemy.y += speed * distance_y / distance

    pygame.quit()


if __name__ == "__main__":
    main()
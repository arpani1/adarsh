import pygame
import sys

pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Overworld")

# Load assets
face = pygame.image.load("face.png").convert_alpha()
face = pygame.transform.scale(face, (64, 64))

grass = pygame.image.load("grass.png").convert()
grass = pygame.transform.scale(grass, (64, 64))

# Character position
player_pos = [WIDTH // 2, HEIGHT // 2]

clock = pygame.time.Clock()

def draw_background():
    for x in range(0, WIDTH, 64):
        for y in range(0, HEIGHT, 64):
            screen.blit(grass, (x, y))

def main():
    while True:
        screen.fill((0, 0, 0))
        draw_background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos[0] -= 5
        if keys[pygame.K_RIGHT]:
            player_pos[0] += 5
        if keys[pygame.K_UP]:
            player_pos[1] -= 5
        if keys[pygame.K_DOWN]:
            player_pos[1] += 5

        # Draw player
        screen.blit(face, player_pos)

        pygame.display.flip()
        clock.tick(60)

main()

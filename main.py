import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsans", 30, True)


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    score = 0
    high_score = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        current_score = font.render("Score: " + str(score), 1, (255,255,255))
        current_hscore = font.render("High Score: " + str(high_score), 1, (255,255,255))

        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                if score > high_score:
                    high_score = score
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    score += 1

        screen.fill('black')
        screen.blit(current_score, (390, 10))
        screen.blit(current_hscore, (1090, 10))

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        
        # limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
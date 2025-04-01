import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import *

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    p1 = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2 )
    asteroid_field = AsteroidField()
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        #frame rate
        dt = fps.tick(60) / 1000
if __name__ == "__main__":
    main()

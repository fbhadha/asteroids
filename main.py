import pygame
from constants import *
from player import *

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    p1 = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2 )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        p1.update(dt)
        p1.draw(screen)
        pygame.display.flip()

        #frame rate
        dt = fps.tick(60) / 1000
if __name__ == "__main__":
    main()

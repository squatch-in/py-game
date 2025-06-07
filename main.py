import pygame
from constants import *
from player import *
from circleshape import *


def main():
    pygame.init()
    clock = pygame.time.Clock()   
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0 
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    print(clock.get_fps())
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #pygame.font(clock.get_fps())


if __name__ == "__main__":
    main()
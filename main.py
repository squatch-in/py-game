import pygame
from constants import *



def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    
    print(clock.get_fps())
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60)
        #pygame.font(clock.get_fps())
if __name__ == "__main__":
    main()
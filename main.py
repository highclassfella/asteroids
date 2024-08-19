import pygame 
from constants import *




def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width: %4i" %(SCREEN_WIDTH))
    print("Screen height: %3i" %(SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while 1>0:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
           return
                   
      screen.fill((0, 0, 0))
      pygame.display.flip()



if __name__ == "__main__":
    main()





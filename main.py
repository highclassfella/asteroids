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


    asteroids_group = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots_group)
    Player.containers = (updatable, drawable) #muss VOR player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) kommen. warum?
    Asteroid.containers = (updatable, drawable, asteroids_group)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids_group:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()   
 
            for shot in shots_group:
                 if asteroid.collides_with(shot):
                     shot.kill()
                     asteroid.split()



        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()





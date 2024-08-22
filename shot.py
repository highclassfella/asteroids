# import pygame
# from constants import *
# from circleshape import CircleShape


# class Shot(CircleShape):
#     def __init__(self, x, y, rotation, radius):
#         super().__init__(x, y, radius)
#         self.position = pygame.Vector2(x, y)
#         self.radius = SHOT_RADIUS
#         self.velocity = pygame.Vector2(0, 1)
#         self.rotation = rotation


        

#     def draw(self, screen):
#         pygame.draw.circle(screen, "white", self.position, self.radius)

#     #def rotate(self, dt):
#      #   self.rotation += PLAYER_TURN_SPEED * dt    


#     def update(self, dt):
#         forward = pygame.Vector2(0, 1).rotate(self.rotation)
#         self.position += forward * PLAYER_SHOOT_SPEED * dt
        


import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
from random import randint
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image, bird_y):
        self.type = randint(0, 1)
        super().__init__(image, self.type, 'bird')
        if bird_y == 0:
            self.rect.y = 260
        else:
            self.rect.y = 315
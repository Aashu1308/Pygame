import pygame
import random
from pygame.locals import *


class Snowflake(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Snowflake, self).__init__()
        self.surface = pygame.image.load(
            "images/snowflake.png").convert_alpha()
        pygame.Surface.convert_alpha(self.surface)
        self.screen = screen

    def draw(self, coord):
        self.screen.blit(self.surface, coord)


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        self.image = pygame.image.load("images/mountain.jpg")
        self.rect = self.image.get_rect()
        self.location = [0, 0]
        self.rect.left, self.rect.top = self.location


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen.fill((255, 255, 255))

        self.background = Background()
        self.snowfall = {}

        for i in range(20):
            x = random.randrange(0, 400)
            y = random.randrange(0, 400)
            snowflake = Snowflake(screen)
            self.snowfall[snowflake] = [x, y]

        self.screen.blit(self.background.image, self.background.rect)

        self.clock = pygame.time.Clock()

    def update(self):
        for i in self.snowfall:
            f = self.snowfall[i]
            i.draw(f)
            f[1] += 1
            if f[1] >= 400:
                y = random.randrange(-50, -10)
                f[1] = y
                x = random.randrange(0, 400)
                f[0] = x

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE or event.key == K_ESCAPE or event.key == ord('q'):
                    raise SystemExit

    def run(self):
        while True:
            self.clock.tick(20)
            self.screen.blit(self.background.image, self.background.rect)
            self.update()
            self._handle_events()
            pygame.display.flip()


pygame.init()

display = pygame.display.set_mode((450, 278), pygame.RESIZABLE)
pygame.display.set_caption("Snowfall")
game = Game(display)

game.run()

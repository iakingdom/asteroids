import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    Player.containers = (updatable, drawable)
    player = Player(x,y)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    field = AsteroidField()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for rock in asteroids:
            if (rock.collides_with(player)):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for rock in asteroids:
            for shot in shots:
                if (rock.collides_with(shot)):
                    rock.split(field)
                    shot.kill()
                    #log_event("asteroid_shot")
        for drawn in drawable:
            drawn.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()

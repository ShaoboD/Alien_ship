import sys
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Setting()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # build the ship   
    ship = Ship(screen)

    while True:
        gf.check_events(ship)   
        gf.update_screen(ai_settings, screen, ship)

run_game()
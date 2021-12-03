from setting import Setting
import sys
import pygame

def run_game():
    pygame.init()
    ai_settings = Setting()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    while True:
        for event in pygame.event.get():
            # listen to Kayboard and mouse
            if event.type == pygame.QUIT:
                sys.exit()
            
            screen.fill(ai_settings.bg_color)
        
        pygame.display.flip()
        
run_game()
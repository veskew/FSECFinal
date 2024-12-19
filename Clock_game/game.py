import pygame
from pygame.locals import *
import sys
import datetime

pygame.init()

color1 = pygame.Color(0, 0, 0)  # Black
color2 = pygame.Color(255, 255, 255)  # White
color3 = pygame.Color(128, 128, 128)  # Grey
color4 = pygame.Color(255, 0, 0)  # Red
color5 = pygame.Color(130, 110, 20)

DISPLAYSURF = pygame.display.set_mode((1200, 800))
DISPLAYSURF.fill(color2)
pygame.display.set_caption("Game")

FPS = pygame.time.Clock()
FPS.tick(60)

ALLOWED_HOUR = 20
show_error = False

font = pygame.font.Font("./freedom/Freedom-10eM.ttf", 30)
text_surface1 = font.render(
    "You can only play this game between eight and nine PM", True, color5
)  # White text
text_rect1 = text_surface1.get_rect(center=(600, 400))  # Centered on the screen

text_surface2 = font.render(
    "Start game", True, color3
)  # White text
text_rect2 = text_surface1.get_rect(center=(1010, 650))  # Centered on the screen

text_surface3 = font.render(
    "There is no game get pranked lol", True, color5
)  # White text
text_rect3 = text_surface1.get_rect(center=(600, 400))  # Centered on the screen

run = True

while run is True:

    DISPLAYSURF.fill((0, 0, 0))  # Black background
    mouse_buttons = pygame.mouse.get_pressed()
    mouse_position = pygame.mouse.get_pos()
    current_time = datetime.datetime.now()
    current_hour = int(current_time.strftime("%H:%M:%S")[0:2])
    object1 = pygame.Rect((450, 600), (300, 100))
    if show_error:
        DISPLAYSURF.blit(text_surface1, text_rect1)
    rectangle_clicked = object1.collidepoint(mouse_position) and mouse_buttons[0]
    if rectangle_clicked and current_hour == ALLOWED_HOUR:
        run = False
    elif rectangle_clicked:
        show_error = True
    pygame.draw.rect(DISPLAYSURF, color4, object1)
    DISPLAYSURF.blit(text_surface2, text_rect2)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

while True:
    DISPLAYSURF.fill((0, 0, 0))
    image = pygame.image.load("Untitled.jpeg")  # Replace with the path to your image
    DISPLAYSURF.blit(
        image, (200, 150)
    )  # (x, y) coordinates where you want to display the image
    DISPLAYSURF.blit(text_surface3, text_rect3)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

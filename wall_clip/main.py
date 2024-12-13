import pygame

# pygame setup
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

# Text setup
font = pygame.font.Font(".././Clock_game/freedom/Freedom-10eM.ttf", 30)
text_surface1 = font.render(
    "Use WASD to move and space for a boost", True, (0, 50, 100)
)  # White text
text_rect1 = text_surface1.get_rect(center=(SCREEN_WIDTH/2, 40))  # Centered on the screen

# Player setup
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_size = 20
player_color = "blue"
player_speed = 300
player = pygame.Rect(player_pos.x, player_pos.y, player_size, player_size)

# Walls
walls = {
    "left": pygame.Rect(SCREEN_WIDTH*2/8, SCREEN_HEIGHT/3, 5, SCREEN_HEIGHT/3),
    "right": pygame.Rect(SCREEN_WIDTH*6/8 - 5, SCREEN_HEIGHT/3, 5, SCREEN_HEIGHT/3),
    "top": pygame.Rect(SCREEN_WIDTH*2/8, SCREEN_HEIGHT/3, SCREEN_WIDTH*4/8, 5),
    "bottom": pygame.Rect(SCREEN_WIDTH*2/8, SCREEN_HEIGHT*2/3, SCREEN_WIDTH*4/8, 5),
}

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player_speed = 300

    # Reset player color
    player_color = "blue" 

    # Handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= player_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += player_speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= player_speed * dt
    if keys[pygame.K_d]:
        player_pos.x += player_speed * dt
    if keys[pygame.K_SPACE]:
        player_speed = 500
        player_color = "green"

    # Update player rectangle's position
    player.topleft = (player_pos.x, player_pos.y)

    # Collision detection
    for wall, rectangle in walls.items():
        if player.colliderect(rectangle):
            player_color = "red"
            player_pos.x = SCREEN_WIDTH/2
            player_pos.y = SCREEN_HEIGHT/2

    # Draw background
    screen.fill("grey")

    # Draw walls
    for wall in walls.values():
        pygame.draw.rect(screen, "black", wall)

    # Draw player
    pygame.draw.rect(screen, player_color, player)
    screen.blit(text_surface1, text_rect1)

    # Flip the display to put your work on screen
    pygame.display.flip()

    # Limit FPS to 60
    # dt is delta time in seconds since the last frame
    dt = clock.tick(15) / 1000

pygame.quit()

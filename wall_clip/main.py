import pygame

# pygame setup
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

# Player setup
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_size = 80
player_color = "blue"
player_speed = 300
player = pygame.Rect(player_pos.x, player_pos.y, player_size, player_size)

# Walls
walls = {
    "left": pygame.Rect(0, 0, 200, SCREEN_HEIGHT),
    "right": pygame.Rect(SCREEN_WIDTH - 200, 0, 200, SCREEN_HEIGHT),
    "top": pygame.Rect(0, 0, SCREEN_WIDTH, 200),
    "bottom": pygame.Rect(0, SCREEN_HEIGHT - 200, SCREEN_WIDTH, 200),
}

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

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
        player_speed = 600

    # Update player rectangle's position
    player.topleft = (player_pos.x, player_pos.y)

    # Collision detection
    for wall, rectangle in walls.items():
        if player.colliderect(rectangle):
            player_color = "red"
            if wall == "left":
                player_pos.x += 300 * dt
            elif wall == "right":
                player_pos.x -= 300 * dt
            elif wall == "top":
                player_pos.y += 300 * dt
            elif wall == "bottom":
                player_pos.y -= 300 * dt


    # Draw walls
    for wall in walls.values():
        pygame.draw.rect(screen, "black", wall)

    # Draw player
    pygame.draw.rect(screen, player_color, player)

    # Flip the display to put your work on screen
    pygame.display.flip()

    # Limit FPS to 60
    # dt is delta time in seconds since the last frame
    dt = clock.tick(60) / 1000

pygame.quit()

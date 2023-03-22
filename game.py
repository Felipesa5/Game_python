import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH = 640
HEIGHT = 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Atrapar el Objeto")

# Configuración de colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Configuración del objeto a atrapar
obj_x = random.randint(0, WIDTH - 50)
obj_y = 0
obj_size = 50

# Configuración del jugador
player_x = WIDTH // 2
player_y = HEIGHT - 50
player_size = 50
player_speed = 5

# Configuración del reloj
clock = pygame.time.Clock()

# Configuración de la puntuación
score = 0
font = pygame.font.SysFont(None, 30)

# Bucle principal del juego
running = True
while running:
    # Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Movimiento del objeto
    obj_y += 5
    if obj_y > HEIGHT:
        obj_x = random.randint(0, WIDTH - 50)
        obj_y = 0
        score += 1

    # Comprobar si el jugador atrapa el objeto
    if obj_y + obj_size > player_y and obj_x > player_x and obj_x + obj_size < player_x + player_size:
        obj_x = random.randint(0, WIDTH - 50)
        obj_y = 0
        score += 10

    # Dibujar objetos en pantalla
    SCREEN.fill(WHITE)
    pygame.draw.rect(SCREEN, BLUE, (obj_x, obj_y, obj_size, obj_size))
    pygame.draw.rect(SCREEN, RED, (player_x, player_y, player_size, player_size))

    # Mostrar puntuación en pantalla
    text = font.render("Puntuación: " + str(score), True, BLUE)
    SCREEN.blit(text, (10, 10))

    # Actualizar pantalla
    pygame.display.update()

    # Configuración del reloj
    clock.tick(60)

# Salida del juego
pygame.quit()

import pygame
import random

pygame.init()
ventana = pygame.display.set_mode((600, 400))
reloj = pygame.time.Clock()
puntos = 0

# Configuración del juego
teclas = [pygame.K_a, pygame.K_s, pygame.K_d]
colores = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Rojo, Verde, Azul

ejecutando = True
while ejecutando:
    objetivo = random.randint(0, 2)
    ventana.fill((0, 0, 0))  # Fondo negro
    pygame.draw.circle(ventana, colores[objetivo], (300, 200), 50)
    pygame.display.flip()

    # Esperar respuesta
    inicio = pygame.time.get_ticks()
    respondio = False
    while pygame.time.get_ticks() - inicio < 1000:  # 1 segundo
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == teclas[objetivo]:
                    puntos += 1
                    print(f"¡Punto! Total: {puntos}")
                    respondio = True
                    break
        if respondio: break

    if not respondio:
        print("¡Muy lento!")
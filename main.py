import pygame
import math
import rand


pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE)

FRAME = 0


class Graph:
    def __init__(self, edges, num_vertices):
        self.edges = edges
        self.num_vertices = num_vertices

    def draw(self, screen):
        centerx, centery = WIDTH / 2, HEIGHT / 2
        radius = round(0.75 * min(WIDTH, HEIGHT) / 2)

        coords = []
        for i in range(self.num_vertices):
            angle = float(i) / self.num_vertices * 2 * math.pi + FRAME * 0.001
            coords.append(
                [
                    round(math.cos(angle) * radius + centerx),
                    round(math.sin(angle) * radius + centery),
                ]
            )

        for x in coords:
            pygame.draw.circle(
                screen, (0, 100, 255), (x[0], x[1]), 0.05 * min(WIDTH, HEIGHT)
            )


graph = Graph([{1, 2}, {0, 2}], 5)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            WIDTH = event.w
            HEIGHT = event.h
            # surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 100, 255), (250, 250), 75)
    graph.draw(screen)

    # Flip the display
    pygame.display.flip()

    FRAME += 1

# Done! Time to quit.
pygame.quit()


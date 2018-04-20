import pygame
def turnAround(pts):
    for i in range(45):
        pts[0]-=1
        pts[1]+=1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), color, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    for j in range(45):
        pts[0]+=0
        pts[1]+=0
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), color, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    for k in range(45):
        pts[0]+=1
        pts[1]-=1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), color, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    for q in range(45):
        pts[0]-=1
        pts[1]-=1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), color, pts, 100)
        pygame.display.update()
        pygame.display.flip()

def shear(pts):
    for i in range(100):
        pts[1] -= 1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), color, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    for j in range(200):
        pts[1] += 1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), color, pts, 100)
        pygame.display.update()
        pygame.display.flip()

def scope():
    pygame.draw.circle(surface, color, [200, 150], 100)

surface = pygame.display.set_mode((800, 600))
color = (250, 250, 0)
points = [200,150]
pygame.display.init()
img = pygame.draw.circle(surface, color, [200, 150], 50)
pygame.display.flip()
pygame.time.wait(1000)
scope()
pygame.time.wait(1000)
turnAround([200,150])  
shear(points)
pygame.display.flip()




import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE=pygame.display.set_mode((400,300))
pygame.display.set_caption("Just Window")

def main():
    sysfont = pygame.font.SysFont(None,36)
    Counter=0
    while True:
        SURFACE.fill((255,255,0))

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        Counter += 1
        SURFACE.fill((0,0,0))
        count_image=sysfont.render(
            "count is {}".format(Counter),True,(255,255,255))
        SURFACE.blit(count_image,(50,50))
        pygame.display.update()

if __name__=='__main__':
    main()
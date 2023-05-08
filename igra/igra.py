import pygame
import random
import sys
import time
import datetime

pygame.init()
X, Y = 1200, 900
screen = pygame.display.set_mode([X, Y])
pygame.display.set_caption("Igra")


korzina=pygame.image.load("korzina.png")
ablk=pygame.image.load("apple.png")
jagod=pygame.image.load("jagod.png")
grusa=pygame.image.load("grusa.png")
fon=pygame.image.load("les.jpg")
font = pygame.font.SysFont("comicsansms", 40)

# korzina
korzina_pos= [X - korzina.get_rect().width, Y - korzina.get_rect().height]
korzina_speed= 10

#jabloko
ablk_pos= [random.randint(0, X - ablk.get_rect().width), 0]
ablk_speed= 3

#jagodi
jagod_pos= [random.randint(0, X - jagod.get_rect().width), 0]
jagod_speed= 5

#grusa
grusa_pos=[random.randint(0, X - grusa.get_rect().width), 0]
grusa_speed=5

#Vremja
kell = pygame.time.Clock()
gameover = False
start_kell = time.time()

muutuja=0


while not gameover:
    kell.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
    if time.time() - start_kell >=20:
        with open("result.txt", "a") as f:#text file
            f.write(f"Play time: {time.time() - start_kell} seconds\n")#aeg 
            f.write(f"Score: {muutuja}\n")# Muttaja arv
            f.write("\n")
        print("Game over!")
        
        gameover = True
#dvizenie
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        korzina_pos[0] -= korzina_speed
    elif keys[pygame.K_RIGHT]:
        korzina_pos[0] += korzina_speed

#Spawn predmetov
    ablk_pos[1] += ablk_speed
    if ablk_pos[1] > Y:
        ablk_pos = [random.randint(0, X - ablk.get_rect().width), 0]

    grusa_pos[1] += grusa_speed
    if grusa_pos[1] > Y:
        grusa_pos = [random.randint(0, X - grusa.get_rect().width), 0]

    jagod_pos[1] += jagod_speed
    if jagod_pos[1] > Y:
        jagod_pos = [random.randint(0, X - jagod.get_rect().width), 0]

#ochki
    
    if pygame.Rect(*korzina_pos, *korzina.get_size()).colliderect(pygame.Rect(*ablk_pos, *ablk.get_size())):
        muutuja+= 1
        ablk_pos = [random.randint(0, X - ablk.get_rect().width), 0]
    
    if pygame.Rect(*korzina_pos, *korzina.get_size()).colliderect(pygame.Rect(*grusa_pos, *grusa.get_size())):
        muutuja+= 2
        grusa_pos = [random.randint(0, X - grusa.get_rect().width), 0]

    if pygame.Rect(*korzina_pos, *korzina.get_size()).colliderect(pygame.Rect(*jagod_pos, *jagod.get_size())):
        muutuja+= 3
        jagod_pos=[random.randint(0, X - jagod.get_rect().width), 0]

    
    screen.blit(fon, (0, 0))
    screen.blit(korzina, korzina_pos)
    screen.blit(ablk, ablk_pos)
    screen.blit(grusa, grusa_pos)
    screen.blit(jagod, jagod_pos)
    pygame.display.flip()
    
    

    pygame.display.update()

pygame.quit() 
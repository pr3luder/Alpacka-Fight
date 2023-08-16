import pygame
h=900
b=1100
Wiese = pygame.image.load('wiese.png')
Wiese = pygame.transform.scale(Wiese, (1100,500))
Wiese_x=0
Wiese_Y=400
alpacka = pygame.image.load('alpacka.png')
alpacka = pygame.transform.scale(alpacka, (200,200))
alpacka_x=0
alpacka_y=530
alpackaböse = pygame.image.load('alpackaböse.png')
alpackaböse = pygame.transform.scale(alpackaböse, (200,200))
alpackaböse_x=600
alpackaböse_y=530
schussbewegung=195
schuss1 = pygame.image.load('schuss.png')
schuss1 = pygame.transform.scale(schuss1, (20,20))
schuss1_x=alpacka_x+schussbewegung
schuss1_y=alpacka_y+25
f=pygame.display.set_mode((b,h))
Run=True
while Run:
    f.fill((0,0,251))

    f.blit(Wiese,(Wiese_x,Wiese_Y))

    f.blit(alpacka,(alpacka_x,alpacka_y))
    f.blit(alpackaböse,(alpackaböse_x,alpackaböse_y))
    f.blit(schuss1,(schuss1_x,schuss1_y))
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run=False

    

    
    pygame.display.update()

pygame.quit()
import pygame,random, textos

#Tamaño de pantalla
ANCHO = 800
ALTO = 500
vel = 8
live = 100
enemy_live = 100

puntuacion = 0
enemy_puntuacion = 0

arial = pygame.font.match_font("Arial")
gotica = pygame.font.match_font("Gotica")
#Aqui especificamos todo lo del jugador
class Player(pygame.sprite.Sprite):

    #SPRITE DEL JUGADOR
    def __init__(self):
        super().__init__()
        #Rectangulo del jugador
        self.nave = pygame.image.load("navesota.png").convert_alpha() #esta es la imagen del jugador
        self.image = pygame.transform.scale(self.nave,(100,70))#Transforma la escala de la imagen
        self.image.set_colorkey((0,0,0))

        #Obtiene el rectangulo de la imagen (hitbox o sprite)
        self.rect =  self.image.get_rect()
        #centra el sprite o hitbox
        self.rect.center = (0, random.randrange(ALTO))

        self.cadencia = 180
        self.ultimo_disparo = pygame.time.get_ticks()



    #update pertenece a la clase sprite
    def update(self):


        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_a]:
            self.rect.x -= vel
        if userInput[pygame.K_d]:
            self.rect.x += vel
        if userInput[pygame.K_w]:
            self.rect.y -= vel
        if userInput[pygame.K_s]:
            self.rect.y += vel

        if userInput[pygame.K_f]:
            puslacion_ahora = pygame.time.get_ticks()#Esto indica la tecla presionada 
            if puslacion_ahora - self.ultimo_disparo > self.cadencia:#si a pasado mas de el valor de self.cadencia en milisegundo entonces se cumple la condicion
                jugador.disparo()
                s_disparo.play()

                self.ultimo_disparo = puslacion_ahora #Resetea el tiempo para que el disparo se vuelva activar dependiendo de la cadencia

        #limita la parte superior para que el jugador no pase
        if self.rect.top < 0:
            self.rect.top = 0

        #limita la parte inferior para que el jugador no pase
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO 

        #limita la parte izquierda
        if self.rect.left < 0:
            self.rect.left = 0 

        
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        # #Actualiza esto cada vuelta de bucle
        # self.rect.x += 10
        # if self.rect.left > ANCHO: #rect.top es el limite de arriba de la pantalla
        #     self.rect.right = 8 #rect.bottom es el limite de abajo de la pantalla

    def disparo(self):
        bala = Disparos(self.rect.centerx, self.rect.centery)
        balas.add(bala)
#Aqui especificamos todo lo del jugador
class Oponente(pygame.sprite.Sprite):

    #SPRITE DEL JUGADOR
    def __init__(self):
        super().__init__()
        #Rectangulo del jugador
        self.oponente = pygame.image.load("enemigo.jpg").convert_alpha() #esta es la imagen del jugador
        self.image = pygame.transform.scale(self.oponente,(100,70))
        self.image.set_colorkey((0,0,0))

        #Obtiene el rectangulo de la imagen (hitbox o sprite)
        self.rect =  self.image.get_rect()
        #centra el sprite o hitbox
        self.rect.center = (ANCHO - self.rect.width, ALTO // 2)
        self.cadencia = 180
        self.ultimo_disparo = pygame.time.get_ticks()
    
    def update(self):


        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_LEFT]:
            self.rect.x -= vel
        if userInput[pygame.K_RIGHT]: 
            self.rect.x += vel
        if userInput[pygame.K_UP]:
            self.rect.y -= vel
        if userInput[pygame.K_DOWN]:
            self.rect.y += vel

        if userInput[pygame.K_SPACE]:
            puslacion_ahora = pygame.time.get_ticks()#Esto indica la tecla presionada 
            if puslacion_ahora - self.ultimo_disparo > self.cadencia:#si a pasado mas de el valor de self.cadencia en milisegundo entonces se cumple la condicion
                enemy.disparo()
                s_disparo.play()
                self.ultimo_disparo = puslacion_ahora
              

        #limita la parte superior para que el jugador no pase
        if self.rect.top < 0:
            self.rect.top = 0

        #limita la parte inferior para que el jugador no pase
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO 

        #limita la parte izquierda
        if self.rect.left < 0:
            self.rect.left = 0 

        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
    
    def disparo(self):
        bala = Disparos_enemigo(self.rect.centerx, self.rect.centery)
        e_balas.add(bala)

            

class Disparos(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("disparo.jpeg").convert(),(20,20))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()#obtenemos el rectangulo de la imagen
        self.rect.bottom = y
        self.rect.centerx = x #va a centrarlo en la pocicision en medio del rectangulo del jugador o enemigo

    def update(self): #nos sirve para actualizar la posicion de la bala
        self.rect.x += 15
        if self.rect.right > ANCHO:
            self.kill()


class Disparos_enemigo(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("disparo.jpeg").convert(),(20,20))#Carga la imagen y le cambia su escala
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()#obtenemos el rectangulo de la imagen
        self.rect.bottom = y
        self.rect.centerx = x #va a centrarlo en la pocicision en medio del rectangulo del jugador o enemigo

    def update(self): #nos sirve para actualizar la posicion de la bala
        self.rect.x -= 15 #Define la velocidad con la que va la bala
        if self.rect.right > ANCHO: #si el borde derecho de la hitbox de la bala(self.rect) es mayor al ancho de la pantalla entonces se elimina
            self.kill()
        





#comienzo del juego

pygame.init()#inicializamos  pygame

screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("WHILEGAME")#le coloca un nombre a la ventana que en este caso es whilegame
clock = pygame.time.Clock()#Define un relojo que se va utilizar para los fps

s_disparo = pygame.mixer.Sound("disparo.mp3")#Carga el sonido del disparo



#Grupo de sprites, instanciacion del objeto jugador.
sprites = pygame.sprite.Group() #instancia de la clase sprite group
enemigos = pygame.sprite.Group()#instancia de la clase sprite group
balas = pygame.sprite.Group()#instancia de la clase sprite group
e_balas = pygame.sprite.Group()#instancia de la clase sprite group balas enemigas
jugador = Player() #instancia de la clase player    
enemy = Oponente() #instancia de la clase Oponente

fondo = pygame.image.load("fondo_pixelart.jpg").convert()

sprites.add(jugador) # le adañimmos a jugador para que tenga la imagen del jugador
enemigos.add(enemy) # le adañimos a enemy parar que tenga la imagen del enemigos (jugador 2)

run = True # si run es true funciona el bucle si es falso se cierra la ventana




while run:


    clock.tick(60)#Define los fps del jugador
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # si se cumple la condicion cierra la ventana
            run = False


    

    sprites.update() # esto actualiza todos los sprites en la pantalla
    enemigos.update() #actualiza todos los sprites de los enemigos en pantalla
    balas.update() # acutaliza todos los sprites de las balas (player_1)
    e_balas.update() # actualiza todos los sprites de las balas enemigas(player2)

 

    # colision = pygame.sprite.groupcollide(enemigos,balas, False, True)#esto nos permite utilizar un sprite contra un grupo
    
    # if colision:
    #     live -= 5

    #Zona de dibujo    
    screen.fill((255,0,0))# primer parametro R(rojo) G(verde) B(blue)



    # Si live es menor a 0 muestra el texto game over (live es la vida del jugador de la izquierda)
    if live <= 0  :
        screen.fill((0,0,0))
        
        over = textos.show_text(screen, gotica, "GAME OVER", (255,255,255), 50, (ANCHO / 2 - 150), (ALTO / 2 - 50))
        win_1 = textos.show_text(screen, gotica, "PLAYER 2 WIN", (255,255,255), 50, (ANCHO / 2 - 150), (ALTO / 2 ))
       

    # Si enemy_live es menor a 0 muestra el texto game over (enemy_live es la vida del jugador de la derecha)
    if enemy_live <= 0 :
        over = textos.show_text(screen, gotica, "GAME OVER", (0,0,0), 50, (ANCHO / 2 - 150), (ALTO / 2 - 50))
        win_2 = textos.show_text(screen, gotica, "PLAYER 1 WIN", (0,0,0), 50, (ANCHO / 2 - 150), (ALTO / 2 ))

    colision = pygame.sprite.groupcollide(sprites,e_balas, False, True) # si las balas chocan con el player 1

    e_colision = pygame.sprite.groupcollide(enemigos, balas, False, True)

    bala_colision = pygame.sprite.groupcollide(e_balas, balas, False, True)#Colision de balas si las balas chocan entre si mismas se desaparecen

    if bala_colision:
        for i in e_balas:
            i.kill()

    if colision : #si las balas chocan con el player 1 le baja 6 puntos a live
        live -= 6
        enemy_puntuacion += 1

        
    if e_colision: # si las balas chocan con el player2 le baja 6 puntos a enemy live
        enemy_live -= 6
        puntuacion += 1

    

    if jugador.rect.colliderect(enemy.rect): #si la hitbox del jugador choca con la hitbox del enemigo live disminuye la vida de player 1 (live)
        live -= 0.3
        pygame.draw.rect(screen, (255,255,255), jugador.rect, 4)

    if enemy.rect.colliderect(jugador.rect): #si la hitbox del enemigo choca con la hitbox del jugador enemy_live disminuye la vida del player2
        pygame.draw.rect(screen, (255,255,255), enemy.rect, 4)
        enemy_live -= 0.3

    
    

    pygame.draw.rect(screen,(0,0,255), (10,10,live,20)) #dibuja el rectangulo la vidad del jugador 1
    pygame.draw.rect(screen,(0,255,0), ((ANCHO - 110),10,enemy_live,20))# dibuja el rectangulo de la vida del jugador 2
    
    p1_score = textos.show_text(screen, gotica,"SCORE: {0}".format(puntuacion), (0,0,0), 20,30,450) #Puntuacion del player 1
    p2_score = textos.show_text(screen, gotica,"SCORE: {0}".format(enemy_puntuacion), (0,0,0), 20,(ANCHO - 100),450)#Puntuacion del player 2

    

    #dibuja los sprites, enemigos, balas, balas enemigas = e_balas
    sprites.draw(screen)
    enemigos.draw(screen)
    balas.draw(screen)
    e_balas.draw(screen)
    
    pygame.display.flip() #actualiza la pantalla


pygame.quit()#quita el juego

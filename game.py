import pygame,random, textos

#Tamaño de pantalla
ANCHO = 1200 #Ancho de la pantalla
ALTO = 500 #Alto de la pantalla
vel = 6.5 #Velocidad de las naves
live = 100 # Vida del jugador 1 o jugador de la izquierda 
enemy_live = 100 #Vida del jugador 2 o jugador de la derecha
x = 0 #coordenada x de la pantalla

puntuacion = 0 #puntacion jugador 1 o jugador de la izquierda
enemy_puntuacion = 0#puntuacion jugador 2 o jugador de la derecha

#Tipos de letras
arial = pygame.font.match_font("Arial")
gotica = pygame.font.match_font("Gotica")
#Aqui especificamos todo lo del jugador
class Player(pygame.sprite.Sprite):

    #SPRITE DEL JUGADOR
    def __init__(self):
        super().__init__()
        #Rectangulo del jugador
        self.nave = pygame.image.load("navesota.png").convert_alpha() #esta es la imagen del jugador
        self.image = pygame.transform.scale(self.nave,(90,60))#Transforma la escala de la imagen
        self.image.set_colorkey((0,0,0))#El color que este en el parametro lo elimina en este caso el negro del fondo lo elimina

        #Obtiene el rectangulo de la imagen (hitbox o sprite)
        self.rect =  self.image.get_rect()
        #centra el sprite o hitbox
        self.rect.center = (0, random.randrange(ALTO))

        self.cadencia = 290 #El tiempo entre disparos
        self.ultimo_disparo = pygame.time.get_ticks()#ultimo disparo para tener como referencia en cuanto tiempo disparar el otro



    #update pertenece a la clase sprite
    def update(self):

        #Define el movimiento de el player o jugador detecta la tecla presionada
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_a]: # Con la letra a se vueve hacia la izquierda
            self.rect.x -= vel
        if userInput[pygame.K_d]: # Con la letra d se mueve hacia la derecha
            self.rect.x += vel
        if userInput[pygame.K_w]: # con la letra w se mueve hacia arriba
            self.rect.y -= vel
        if userInput[pygame.K_s]: # con la letra s se mueve hacia abajo
            self.rect.y += vel

        if userInput[pygame.K_q]: # con la letra  q adisapara
            puslacion_ahora = pygame.time.get_ticks()#Esto indica la tecla presionada 
            if puslacion_ahora - self.ultimo_disparo > self.cadencia:#si a pasado mas de el valor de self.cadencia en milisegundo entonces se cumple la condicion
                jugador.disparo()#llama a la funcion disparo
                s_disparo.play()#reproduce el sonido de disparo

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
       
    def disparo(self):
        bala = Disparos(self.rect.centerx, self.rect.centery) #ES una instancia de la clase disparo con su ubicacion inicial
        balas.add(bala) #la instancia se agrega a la lista balas
#Aqui especificamos todo lo del jugador
class Oponente(pygame.sprite.Sprite):

    #SPRITE DEL JUGADOR
    def __init__(self):
        super().__init__()
        #Rectangulo del jugador
        self.oponente = pygame.image.load("enemigo.png").convert_alpha() #esta es la imagen del jugador
        self.image = pygame.transform.scale(self.oponente,(90,60))#Transforma la escala del jugador para que sea mas pequeña
        self.image.set_colorkey((0,0,0))#El color que este en el parametro desaparece

        #Obtiene el rectangulo de la imagen (hitbox o sprite)
        self.rect =  self.image.get_rect()
        #centra el sprite o hitbox
        self.rect.center = (ANCHO - self.rect.width, random.randrange(ALTO)) # En que posicion aparece al inicio
        self.cadencia = 290 # la velocidad entre disparos
        self.ultimo_disparo = pygame.time.get_ticks()
    
    def update(self):

        #MOVIMIENTO DEL OPONENTE O JUGADOR 2
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_LEFT]: # Se mueve a la izquierda
            self.rect.x -= vel
        if userInput[pygame.K_RIGHT]: #Se mueve a la derecha 
            self.rect.x += vel
        if userInput[pygame.K_UP]: # Se mueve hacia arriba
            self.rect.y -= vel
        if userInput[pygame.K_DOWN]: # Se mueve hacia abajo
            self.rect.y += vel

        if userInput[pygame.K_RSHIFT]: # dispara con el shift derechow
            puslacion_ahora = pygame.time.get_ticks()#Esto indica la tecla presionada 
            if puslacion_ahora - self.ultimo_disparo > self.cadencia:#si a pasado mas de el valor de self.cadencia en milisegundo entonces se cumple la condicion
                enemy.disparo()#Llama al metodo disparo
                s_disparo.play()#reproduce el sonido 
                self.ultimo_disparo = puslacion_ahora #Actualiza el ultimo disparo para que se reinice y vuelva a repetir el ciclo
              

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
        self.image = pygame.transform.scale(pygame.image.load("bala.png").convert(),(20,20))#Carga la imagen y transforma su escla en 20 de ancho y 20 de alto
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()#obtenemos el rectangulo de la imagen
        self.rect.bottom = y
        self.rect.centerx = x #va a centrarlo en la pocicision en medio del rectangulo del jugador o enemigo

    def update(self): #nos sirve para actualizar la posicion de la bala
        self.rect.x += 10 #Velocidad de la bala
        if self.rect.right > ANCHO:
            self.kill() # Si la bala supera el ancho de la pantalla se elimina


class Disparos_enemigo(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("bala_2.png").convert(),(20,20))#Carga la imagen y transforma su escala en 20 , 20
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()#obtenemos el rectangulo de la imagen
        self.rect.bottom = y
        self.rect.centerx = x #va a centrarlo en la pocicision en medio del rectangulo del jugador o enemigo

    def update(self): #nos sirve para actualizar la posicion de la bala
        self.rect.x -= 10 #Define la velocidad con la que va la bala
        if self.rect.right > ANCHO: #si el borde derecho de la hitbox de la bala(self.rect) es mayor al ancho de la pantalla entonces se elimina
            self.kill()
        





#comienzo del juego

pygame.init()#inicializamos  pygame

screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("WHILEGAME")#le coloca un nombre a la ventana que en este caso es whilegame
clock = pygame.time.Clock()#Define un reloj que se va utilizar para los fps

background_simple = pygame.image.load("fondo_pixelart.png").convert() #Carga la imagen del fondo
background = pygame.transform.scale(background_simple,(2500,700))#Transforma la escala de la imagen

s_disparo = pygame.mixer.Sound("disparo.mp3")#Carga el sonido del disparo



#Grupo de sprites, instanciacion del objeto jugador.
sprites = pygame.sprite.Group() #instancia de la clase sprite group
enemigos = pygame.sprite.Group()#instancia de la clase sprite group
balas = pygame.sprite.Group()#instancia de la clase sprite group
e_balas = pygame.sprite.Group()#instancia de la clase sprite group balas enemigas
jugador = Player() #instancia de la clase player    
enemy = Oponente() #instancia de la clase Oponente

sprites.add(jugador) # le adañimmos a jugador para que tenga la imagen del jugador
enemigos.add(enemy) # le adañimos a enemy parar que tenga la imagen del enemigos (jugador 2)

run = True # si run es true funciona el bucle si es falso se cierra la ventana




while run: #inicia el bucle


    clock.tick(60)#Define los fps del jugador
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # si se cumple la condicion cierra la ventana
            run = False


    

    sprites.update() # esto actualiza todos los sprites en la pantalla
    enemigos.update() #actualiza todos los sprites de los enemigos en pantalla
    balas.update() # acutaliza todos los sprites de las balas (player_1)
    e_balas.update() # actualiza todos los sprites de las balas enemigas(player2)

 
    

    #Zona de dibujo    
  
    x_final = x % background.get_rect().width# Se divide el valor de x por el ancho de la imagen background y devuelve el resto

    
    screen.blit(background, (x_final - background.get_rect().width, 0))#Esto hace que la imagen se cargue en bucle
    if x_final < ANCHO:
        screen.blit(background,(x_final, 0))
    
    x -= 1#Es la velocidad con la que queremos que se vaya moviendo el fondo 

    # Si live es menor a 0 muestra el texto game over (live es la vida del jugador de la izquierda)
    if live <= 0  :
        over = textos.show_text(screen, gotica, "GAME OVER", (255,255,255), 50, (ANCHO / 2 - 150), (ALTO / 2 - 50))
        win_1 = textos.show_text(screen, gotica, "PLAYER 2 WIN", (255,255,255), 50, (ANCHO / 2 - 150), (ALTO / 2 ))
        run = False       

    # Si enemy_live es menor a 0 muestra el texto game over (enemy_live es la vida del jugador de la derecha)
    if enemy_live <= 0 :
        over = textos.show_text(screen, gotica, "GAME OVER", (0,0,0), 50, (ANCHO / 2 - 150), (ALTO / 2 - 50))
        win_2 = textos.show_text(screen, gotica, "PLAYER 1 WIN", (0,0,0), 50, (ANCHO / 2 - 150), (ALTO / 2 ))
        run = False
    colision = pygame.sprite.groupcollide(sprites,e_balas, False, True) # detecta la colision de las balas del jugador 2 con cualquier de el sprite el jugador 1

    e_colision = pygame.sprite.groupcollide(enemigos, balas, False, True) # detecta la colision de las balas del jugador 1 con cualquiera de la lista de enemigos


    #codigo en mantinemiento lo que esta desde la linea 260 - 266

    # e_bala_colision = pygame.sprite.groupcollide(e_balas, balas, True, True)#Colision de balas si las balas chocan entre si mismas se desaparecen

    
    
    # if e_bala_colision:
    #     for i in e_balas:
    #         i.kill()

    if colision : #si las balas chocan con el player 1 le baja 6 puntos a live
        live -= 2.5
        enemy_puntuacion += 1

        
    if e_colision: # si las balas chocan con el player2 le baja 6 puntos a enemy live
        enemy_live -= 2.5
        puntuacion += 1

    

    if jugador.rect.colliderect(enemy.rect): #si la hitbox del jugador choca con la hitbox del enemigo live disminuye la vida de player 1 (live)
        live -= 0.3
        pygame.draw.rect(screen, (255,255,255), jugador.rect, 4)

    if enemy.rect.colliderect(jugador.rect): #si la hitbox del enemigo choca con la hitbox del jugador enemy_live disminuye la vida del player2
        pygame.draw.rect(screen, (255,255,255), enemy.rect, 4)
        enemy_live -= 0.3

    
    

    pygame.draw.rect(screen,(0,0,255), (10,10,live,20)) #dibuja el rectangulo la vidad del jugador 1
    pygame.draw.rect(screen,(0,255,0), ((ANCHO - 110),10,enemy_live,20))# dibuja el rectangulo de la vida del jugador 2
    
    p1_score = textos.show_text(screen, gotica,"SCORE: {0}".format(puntuacion), (255,255,255), 20,30,450) #Puntuacion del player 1
    p2_score = textos.show_text(screen, gotica,"SCORE: {0}".format(enemy_puntuacion), (255,255,255), 20,(ANCHO - 100),450)#Puntuacion del player 2

    p1_salud = textos.show_text(screen, gotica,"SALUD: {0}".format(int(live)), (255,255,255), 20,10,30) #Muestra el texto de la salud del primer jugador
    p2_salud = textos.show_text(screen, gotica,"SALUD: {0}".format(int(enemy_live)), (255,255,255), 20,(ANCHO - 110),30)#Muestra el texto de la salud del segundo jugador
    

    #dibuja los sprites, enemigos, balas, balas enemigas y e_balas
    sprites.draw(screen)
    enemigos.draw(screen)
    balas.draw(screen)
    e_balas.draw(screen)
    
    pygame.display.flip() #actualiza la pantalla


pygame.quit()#quita el juego

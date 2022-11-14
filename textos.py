import pygame

def show_text(pantalla, fuente, texto, color, dimensiones,x,y):
    tipo_letra = pygame.font.Font(fuente, dimensiones)#Define el tipo de letra
    superficie = tipo_letra.render(texto, False, color)#texto : es el texto que vamos a mostrar  True: si queremos utilizar el anti-alaising en las letras colocamos True si no False
    rectangulo = superficie.get_rect()
    rectangulo.x = x
    rectangulo.y = y
    pantalla.blit(superficie, rectangulo)
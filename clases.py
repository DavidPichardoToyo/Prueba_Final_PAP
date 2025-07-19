from abc import abstractmethod , ABC
from error import LargoExcedidoError, SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo:str, url_click:str, sub_tipo:str):
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_click = url_click
        self.__sub_tipo = sub_tipo

    
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        self.__alto = alto

    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def ancho(self, url_archivo):
        self.__url_archivo = url_archivo


    @property
    def url_click(self):
        return self.__url_click
    
    @url_click.setter
    def url_click(self, url_click):
        self.__url_click = url_click

    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        if (isinstance (self,Video) and sub_tipo in Video.SUB_TIPOS
            or isinstance (self, Social) and sub_tipo in Social.SUB_TIPOS
            or isinstance (self, Display) and sub_tipo in Display.SUB_TIPOS):
            self.__sub_tipo = sub_tipo           
        else:
            raise SubTipoInvalidoError("error de tipo invalido")
        #si la instancia actual == instancia de video y self.subtipo esta en la tupla 

    @staticmethod
    def mostrar_formatos():
        return {Video.FORMATO} - {Social.FORMATO} - {Display.FORMATO}
    
    @abstractmethod  
    def comprimir_anuncio():
        pass

    @abstractmethod
    def redimensionar_anuncio():
        pass



class Campana:
    def __init__(self, nombre, fecha_inicio, fecha_termino):
        self.__nombre = nombre 
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.contador_display = 0
        self.contador_video = 0
        self.contador_social = 0
        self.__anuncios = [Video(45,1,1, "En tu corazón", "Hasta el infinito", "Instream")]

    def peticiones(self, anuncio):
        ancho = int(input(f"Ingrese el ancho del {anuncio}: "))
        alto = int(input(f"Ingrese el alto del {anuncio}: "))
        url_archivo = input(f"Ingrese la url del {anuncio}: ")
        url_click = input(f"Ingrese la url para hacer click del {anuncio}: ")
        sub_tipo = input(f"Ingrese el subtipo del {anuncio}: ")

        return ancho, alto, url_archivo, url_click, sub_tipo

    def componer_anuncio(self):
        
        opcion = int(input("que tipo de anuncio quieres?\n  1. - para video - 2. - para display - 3. - para social"))
        if opcion == 1:
            duracion = int(input("cual es la duracion del video (minimo 5): "))
            ancho, alto, url_archivo, url_click, sub_tipo = self.peticiones("video")
            new_anuncio = Video(duracion, ancho, alto, url_archivo, url_click, sub_tipo)
            self.contador_video += 1
        elif opcion == 2:
            ancho, alto, url_archivo, url_click, sub_tipo = self.peticiones("display")
            new_anuncio = Display(ancho, alto, url_archivo, url_click, sub_tipo)
            self.contador_display += 1
        elif opcion == 3:
            ancho, alto, url_archivo, url_click, sub_tipo = self.peticiones("social")
            new_anuncio = Social(ancho, alto, url_archivo, url_click, sub_tipo)
            self.contador_social += 1
        
        return new_anuncio
     
    def agregar_anuncios(self):

        
        while True:
            try:
                opcion = int(input("que tipo de anuncio quieres  1 -  para video - 2 para display - 3 para social"))
                if opcion == 1:
                    duracion = int(input("cual es la duracion del video  minimo 5"))
                    new_anuncio = Video(duracion)
                elif opcion == 2:
                    new_anuncio = Display()
                elif opcion == 3:
                    new_anuncio = Social()
                else:
                    break
                    
                self.__anuncios.append(new_anuncio)
            except Exception as e:
                pass
        #opcion que el usuario pone la opcion y entramos al bucle while\
        #self.__anuncios.append(new_anuncio)
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if len(nombre) <= 250:
            self.__nombre = nombre
        else:
            raise  LargoExcedidoError("el largo del texto supera los 250 caracteres")

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio


    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, fecha_termino):
        self.__fecha_termino = fecha_termino

    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @property
    def anuncios(self):
        return self.__anuncios
    
    def __repr__(self):
        return f"nombre de campana  :{self.nombre} - {self.__anuncios}"
            

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("INSTREAM" , "OUTSTREAM" )

    def __init__(self,duracion):
        self.ancho = 1 
        self.alto = 1
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self,duracion):
        self.__duracion = duracion 

      
    def comprimir_anuncio():
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio():
        print( "RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

    def __repr__(self):
        return f"{Video.FORMATO} - {self.duracion}"
    

class Display(Anuncio):
    FORMATO = "DISPLAY"
    SUB_TIPOS = ("TRADICIONAL" , "NATIVE")

    def __init__(self, ancho, alto, url_archivo, url_click, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)

    def comprimir_anuncio():
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio():
        print( "RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

    def __repr__(self):
        return f"{Display.FORMATO}"

class Social(Anuncio):
    FORMATO = "SOCIAL"
    SUB_TIPOS = ("FACEBOOK" , "LINKEDIN" )

    def __init__(self, ancho, alto, url_archivo, url_click, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)

    def comprimir_anuncio():
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio():
        print( "RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
    
    def __repr__(self):
        return f"{Social.FORMATO}"
import datetime
Libro1 = []
FechaPrestamo = []
class usuario:
    def __init__(self, nombre = 0, apellido= 0, cedula= 0, telefono= 0):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._telefono = telefono
    def set_nombre(self, nombre):
        self._nombre = nombre
    def get_nombrecompleto(self):
        return self._nombre
    def get_apellido(self):
        return self._apellido
    def set_cedula(self, cedula):
        self._cedula = cedula
    def get_cedula(self):
        return self._cedula
    def get_completo(self):
        return self._cedula
    def set_telefono(self, telefono):
        self.telefono = telefono
    def get_telefono(self):
        return self._telefono
class libros:
    def libro1(self):
        print("Actualmente contamos con un título")
        print("======================")
        Menu=[
            ["Título: Introduction to Java Programming"],
            ["3a. edición"],
            ["Autor: Liang, Y. Daniel"],
            ["ISBN: 0-13-0434323-X"],
            ["Prentice-Hall, New Jersey (USA), viernes 16 de noviembre de 2001"],
            ["784 páginas"]
        ]
        for x in range(6):
            print(Menu[x][0])
        print("======================")
        print("Si desea prestar un libro, escriba 1")
        print("Si desea volver al menú principal, escriba 2")
        print("======================")
        desicion = int(input(("Ingrese una opción: ")))
        if desicion == 1:
            Biblioteca = usuario()
            print("======================")
            Biblioteca.set_nombre(input("Para prestar un libro debes ingresar tu nombre completo: "))
            Biblioteca.set_cedula(input("Ahora ingresa tu número de cédula: "))
            Biblioteca.set_telefono(input("Ingrese su número de teléfono: "))
            print("======================")
            desicion = int(input(("Si desea prestar el libro, escriba 1: ")))
            if desicion == 1:
                if 1 in Libro1:
                    print("======================")
                    print("Libro no disponible, alguien ya lo prestó")
                    self.__init__()
                else:
                    print("======================")
                    print("Libro prestado con éxito")
                    print("======================")
                    print("Prestado a : ", (Biblioteca.get_nombrecompleto()))
                    print("Numero de cédula:", (Biblioteca.get_cedula()))
                    Fecha = datetime.datetime.now()
                    FechaPrestamo2 = datetime.datetime.strftime(Fecha, "%d/%m/%Y")
                    FechaPrestamo.append(FechaPrestamo2)
                    print("Dia prestado :",datetime.datetime.strftime(Fecha, "%d/%m/%Y"), "Hora :", datetime.datetime.strftime(Fecha, "%H:%M:%S"))
                    print("======================")
                    print("Gracias por preferirnos")
                    print("Redirigiendo al menú principal")
                    Libro1.append(1)
                    self.__init__()
            if desicion == 2:
                self.__init__()

class Inicio(usuario,libros):
    def __init__(self):
        super(Inicio,self).__init__()
        print("======================")
        print("Bienvenido a la biblioteca")
        tiempo =datetime.datetime.now()
        fecha= datetime.datetime.strftime(tiempo,"%B/%d/%Y")
        print("Fecha:",fecha)
        hora=datetime.datetime.strftime(tiempo,"%I:%M:%S") 
        print("Hora:",hora)
        print("¿Qué desea hacer hoy?")
        print("1 = Ver librería")
        print("2 = Prestar un libro")
        print("3 = Salir")
        print("======================")
        desicion = int(input("Ingrese una opción: "))
        print("======================")
        if desicion == 1:
            self.libro1()
        if desicion == 2:
            Biblioteca = usuario()
            Biblioteca.set_nombre(input("Para prestar un libro debes ingresar tu nombre completo: "))
            Biblioteca.set_cedula(input("Ahora ingresa tu número de cédula: "))
            Biblioteca.set_telefono(input("Ingrese su número de teléfono: "))
            print("======================")
            desicion = int(input(("Si desea prestar el libro Introduction to Java Programming, escriba 1: ")))
            if desicion == 1:
                if 1 in Libro1:
                    print("Libro no disponible")
                    self.__init__()
                else:
                    print("======================")
                    print("Libro prestado con éxito")
                    print("Prestado a : ", (Biblioteca.get_completo()))
                    print("Numero de cédula:", (Biblioteca.get_cedula()))
                    Fecha = datetime.datetime.now()
                    FechaPrestamo2 = datetime.datetime.strftime(Fecha, "%d/%m/%Y")
                    FechaPrestamo.append(FechaPrestamo2)
                    print("Dia prestado :",datetime.datetime.strftime(Fecha, "%d/%m/%Y"), "Hora :", datetime.datetime.strftime(Fecha, "%H:%M:%S"))
                    print("======================")
                    print("Gracias por preferirnos")
                    print("Redirigiendo al menú principal")
                    Libro1.append(1)
                    self.__init__()
        if desicion == 3:
            print("Un libro es una aventura, esperando quien la emprenda")
            print("Vuelva pronto")
            exit()
Biblioteca = Inicio()
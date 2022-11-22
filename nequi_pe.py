import datetime

Usuario_ = []
Contraseña_ = []
Ahorros_ = []

import datetime

class inicio():
    def login(self):
        print("======================")
        usuario = int(input("Ingrese su número de teléfono: "))
        if usuario in Usuario_:
            print
            contraseña = int(input("Ahora introduce tu contraseña: "))
            if contraseña in Contraseña_:
                print()
            else:
                print("======================")
                print("Número de teléfono o contraseña incorrecta")
                self.login()
        else:
            print("======================")
            print("Este número aún no se ha registrado")
            print("======================")
            desicion = int(input("Si desea registrarse escriba 1, o escriba 2 para volver al menú principal: "))
            print("======================")
            if desicion == 1:
                super(Inicio,self).registro()
            if desicion == 2:
                self.__init__()

    def registro(self):
        print("======================")
        self.usuarios = int(input("Ingrese su número de teléfono: "))
        if self.usuarios in (Usuario_):
            print("======================")
            print("Este número ya está en uso")
            print("Inténtelo nuevamente")
            self.registro()
        self.usuarios2 = input("Ingrese su nombre: ")
        self.contraseñas = int(input("Ingrese su contraseña: "))
        print("======================")
        print("Te has registrado existosamente", self.usuarios2)
        print("Gracias por utilizar nuestros servicios")
        print("Será redirigido al meú principal, por favor inicie sesión")
        print("======================")
        Usuario_.append(self.usuarios)
        Contraseña_.append(self.contraseñas)
        self.__init__()

class Inicio(inicio):
    def __init__(self):
        print("Bienvenido a Nequi")
        tiempo =datetime.datetime.now()
        fecha= datetime.datetime.strftime(tiempo,"%B/%d/%Y")
        print("Fecha:",fecha)
        hora=datetime.datetime.strftime(tiempo,"%I:%M:%S") 
        print("Hora:",hora)

        print("¿Qué desea hacer hoy?")
        print("1 = Iniciar sesión")
        print("2 = Registrarse")
        print("3 = Salir")
        print("======================")
        desicion2 = int(input("Ingrese una opción: "))
        if desicion2 == 1:
            super(Inicio,self).login()
        if desicion2 == 2:
            super(Inicio,self).registro()
        if desicion2 == 3:
            print("======================")
            exit("Gracias por usar nuestros servicios")

class NequiP(Inicio):
    def __init__(self):
        super().__init__()
        self.Menu()
    def Menu(self):
        print("======================")
        print("Bienvenido nuevamente",self.usuarios2)
        print("¿Qué desea hacer hoy?")
        print("1 = Crear una cuenta")
        print("2 = Administrar tu cuenta")
        print("3 = Cerrar sesión")
        print("======================")
        desicion3 = int(input("Ingrese una opción: "))
        if desicion3 == 1:
            self.CrearCuenta()
        if desicion3 == 2:
            self.AdministrarCuenta()
        if desicion3 == 3:
            print("======================")
            self.__init__()

    def CrearCuenta(self):
        print("======================")
        print("A continuación se muestra el tipo de cuenta disponible")
        print("1 = Cuenta de ahorros")
        print("======================")
        desicion = int(input("Ingrese el tipo de cuenta que desea crear: "))
        if desicion == 1:
            print("Cuenta de ahorros creada")
            print("======================")
            saldo = float(input("Ingrese el valor de su primera consignación: "))
            Ahorros_.append(saldo)
            print("Has depositado exitosamente",(saldo))
            self.AdministrarCuenta


    def AdministrarCuenta(self):
        print("======================")
        print("1 = Depositar dinero")
        print("2 = Ver saldo disponible")
        print("3 = Retirar dinero")
        print("4 = Regresar")
        print("======================")
        desicion = int(input("Ingrese una opción: "))
        if desicion == 1:
            print("======================")
            print("Cuentas disponibles")
            print("1 = Cuenta de ahorros")
            desicion = int(input("Seleccione la cuenta: "))
            if desicion == 1:
                print("======================")
                saldo2 = float(input("Ingrese el valor del deposito: "))
                Ahorros_.append(saldo2)
                print("Has depositado exitosamente",(saldo2))
                self.AdministrarCuenta()
        if desicion == 2:
            print("======================")
            print("Cuentas disponibles")
            print("1 = Cuenta de ahorros")
            desicion = int(input("Seleccione la cuenta: "))
            print("======================")
            if desicion == 1:
                print("El saldo total es de : $ ",sum(Ahorros_))
                self.AdministrarCuenta()
        if desicion == 3:
            TotalAhorros = sum(Ahorros_)
            print("======================")
            print("Cuentas disponibles")
            print("1 = Cuenta de ahorros")
            seleccion = int(input("Ingrese una opción: "))
            if seleccion == 1:
                print("======================")
                print("Su saldo disponible es de : ",Ahorros_)
                dinero_a_retirar = int(input("Ingrese la cantidad que desea retirar: "))
                if dinero_a_retirar < TotalAhorros:
                    print("======================")
                    print("Retiro realizado con exito")
                    DineroRestante = TotalAhorros - dinero_a_retirar  
                    Ahorros_.clear()
                    Ahorros_.append(DineroRestante)
                    print("Su nuevo saldo es de : ", Ahorros_)
                    self.AdministrarCuenta()
                if dinero_a_retirar > TotalAhorros:
                    print("======================")
                    print("Fondos insuficientes")
                    self.AdministrarCuenta()
        if desicion == 4:
            print("======================")
            print("Regresando al menu principal")
            self.Menu()
NequiP()
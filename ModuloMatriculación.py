import os

'''
    CREACION DE CLASES
'''

class Cargo:
    def __init__(self, id, descripcion):
        self.__id = id
        self.descripcion = descripcion

    @property
    def id(self):
        return self.__id

    def getCargo(self):
        return str(self.id)+"%"+self.descripcion

class Depto:
    def __init__(self, id, descripcion):
        self.__id = id
        self.descripcion = descripcion

    @property
    def id(self):
        return self.__id

    def getDepto(self):
        return str(self.id)+"%"+self.descripcion


class Empleado:
    def __init__(self, id, nombre, cedula, cargo, departamento, sueldo):
        self.__id = id
        self.nombre = nombre
        self.cedula = cedula
        self.cargo = cargo
        self.departamento= departamento
        self.sueldo= sueldo

    @property
    def id(self):
        return self.__id

    def getEmpleado(self):
        return str(self.id)+"%"+self.nombre+"%"+self.cedula+"%"+self.cargo+"%"+self.departamento+"%"+self.sueldo


'''
    CREACION DE FUNCIONES
'''

def contarCargo():
    f = open("archivos/cargo.txt")
    contador = 0
    for _ in f:
        contador += 1
    f.close()

    return contador


def contarDepto():
    f = open("archivos/depto.txt")
    contador = 0
    for _ in f:
        contador += 1
    f.close()

    return contador



def contarEmpleado():
    f = open("archivos/empleado.txt")
    contador = 0
    for _ in f:
        contador += 1
    f.close()

    return contador


def leerCargo():
    os.system("cls")
    print("\tINGRESO DE CARGOS\n")

    _id = contarCargo() + 1
    _descripcion = input("Cargo: ")
    if(len(_descripcion) <= 20 and len(_descripcion) > 0):

        cargo = Cargo(_id, _descripcion)

        f = open("archivos/cargo.txt", "a")
        f.write(cargo.getCargo()+"\n")
        print("\nSe agrego el cargo satisfactoriamente!")
        f.close()
    else:
        print("Ingreso inválido, ingrese nuevamente (1-20 caracteres)")

def leerDepto():
    os.system("cls")
    print("\tINGRESO DE DEPARTAMENTOS\n")
    _id = contarDepto() + 1
    _descripcion = input("DESCRIPCION: ")
    if(len(_descripcion) >= 5 and len(_descripcion) <= 20):

        depto = Depto(_id, _descripcion)

        f = open("archivos/depto.txt", "a")
        f.write(depto.getDepto()+"\n")
        print("\nSe agrego la departamento satisfactoriamente!")
        f.close()
    else:
        print("Ingreso inválido, ingrese nuevamente (5-20 caracteres)")


def buscarCargo(_id):
    try:
        f = open("archivos/cargo.txt")
        cargo = None

        for linea in f:
            _lectura = linea.split("%")
            if int(_lectura[0]) == _id:
                cargo = Cargo(int(_lectura[0]), _lectura[1])

        f.close()
        return cargo
    except FileNotFoundError:
        print("No se encontró el archivo")

def mostrarCargos():
    try:
        f = open("archivos/cargo.txt")
        cargo = None
        print("*************LISTADO DE CARGOS*************\nCódigo  Descripción")
        for linea in f:
            _lectura = linea.split('%')
            print("{}       {}".format(_lectura[0], _lectura[1]))
        print("*******************************************")
        f.close()
    except FileNotFoundError:
        print("No se encontró el archivo")

def ingresarCargo(_id):
    while validarCargo(_id):
        print("El código {} no existe, ingrese nuevamente".format(_id))
        _id = int(input("   INGRESE EL CÓDIGO DEL CARGO: "))
    
    return buscarCargo(_id).descripcion

def validarCargo(_id):
    try:
        f = open("archivos/cargo.txt")

        for linea in f:
            _lectura = linea.split("%")
            if int(_lectura[0]) == _id:
                return False
            else:
                bandera = True
        f.close()
        return bandera
    except FileNotFoundError:
        print("No existe el archivo")

def ingresarDepto(_id):
    while validarDepto(_id):
        print("El código {} no existe, ingrese nuevamente".format(_id))
        _id = int(input("INGRESE EL CÓDIGO DEL DEPARTAMENTO: "))

    return buscarDepto(_id).descripcion

def validarDepto(_id):
    try:
        f = open("archivos/Depto.txt")
        
        for linea in f:
            _lectura = linea.split("%")
            if int(_lectura[0]) == _id:
                return False
            else:
                bandera = True
        f.close()
        return bandera
    except FileNotFoundError:
        print("No existe el archivo")

def validarNombre(nombre):
    while (len(nombre) < 3 or len(nombre) > 20):
        print("Ingreso incorrecto, ingrese nuevamente (3-20 caracteres)")
        nombre = input("   NOMBRE: ")
    return nombre

def validarCedula(cedula):
    while (len(cedula) != 10 or not cedula.isdigit()):
        print("Ingreso incorrecto, ingrese nuevamente (10 digitos)")
        cedula = input("   CEDULA: ")
    return cedula

def ingresarSueldo(sueldo):
    while validarSueldo(sueldo):
        print("Ingreso incorrecto, ingrese nuevamente")
        sueldo = input(" SUELDO: ")
    
    return sueldo

def validarSueldo(sueldo):
    try:
        float(sueldo)
        return False
    except:
        return True

def leerEmpleado():
    os.system("cls")
    print("\tINGRESO DE EMPLEADO\n")
    _id = contarEmpleado() + 1
    _nombre = validarNombre(input("   NOMBRE: "))
    _cedula = validarCedula(input("   CEDULA: "))
    _cargo = ingresarCargo(int(input("   INGRESE EL CÓDIGO DEL CARGO: ")))
    _departamento = ingresarDepto(int(input("INGRESE EL CÓDIGO DEL DEPARTAMENTO: ")))
    _sueldo = ingresarSueldo(input(" SUELDO: "))

    opcion = input("\nEsta seguro de grabar el registro? (s/n): ")

    if opcion in ['s', 'S']:
        empleado = Empleado(_id, _nombre, _cedula, _cargo.strip('\n'), _departamento.strip('\n'), _sueldo)

        f = open("archivos/empleado.txt", "a")
        f.write(empleado.getEmpleado()+"\n")
        print("\nSe agrego al empleado satisfactoriamente!")
        f.close()
    else:
        print("\nRegistro eliminado!")


def buscarEmpleado(_id):
    try:
        f = open("archivos/empleado.txt")
        empleado = None

        for linea in f:
            _lectura = linea.split("%")
            if int(_lectura[0]) == _id:
                empleado = Empleado(
                    int(_lectura[0]), _lectura[1], _lectura[2], _lectura[3], _lectura[4])
        f.close()
        return empleado
    except FileNotFoundError:
        print("No se encontró el archivo")

def mostrarEmpleados():
    try:
        f = open("archivos/empleado.txt")
        cargo = None
        print("*************LISTADO DE EMPLEADOS*************\nCódigo  Nombre               Cédula       Cargo        Departamento           Sueldo")
        for linea in f:
            _lectura = linea.split('%')
            print("{}       {}      {}      {}      {}      {}".format(_lectura[0], _lectura[1], _lectura[2], _lectura[3], _lectura[4], _lectura[5]))
        print("*******************************************")
        f.close()
    except FileNotFoundError:
        print("No se encontró el archivo")

def buscarDepto(_id):
    try:
        f = open("archivos/Depto.txt")
        depto = None

        for linea in f:
            _lectura = linea.split("%")
            if int(_lectura[0]) == _id:
                depto = Depto(int(_lectura[0]), _lectura[1])

        f.close()
        return depto
    except FileNotFoundError:
        print("No se encontré el archivo")

def mostrarDepto():
    try:
        f = open("archivos/Depto.txt")
        depto = None
        print("*************LISTA DE DEPARTAMENTOS*************\nCódigo     Departamento")
        for linea in f:
            _lectura = linea.split('%')
            print("{}          {}".format(_lectura[0], _lectura[1]))
        print("************************************************")
        f.close()
    except FileNotFoundError:
        print("No se encontré el archivo")

def ingresarOpcion(opcion):
    while not opcion.isdigit():
        print("Ingrese únicamente dígitos")
        opcion = input("Selecciona una opcion: ")
        
    return int(opcion)

'''
    CREACION DE MENUS ITERACTIVOS
'''

while True:
    os.system('cls')
    print("=========================================")
    print("  Bienvenido al crud de ficha personal   ")
    print("=============Menu Principal==============")
    print("\t[1] Cargo                              ")
    print("\t[2] Departamento                       ")
    print("\t[3] Empleados                          ")
    print("\t[0] Salir                              ")
    print("=========================================")

    opcion = ingresarOpcion(input("Selecciona una opcion: "))
    if(opcion == 1):
        while True:
            os.system('cls')
            print("=========================================")
            print("       Mantenimiento de cargos           ")
            print("=========================================")
            print("\t[1] Ingreso                            ")
            print("\t[2] Consulta                           ")
            print("\t[0] Salir                              ")
            print("=========================================")

            opcion = ingresarOpcion(input("Selecciona una opcion: "))
            if(opcion == 1):
                leerCargo()
            elif (opcion == 2):
                mostrarCargos()
            elif (opcion == 0):
                break
            else:
                print("\nPor favor, selecciona las opciones correctas")
            os.system('pause')
    elif (opcion == 2):
        while True:
            os.system('cls')
            print("=========================================")
            print("    Mantenimiento de departamentos       ")
            print("=========================================")
            print("\t[1] Ingreso                            ")
            print("\t[2] Consulta                           ")
            print("\t[0] Salir                              ")
            print("=========================================")

            opcion = ingresarOpcion(input("Selecciona una opcion: "))
            if(opcion == 1):
                leerDepto()
            elif (opcion == 2):
                mostrarDepto()
            elif (opcion == 0):
                break
            else:
                print("\nPor favor, selecciona las opciones correctas")
            os.system('pause')
    elif (opcion == 3):
        while True:
            os.system('cls')
            print("=========================================")
            print("       Mantenimiento de empleados        ")
            print("=========================================")
            print("\t[1] Ingreso                            ")
            print("\t[2] Consulta                           ")
            print("\t[0] Salir                              ")
            print("=========================================")

            opcion = ingresarOpcion(input("Selecciona una opcion: "))
            if(opcion == 1):
                leerEmpleado()
            elif (opcion == 2):
                mostrarEmpleados()
            elif (opcion == 0):
                break
            else:
                print("\nPor favor, selecciona las opciones correctas")
            os.system('pause')
    elif (opcion == 0):
        print("\nGracias por usar el programa!")
        break
    else:
        print("\nPor favor, selecciona las opciones correctas")

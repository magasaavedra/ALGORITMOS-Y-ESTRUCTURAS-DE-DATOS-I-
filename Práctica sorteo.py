"""
-----------------------------------------------------------------------------------------------
Título:
Fecha:
Autor:
Descripción:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
#----------------------------------------------------------------------------------------------
import random

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def agregarAmigoAlSorteo(_path):
    ## Desarrolla aquí el código ##
    ## Esta función permite agregar un amigo al archivo
    ## (el string a almacenar debe quedar así "nombre;apellido;dni;num1;num2;num3;num4;num5;num6")
    cadenaCaracter = ""
    mensajePedido = "Ingresar numero/s "
    mensajeError = "El valor ingresado no es un entero"
    
    try:
        archivo = open(_path, mode="a", encoding="utf-8")
        nombre = input("nombre ")
        apellido = input("apellido ")
        dni = validarEntero(mensajePedido, mensajeError)
        cadenaCaracter = nombre + ";" + apellido + ";" +  str(dni)
        for i in range(6):
            num = validarEntero(mensajePedido, mensajeError)
            cadenaCaracter = cadenaCaracter + ";" + str(num)
        archivo.write(cadenaCaracter)
    except:
        pass
    finally:
        try:
            archivo.close()
        except: 
            pass 
    

def validarEntero(_mensajePedido, _mensajeError):
    ## Desarrolla aquí el código ##
    ## Esta función se utilizará en las funciones agregarAmigosAlSorteo y repartirPozo
    ## para validar que los valores ingresados (dni y numeros elegidos en el primer caso y monto en el segundo) sean enteros
    ## utilizar un manejador de excepciones 
    ## No es necesario validar que el número jugado esté entre 0 y 90, asumiremos que el usuario siempre ingresa correctamente esos números
    while True:
        try:
            valor = int(input(_mensajePedido))
            break
        except ValueError:
            print(_mensajeError)
    return valor



def realizarSorteo(_path):
    ## Desarrolla aquí el código ##
    """Y la segunda parte de la función abrirá el archivo amigos.txt y buscará dentro de las líneas si hay coincidencia entre
los números apostados[3] a [8] y sorteados.
Ganarán sólo quienes con sus 6 números acierten al menos 2 de los números sorteados. De ser así, almacenará el
nombre y apellido de los ganadores como un solo string dentro de la variable listaGanadores."""
    _numerosSorteados = sortearNumeros()
    _listaGanadores = []
    coincidencia = 0
    try: 
        archivo = open(_path, mode="r", encoding="utf-8")
        for linea in archivo:
            contenido = linea.split(";")
            for j in range(int(contenido[3]), int(contenido[8])):
                if int(contenido[j]) in _numerosSorteados:
                    coincidencia +=1
                j +=1
            if coincidencia >= 2:
                ganador = contenido[0] + " " + contenido[1]
                _listaGanadores.append(ganador)
        print(_numerosSorteados, end = " ")
        print(_listaGanadores, end= " ")

    except:
        pass
    finally: pass
    
    

def sortearNumeros():
    ## Desarrolla aquí el código ##
    ## Esta función crea una lista de 6 números aleatorios distintos
    _numerosSorteados = []
    while len(_numerosSorteados) < 6:
        n = random.randint(0,90)
        if n not in _numerosSorteados:
            _numerosSorteados.append(n)
    return _numerosSorteados



def repartirPozo(_listaGanadores):
    ## Desarrolla aquí el código ##
    ## Utilizar un manejador de excepciones si el pozo es vacante
    mensajePedido = "Ingrese un monto total de apuestas válido: "
    mensajeError = "El monto no es un número, intente de nuevo."
    monto = validarEntero(mensajePedido, mensajeError)
    ...
    

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables
#----------------------------------------------------------------------------------------------
numerosSorteados = sortearNumeros()
listaGanadores = []
path = r"C:\Users\magas\Downloads\parcial2\sorteados.txt" # IMPORTANTE!!!!! usa esta variable string para el path completo del archivo amigos.txt

# Bloque de menú
#----------------------------------------------------------------------------------------------
while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Cargar Amigo al sorteo")
        print("[2] Sortear!")
        print("[3] Mostrar ganadores!")
        print("[0] Salir del programa")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in ("0","1","2","3"): # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para continuar.")

    if opcion == "0": # Opción salir del programa
        exit()

    elif opcion == "1":   # Opción Cargar Amigo al sorteo
        agregarAmigoAlSorteo(path)
        
    elif opcion == "2":   # Sortear!
        realizarSorteo(path)
#        numerosSorteados, listaGanadores = realizarSorteo(path)
#        print('Números sorteados: ', numerosSorteados)
#        print('Ganadores: ', listaGanadores)

    elif opcion == "3":   # Vaciar lista de amigos
        if len(numerosSorteados) > 0:
            repartirPozo(listaGanadores)
        else:
            print("Primero realice el sorteo!")

    print()
    input("Presione ENTER para continuar.")

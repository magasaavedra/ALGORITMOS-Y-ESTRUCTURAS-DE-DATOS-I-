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
...

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def diasEnElMes(_mes): 
    ##### FUNCION DADA. NO MODIFICAR #####
    # Esta función que ya está programada y devuelve la cantidad de días en el mes
    if _mes in(4,6,9,11):
        _dias = 30
    elif _mes == 2:
        _dias = 28
    else:
        _dias = 31 
    return _dias
    ##### FUNCION DADA. NO MODIFICAR #####


def pedirEntero(_mensajeInput, _mensajeError):
    # Esta función sirve para pedir un valor y validar si es un múmero entero utilizando excepciones
    # Si no se ingresa nada o si se ingresa un valor que no se pueda convertir a un entero entonces
    # se debe mostrar el mensaje de error y volver a pedir el valor
    ##### DESARROLLA DESDE AQUI #####
    while True :
        
        try:
            valor = int(input(_mensajeInput))
            break
                
        except ValueError as detalle:
            print(_mensajeError, detalle)
    return valor


def mostrarChoferes(_pathChoferes):
    # Esta función sirve simplemente para mostrar el listado de choferes
    # Será llamada desde dentro de otras funciones justo antes que se solicite la selección de un chofer
    # Mostrará el listado de choferes para ayudar a la posterior carga de códigos
    ##### DESARROLLA DESDE AQUI #####
    a = open(_pathChoferes, mode="r", encoding="utf-8")
    try:
        for linea in a:
            print(linea)
    except FileNotFoundError:
        print("Archino no encontrado")
    finally:
        try:
            a.close
        except:
            pass
    return


def reservarViaje(_pathReservas, _pathChoferes, _ciudadesDestino):
    # Esta función permite agregar reservas de viajes al archivo de texto (delimitado por tabulación)
    #
    # La estructura de registro en el archivo es la siguiente:
    # nombrePasajero TAB diaReserva TAB mesReserva TAB ciudadDestino TAB codigoChofer
    # A saber:
    #   - nombrePasajero : Es un string
    #   - diaReserva: Es un entero (utilizar pedirEntero), además validar aquí que no sea un número que se haya almacenado en diasOcupados
    #   - mesReserva: Es un entero (utilizar pedirEntero), además validar aquí que esté entre 1 y 12
    #   - ciudadDestino: Es un string
    #   - codigoChofer: Es un entero (utilizar pedirEntero)

    cadenaCaracter = "" # En esta cadena se concatenará el texto a cargar en el archivo
    mensajeInput = "Ingrese el día/mes"   # Variable modificable para utilizar como mensaje de entrada cada vez que se tenga que llamar a la función pedirEntero
    mensajeError = "Dia ingresado inválido"   # Variable modificable para utilizar como mensaje de error cada vez que se tenga que llamar a la función pedirEntero
    diasOcupados = []   # Lista en donde almacenar los días con reserva asignada tomando los datos desde el archivo y para el mes ingresado 
    ##### DESARROLLA DESDE AQUI #####
    a = open(_pathReservas, mode="a", encoding="utf-8")
    try:
        nombre = input("Ingresar apellido y nombre del pasajero").upper()
        cadenaCaracter = nombre
        while True:
            dia = pedirEntero(mensajeInput, mensajeError)
            if dia not in diasOcupados:
                cadenaCaracter = cadenaCaracter + "\t" + str(dia)
                break
            else:
                print("Error!, dia reservado")
        while True:
            mes = pedirEntero(mensajeInput, mensajeError)
            if mes > 0 and mes < 13:
                cadenaCaracter = cadenaCaracter + "\t" + str(mes)
                break
            else:
                    print("Error!, mes erróneo")
        while True:
            ciudad = input("Ingrese ciudad de destino").upper()
            if ciudad in _ciudadesDestino:
                cadenaCaracter = cadenaCaracter + "\t" + str(ciudad)
                break
            else:
                print("La ciudad mencionada no está disponible")
        while True:
            codigoChofer = pedirEntero(mensajeInput, mensajeError)
            if codigoChofer == 100 or codigoChofer == 200 or codigoChofer == 300 or codigoChofer == 400 or codigoChofer == 500:
                cadenaCaracter = cadenaCaracter + "\t" + str(codigoChofer)
                break
            else:
                print("Código de chofer no válido")
        a.write(cadenaCaracter)    
    except:
        print("Archino no encontrado")
    finally:
        try:
            a.close
        except:
            pass
    return


def mostrarPasajerosSegunChofer(_pathReservas, _pathChoferes):
    ## Esta función muestra todos los pasajeros según un chofer ingresado

    pasajeros = set()  # AYUDA! Conjunto vacío preparado para cargar los pasajeros del chofer seleccionado
    ##### DESARROLLA DESDE AQUI #####
    mostrarChoferes(_pathChoferes)
    
    #pido el número de chofer validando que sea entero y que sea 100 o 200 o 300 o 400 o 500
    mensajeInput = "Ingresar el código del chofer "
    mensajeError = "Código no válido"
    
    f = open(_pathReservas, mode="r", encoding="utf-8")
    codigoChofer = pedirEntero(mensajeInput, mensajeError)
    if codigoChofer == 100 or codigoChofer == 200 or codigoChofer == 300 or codigoChofer == 400 or codigoChofer == 500:
        for linea in f:
            contenido = linea.split("\t")
            if contenido[4] == codigoChofer:     
                pasajeros.add(contenido[0])
        print(pasajeros)    

    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#-------------------------------------------------
pathReservas = r"C:\Users\magas\Downloads\parcial2\reservas.csv"
  # IMPORTANTE!!!!! usa esta variable string para el path completo del archivo base de reservas
pathChoferes = r"C:\Users\magas\Downloads\parcial2\choferes.txt" # IMPORTANTE!!!!! usa esta variable string para el path completo del archivo base de choferes
ciudadesDestino = ["ROMA", "MADRID", "LONDRES"]

#-------------------------------------------------
# Bloque de menú
#-------------------------------------------------
while True:
    while True:
        try:
            print()
            print("-------------------------------------------")
            print("MENÚ DEL SISTEMA")
            print("-------------------------------------------")
            print("[1] Reservar un Viaje")
            print("[2] Mostrar Pasajeros según Chofer")
            print("-------------------------------------------")
            print("[0] Salir")
            print("-------------------------------------------")
            print()
            opcion = input("Seleccione una opción: ")
            if opcion in ["0","1","2"]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        except ValueError:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    if opcion == "0":
        exit()

    elif opcion == "1":  
        reservarViaje(pathReservas, pathChoferes, ciudadesDestino)
        
    elif opcion == "2":   
        mostrarPasajerosSegunChofer(pathReservas, pathChoferes)
        

    print()
    input("Presione ENTER para volver al menú.")




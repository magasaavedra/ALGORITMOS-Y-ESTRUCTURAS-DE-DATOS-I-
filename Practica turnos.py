"""
-----------------------------------------------------------------------------------------------
Título:
Fecha:
Autor: Magali Saavedra
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
    # Esta función que ya está programada devuelve la cantidad de días en el mes (no modificar!!)
    if _mes == 4 or _mes == 6 or _mes == 9 or _mes == 11:
        _dias = 30
    elif _mes == 2:
        _dias = 28
    else:
        _dias = 31 
    return _dias


def pedirEntero(_mensajeInput, _mensajeError):
    # Esta función sirve para pedir un valor y validar si es un múmero entero utilizando excepciones
    # Si no se ingresa nada o si se ingresa un valor que no se pueda convertir a un entero entonces
    # se debe mostrar el mensaje de error y volver a pedir el valor

    ##### DESARROLLA DESDE AQUI #####
    while True:
        try:
            valor = int(input(_mensajeInput))
            break
        except ValueError:
            print(_mensajeError)
    return valor


def reservarTurno(_path, _codigoSedes, _nombreSedes):
    # Esta función permite agregar turnos de pacientes al archivo
    #
    # La estructura de registro en el archivo es la siguiente:
    # nombre;mes;dia;codigoSede;nombreSede
    # A saber:
    #   - nombre: nombre del paciente
    #   - mes: es un entero (utilizar pedirEntero), además validar aquí que esté entre 1 y 12
    #   - dia: es un entero (utilizar pedirEntero), además validar aquí que no sea un número que se haya almacenado en diasOcupados
    #   - codigoSede: es un entero (utilizar pedirEntero), además validar aquí que sea un código válido de la lista _codigoSedes
    #   - nombreSede: es una cadena de caracteres que se asigna automáticamente dado que se usa la misma posición _codigoSedes dentro de _nombreSedes

    cadenaCaracter = "" # En esta cadena se concatenará el texto a cargar en el archivo
    mensajeInput = ""   # Variable modificable para utilizar como mensaje de entrada cada vez que se tenga que llamar a la función pedirEntero
    mensajeError = "error! ingrese un valor entero"   # Variable modificable para utilizar como mensaje de error cada vez que se tenga que llamar a la función pedirEntero
    diasOcupados = []   # Lista en donde almacenar los días con turnos asignados tomando los datos desde el archivo para el mes correspondiente 
    
    ##### DESARROLLA DESDE AQUI #####
    archivo = open(_path, mode="a", encoding="utf-8")
    try:
        while True:
            nombre = input("Ingrese nombre del paciente ").upper()
            cadenaCaracter = nombre + ";"
            break
        while True:
            mensajeInput = "Ingrese el mes del turno (en número) "
            mes = pedirEntero(mensajeInput, mensajeError)
            if mes > 0 and mes < 13:
                cadenaCaracter = cadenaCaracter + str(mes) +  ";"
                break
            else:
                print("Mes ingresado incorecto")
        while True:
            mensajeInput = "Ingrese el día del turno (en número) "
            dia = pedirEntero(mensajeInput, mensajeError)
            if dia not in diasOcupados:
                cadenaCaracter = cadenaCaracter + str(dia) +  ";"
                diasOcupados.append(dia)
                break
            else:
                print("El día solicitado se encuenta ocupado.")
        while True:
            mensajeInput = "Ingrese el código de la sede "
            codigoSede = pedirEntero(mensajeInput, mensajeError)
            if codigoSede in _codigoSedes:
                for i, e in enumerate(codigoSedes):
                    if e == codigoSede:
                        cadenaCaracter = cadenaCaracter + str(codigoSede) +  ";" + nombreSedes[i]
                break
            else:
                print("Código ingresado incorecto")
        
        archivo.write(cadenaCaracter)

    except FileNotFoundError:
        print("Error, no se encuentra el archivo")
    finally:
        try:
            archivo.close()
        except:
            pass
    
    
    
def contarTurnosPorSede(_path, _codigoSedes, _nombreSedes):
    ## Esta función imprime la cantidad de turnos por cada sede

    turnosPorSede = [0,0,0,0,0] # Utiliza esta lista para almacenar los turnos por sede respetando el orden de sedes, es decir [10, 115, 120, 25, 30]
    belgrano = caballito = sanTelmo = palermo = recoleta = 0
    ##### DESARROLLA DESDE AQUI #####
    try:
        archivo = open(_path, mode="r", encoding="utf-8")
        for i in archivo:
            contenido = i.split(";")
            if int(contenido[3]) == _codigoSedes[0]:
                belgrano +=1
            if int(contenido[3]) == _codigoSedes[1]:
                caballito +=1
            if int(contenido[3]) == _codigoSedes[2]:
                sanTelmo +=1
            if int(contenido[3]) == _codigoSedes[3]:
                palermo +=1
            if int(contenido[3]) == _codigoSedes[4]:
                recoleta +=1

        turnosPorSede = [belgrano, caballito, sanTelmo, palermo, recoleta]
        for j in range(len(turnosPorSede)): 
            print(f"La cantidad de turnos de {_nombreSedes[j]} es: {turnosPorSede[j]}")
            j+=1
    except FileNotFoundError:
        print("Error, no se encuentra el archivo")
    finally:
        try:
            archivo.close()
        except:
            pass
    
        
    
def mostrarPacientesPorSede(_path, _codigoSedes, _nombreSedes):
    ## Esta funcion le pide al usuario el código de la sede que quiere ver e imprime los pacientes para dicha sede
    ## Si no hay pacientes arroja un mensaje de "No hay pacientes en dicha sede"

    ##### DESARROLLA DESDE AQUI #####
    pacientes = set()

    try:
        archivo = open(_path, mode="r", encoding="utf-8")
        codigoSede = int(input("Ingresar código de sede para imprimir listado de pacientes "))
        for i in archivo:
            contenido = i.split(";")
            if int(contenido[3]) == codigoSede:
                pacientes.add(contenido[0])
        print(pacientes)
    except:
        pass
    
    
        
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#-------------------------------------------------
path = r"C:\Users\magas\Downloads\parcial2\turnos.txt"  # IMPORTANTE!!!!! usa esta variable string para el path completo del archivo turnos.txt
# Las listas codigoSedes y nombreSedes contienen los únicos valores existentes para las sedes del centro médico
# Por ejemplo, a la Sede Belgrano le corresponde el código 10 y así...
codigoSedes = [10, 25, 30, 115, 120]
nombreSedes = ["Sede Belgrano", "Sede Caballito", "Sede San Telmo", "Sede Palermo", "Sede Recoleta"]


#-------------------------------------------------
# Bloque de menú
#-------------------------------------------------
while True:
    while True:
        try:
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("[1] Reservar turno")
            print("[2] Mostrar cantidad de turnos según sede")
            print("[3] Mostrar pacientes por sede")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            opcion = input("Seleccione una opción: ")
            if opcion in ["0","1","2","3"]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        except ValueError:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    if opcion == "0": # Opción: Salir del programa
        exit()

    elif opcion == "1":   # Opcion para la carga de turnos al archivo 
        reservarTurno(path, codigoSedes, nombreSedes)
        
    elif opcion == "2":   # Opción que muestra la cantidad de turnos según la sede
        contarTurnosPorSede(path, codigoSedes, nombreSedes)

    elif opcion == "3":   # Opción que muestra los pacientes por sede
        mostrarPacientesPorSede(path, codigoSedes, nombreSedes)
    
    print()
    input("Presione ENTER para volver al menú.")




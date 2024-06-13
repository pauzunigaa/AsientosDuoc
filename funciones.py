def anular_pasaje(asientos):
    # Solicitar el número del asiento a anular
    nroAsientoAAnular = int(input("Ingrese numero del asiento del pasaje a anular: "))
    if len(asientos[nroAsientoAAnular - 1])==0: # este if analiza si hay algo dentro de la lista que guarda la lista de ese asiento
        print(" No existe la compra de este pasaje ") # Entonces si el rango es igual a 0 es porque no existe la compra de ese pasaje 
    else:
        # Anular el asiento (vaciar la lista para indicar que está disponible)
        asientos[nroAsientoAAnular - 1] = []
        print(" Su pasaje ha sido eliminado con exito ")
        
        
def ver_Asiento_disponible(asientos): # Esta función visualiza asientos disponibles
    contadorFila = 0  # Contador para controlar la cantidad de asientos mostrados en cada fila

    # Recorrer los asientos
    for i in range(len(asientos)):
        if contadorFila == 0:
            print("|", end="\t")
        contadorFila = contadorFila + 1  # Incrementar el contador de fila
        # Mostrar el número del asiento si está disponible, de lo contrario mostrar 'X'
        if len(asientos[i]) == 0:  # Si la lista del asiento está vacía, está disponible
            print(i + 1, end="\t")  # Mostrar el número del asiento (i + 1 para ajustar a base 1)
        else:  # Si la lista del asiento no está vacía, está ocupado
            print("X", end="\t")  # Mostrar 'X' para indicar que el asiento está ocupado




        # Imprimir un salto de línea cada 6 asientos para organizar la vista en filas
        if contadorFila == 6:
            print("|")
            print("")  # Salto de línea
            contadorFila = 0  # Reiniciar el contador de fila
        # Imprimir una tabulación extra cada 3 asientos (simulando el pasillo)
        elif contadorFila == 3:
            print(end="\t\t")  # Tabulación extra para simular el pasillo

        if i ==29: # para crear la division entre pasajes normales y VIP
            print("|","_"*23,"\t\t\t","_"*22,"|")
            print()
            print("|","_"*23,"\t\t\t","_"*22,"|")
            print()

    print()  # Salto de línea final después de mostrar todos los asientos
    
def comprar_pasajes(asientos,precioAsientoVIP,precioAsientoNormal):
    # Solicitar el número de asiento y datos del pasajero
    print("Precio asientos:")
    print("Asiento normal (DESDE ASIENTO 1 AL 30): $", precioAsientoNormal)
    print("Asiento VIP ( DESDE ASIENTO 31 AL 42): $", precioAsientoVIP)
    nroAsiento = int(input("Ingrese numero asiento: "))

    if nroAsiento > 0 and nroAsiento <= 30:
        print("Seleccionaste asiento normal.")
        totalPasaje = precioAsientoNormal
    elif nroAsiento > 30 and nroAsiento <=42:
        print("Seleccionaste asiento vip")
        totalPasaje = precioAsientoVIP
        
    nombrePasajero = input("Ingrese nombre pasajero: ")
    while True: # validando rut
        try:
            rutPasajero = int(input("Ingrese rut pasajero (sin punto ni guión)): "))
            break
        except ValueError:
            print(" Ingrese solo números ")
            
    while True: # validando telefono
        try:
            telefonoPasajero = int(input("Ingrese teléfono pasajero : "))
            break
        except ValueError:
            print(" Ingrese solo números ")
            
    bancoPasajero = input("Ingrese banco pasajero (bancoDuoc / Otro) : ").lower()

    # Crear una lista con los datos del nuevo pasajero
    nuevoPasajero = [nombrePasajero, rutPasajero, telefonoPasajero, bancoPasajero]
    

    # Asignar los datos del pasajero al asiento correspondiente 
    asientos[nroAsiento - 1] = nuevoPasajero
    if bancoPasajero == "bancoduoc":
        descuento = totalPasaje*.15
    else:
        descuento = 0

    totalAPagar = totalPasaje - descuento

    print("El total a pagar es de $", totalAPagar)
    
    
def modificar_datos_pasajero(asientos):
    # Solicitar el número de asiento y el RUT del pasajero
    nroAsiento = int(input("Ingrese numero asiento: "))
    if len(asientos[nroAsiento - 1])==0: # si el largo es igual a 0, la lista esta vacia y el pasaje no existe
        print(" No registrado ")
    else: # el codigo se ejecutará solo si el pasaje existe o si el largo de la lista es distinta de 0
        
        rutPasajero = input("Ingrese rut pasajero (sin guiones ni puntos)): ")

        # Verificar que el RUT del pasajero coincida con el registrado en el asiento
        if asientos[nroAsiento - 1][1] == rutPasajero:
            print("RUT valido")

            while True:
                # Mostrar el menú de modificación de datos del pasajero
                print("****Modificar datos pasajero****")
                print("1. Modificar nombre pasajero")
                print("2. Modificar telefono pasajero")
                print("3. Salir")

                # Obtener la opción del usuario para modificar datos
                opcionMenuPasajero = int(input("Seleccione una opción: "))

                # Modificar el nombre del pasajero
                if opcionMenuPasajero == 1:
                    nuevoNombrePasajero = input("Ingrese el nuevo nombre del pasajero: ")
                    # Acceder a la lista del asiento y cambiar el nombre (índice 0 de la lista del asiento)
                    asientos[nroAsiento - 1][0] = nuevoNombrePasajero

                # Modificar el teléfono del pasajero
                elif opcionMenuPasajero == 2:
                    nuevoTelefonoPasajero = input("Ingrese el nuevo telefono del pasajero: ")
                    # Acceder a la lista del asiento y cambiar el teléfono (índice 2 de la lista del asiento)
                    asientos[nroAsiento - 1][2] = nuevoTelefonoPasajero

                # Salir del menú de modificación de datos del pasajero
                elif opcionMenuPasajero == 3:
                    print("Saliendo...")
                    break
                else:
                    # Opción no válida
                    print("Seleccione una opcion valida.")
        else:
            print("Rut no encontrado.")
from funciones import anular_pasaje,ver_Asiento_disponible,comprar_pasajes,modificar_datos_pasajero

# Lista de asientos inicializada con 42 listas vacías, representando cada asiento.
asientos = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

precioAsientoNormal = 78900
precioAsientoVIP = 240000
totalPasaje = 0

# Bucle infinito para mostrar el menú de opciones hasta que el usuario decida salir.
while True:
    # Mostrar el menú principal con las opciones disponibles.
    print("****VENTA PASAJES****")
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")

    # Obtener la opción del usuario
    opcionMenu = int(input("Seleccione una opción:"))

    # Opción 1: Ver asientos disponibles
    if opcionMenu == 1:
        ver_Asiento_disponible(asientos)
        
    # Opción 2: Comprar asiento
    elif opcionMenu == 2:
        ver_Asiento_disponible(asientos)
        comprar_pasajes(asientos,precioAsientoVIP,precioAsientoNormal)

    # Opción 3: Anular vuelo
    elif opcionMenu == 3:
        print("Anular vuelo")
        anular_pasaje(asientos)

    # Opción 4: Modificar datos de pasajero
    elif opcionMenu == 4:
        print("Modificar datos de pasajero")
        modificar_datos_pasajero(asientos)

    # Opción 5: Salir del programa
    elif opcionMenu == 5:
        print("Saliendo...")
        break  # Terminar el bucle infinito y salir del programa

    # Manejar cualquier otra opción no válida
    else:
        print("Por favor, seleccione una opción valida")

#Lista estudiantes
estudiantes = [
    {"nombre": "Juan", "nota1": 8, "nota2": 7},
    {"nombre": "Ana", "nota1": 5, "nota2": 6},
    {"nombre": "Luis", "nota1": 3, "nota2": 4}
]

opcion = 0
#Menú
while opcion != 4:
    print("------Menú------")
    print("1. Ver listado de estudiantes")
    print("2. Consultar condición de un estudiante")
    print("3. Ver promedio de un estudiante")
    print("4. Salir")

    try:
        opcion = int(input("Ingrese una opción: "))

        if opcion not in (1, 2, 3, 4):
            print("La opción ingresada está fuera de rango.")
            continue

    except ValueError:
        print("El valor ingresado no es válido.")
        continue

    if opcion == 1:
        pass

    elif opcion == 2:
        pass

    elif opcion == 3:
        pass

    elif opcion == 4:
        print("Saliendo del programa.")
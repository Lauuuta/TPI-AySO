#Lista estudiantes
estudiantes = [
    {"nombre": "Juan", "nota1": 8, "nota2": 7},
    {"nombre": "Ana", "nota1": 5, "nota2": 5},
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
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}, Nota 1: {estudiante['nota1']}, Nota 2: {estudiante['nota2']}")

    elif opcion == 2:
        nombre = input("Ingrese el nombre del estudiante: ")
        encontrado = False
        for estudiante in estudiantes:
            if estudiante["nombre"].lower() == nombre.lower():
                print(f"Notas: {estudiante['nota1']}, {estudiante['nota2']}")
                condicion = (estudiante["nota1"] + estudiante["nota2"]) / 2 
                if condicion >= 7:
                    print("Condición: Aprobado")
                else:
                    print("Condición: Reprobado")
                encontrado = True
                break
        if not encontrado:
            print("El estudiante no se encuentra en la lista.")

    elif opcion == 3:
        nombre = input("Ingrese el nombre del estudiante: ")
        encontrado = False
        for estudiante in estudiantes:
            if estudiante["nombre"].lower() == nombre.lower():
                promedio = (estudiante["nota1"] + estudiante["nota2"]) / 2
                print(f"El promedio de {estudiante['nombre']} es: {promedio}")
                encontrado = True
                break
        if not encontrado:
            print("El estudiante no se encuentra en la lista.")
    elif opcion == 4:
        print("Saliendo del programa.")
        
def area_rectangulo(a, b):
    return a * b


def area_triangulo(b, h):
    return (b * h) / 2


def area_circulo_sin_math(radio):
    pi = 3.1416
    return pi * radio ** 2


while True:
    print("\nMenú:")
    print("1. Calcular el área de un rectángulo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un círculo (sin math)")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        x = float(input("Ingresa la base del rectángulo: "))
        y = float(input("Ingresa la altura del rectángulo: "))
        rect_area = area_rectangulo(x, y)
        print("Área del rectángulo:", rect_area)

    elif opcion == "2":
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        tri_area = area_triangulo(base, altura)
        print("Área del triángulo:", tri_area)

    elif opcion == "3":
        radio = float(input("Ingresa el radio del círculo: "))
        circ_area = area_circulo_sin_math(radio)
        print("Área del círculo:", circ_area)

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida, por favor elige una opción del 1 al 4.")

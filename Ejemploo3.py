def area_rectangulo(a, b):
    return a * b


def area_triangulo(b, h):
    return (b * h) / 2


while True:
    print("\nMenú:")
    print("1. Calcular el área de un rectángulo")
    print("2. Calcular el área de un triángulo")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

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
        print("Saliendo...")
        break

    else:
        print("Opción inválida, elige una opción del 1 al 3.")

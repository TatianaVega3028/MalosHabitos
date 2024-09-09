def calcular(numero1, numero2, numero3):
    resultado = numero1 * numero2 + numero3
    return resultado

if __name__ == "__main__":
    factor1 = float(input("Ingrese factor 1: "))
    factor2 = float(input("Ingrese factor 2: "))
    factor3 = float(input("Ingrese factor 3: "))

    resultado = calcular(factor1, factor2, factor3)

    print(f"{factor1} * {factor2} + {factor3} = {resultado}")

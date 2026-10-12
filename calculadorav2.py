
def suma(a, b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a, b):
    return a * b
def divicion(a, b):
    if b == 0:
        return "error: no se puede dividir entre 0"
    return a / b
print("===MI CALCULADORA MAYOR V2 ===")
while True:
    print("\nMENU:")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. divicion")
    print("5. salir")
    opcion = input("elige una opcion (1-5): ")
    if opcion == "5":
        print("Gracias por usar la calculadora mayor!")
        break
    if opcion not in ["1", "2", "3", "4",]:
        print("opcion no valida, intenta de nuevo")
        continue
    try:
        num1 = float(input("ingresa primer numero"))
        num2 = float(input("ingrsa segundo numero"))
    except ValueError:
        print("error: tines que poner numeros en lugar de letras")
        continue
    if opcion == "1":
        print(f"Resultado: {suma(num1, num2)}")
    elif opcion == "2":
        print(f"resultado: {resta (num1, num2)}")
    elif opcion == "3":
        print(f"resultado: {multiplicacion(num1, num2)}")
    elif opcion == "4":
        print(f"resultado: {divicion(num1, num2)}")

def suma (a, b):
    return a + b
def resta (a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def divicion(a, b):
    if b == 0:
        return "error: no se puede dividir entre 0"
    return a / b
print("=== MI CALCULADORA MAYOR ===")
num1 = float(input("ingresa primer numero: "))
num2 = float(input("ingresa segundo numero: "))

print(f"\nResultado con {num1} y {num2}:")
print(f"suma: {suma(num1, num2)}")
print(f"resta: {resta(num1, num2)}")
print(f"multiplicacion: {multiplicacion(num1, num2)}")
print(f"divicion: {divicion(num1, num2)}")
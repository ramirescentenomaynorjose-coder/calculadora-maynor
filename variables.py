while True:
    print("/n---CALCULADORA DE MAYOR --- ")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("0. salir")
    opcion = int (input("elige una opcion: "))
    if opcion == 0:
        print("chao carlos eres un crak")
        break
    n1 =int(input("primer numero"))
    n2 = int(input("segundo numero"))
    if opcion == 1:
        print("resultado:", n1 + n2)
    elif opcion == 2:
        print("resultado:" ,n1 - n2)
    elif opcion == 3:
        print("resultado:", n1 * n2)
    elif opcion == 4:
        if n2 == 0:
            print("no se puede dividir entre cero")
        else:
            print("resultado:", n1 / n2)
    else:
        print("opcion no valida")



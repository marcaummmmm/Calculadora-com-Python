
print("\nCalculadora\n")

while True:
    n1 = input("Informe o primeiro número (ou 'sair' para encerrar): ")
    if n1.lower() == "sair":
        break

    operador = input("Informe o operador (+, -, *, /): ")
    if operador.lower() == "sair":
        break

    n2 = input("Informe o segundo número: ")
    if n2.lower() == "sair":
        break

    try:
        n1_float = float(n1)
        n2_float = float(n2)
    except ValueError:
        print("Por favor, insira números válidos.")
        continue

    if operador == "+":
        resultado = n1_float + n2_float
    elif operador == "-":
        resultado = n1_float - n2_float
    elif operador == "*":
        resultado = n1_float * n2_float
    elif operador == "/":
        if n2_float != 0:
            resultado = n1_float / n2_float
        else:
            print("Erro: divisão por zero.")
            continue
    else:
        print("Operador inválido. Use +, -, * ou /.")
        continue

    print(f"\nResultado: {resultado}\n")

print("\nCalculadora encerrada.\n")

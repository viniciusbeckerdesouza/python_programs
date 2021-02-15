x = float(input("Digite um nº: "))
y = float(input("Digite outro nº: "))
op = int(input("Escolha uma opção: 1- Adição, 2- Subtração, 3- Multiplicação, 4- Divisão, 5- Potenciação. "))

if op == 1:
    print(f"{x} + {y} = {x + y}")
elif op == 2:
    print(f"{x} - {y} = {x - y}")
elif op == 2:
    print(f"{x} x {y} = {x * y}")
elif op == 4:
    print(f"{x} ÷ {y} = {x / y}")
else:
    print(f"{x} ^ {y} = {x ** y}")
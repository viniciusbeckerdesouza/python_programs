print('******************************')
print('*  Jogo    da   adivinhação  *')
print('******************************')

import random

num_secreto = random.randint(0, 100)

tentativa = 5
while tentativa <= 5 and tentativa > 0:
    num = int(input("Chute um nº de 1 a 100: "))
    if num == num_secreto:
        print(f"Você acertou! {num} é o nº secreto! :)")
        break
    else:
        print("Tente de novo")
        print(f"Restam {tentativa - 1} chances.")
        tentativa -= 1

print(f"O número secreto é {num_secreto}")
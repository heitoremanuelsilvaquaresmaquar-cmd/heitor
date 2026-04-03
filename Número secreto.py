import random

numero_secreto = random.randint(1, 20)

for tentativa in range(1, 6):
    palpite = int(input("Tentativa " + str(tentativa) + ": Adivinhe o número de 1 a 20: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")

    if tentativa == 5:
        print("Não há mais tentativas. O número secreto era " + str(numero_secreto))
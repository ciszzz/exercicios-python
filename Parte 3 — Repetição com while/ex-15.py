numero = int(input("Digite um número: "))

quantidade = 0

while numero != 0:
    if numero > 0:
        quantidade = quantidade + 1
    numero = int(input("Digite outro número: "))


print("Você digitou " + str(quantidade) + " números positivos.")
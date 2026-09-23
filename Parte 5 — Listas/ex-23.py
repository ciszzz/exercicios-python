numeros = [67, 42, 41, 13, 22]

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("O maior número é:", maior)
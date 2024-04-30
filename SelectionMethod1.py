

import random
import time

numb = [random.randint(2, 36) for _ in range(8)]
print("Lista de numeros aleatorios: ")
print(numb)
print(" ")
time.sleep(2.5)

primes = []

powers = []

def es_primo(numb):
    if numb <= 1:
        return False
    elif numb <= 3:
        return True
    elif numb % 2 == 0 or numb % 3 == 0:
        return False
    i = 5
    while i * i <= numb:
        if numb % i == 0 or numb % (i + 2) == 0:
            return False
        i += 6
    return True

def siguiente_primo(numb):
    while True:
        numb += 1
        if es_primo(numb):
            return numb

for n in numb:
    if es_primo(n):
        primes.append(n)
    else:
        primes.append(siguiente_primo(n))

print("Lista de numeros primos: ")
print(primes)
print(" ")
time.sleep(2.5)

def elevar_a_n():
    for i in primes:
        n = random.randint(1, 3)
        power = i ** n
        powers.append(power)
    return powers

powers = elevar_a_n()

print("Lista de potencias primas: ")
print(powers)
print(" ")
time.sleep(2.5)

def selection_sort(powers):
    n = len(powers)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if powers[min_idx] > powers[j]:
                min_idx = j
        powers[i], powers[min_idx] = powers[min_idx], powers[i]

selection_sort(powers)
print("Lista ordenada usando el método de Selección:")
for i in range(len(powers)):
    print(powers[i], end=" ")
print(" ")
time.sleep(2.5)
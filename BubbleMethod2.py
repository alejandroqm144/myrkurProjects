

import random
import time

numb = [random.randint(2, 100) for _ in range(8)]
print("Lista original de numeros aleatorios: ")
print(numb)
print(" ")
time.sleep(2.5)

def bubble_sort(numb):
    n = len(numb)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if numb[j] > numb[j + 1]:
                numb[j], numb[j + 1] = numb[j + 1], numb[j]
    return numb

n = bubble_sort(numb)

print("Lista ordenada por metodo de Burbuja: ")
print(n)
print(" ")
time.sleep(2.5)
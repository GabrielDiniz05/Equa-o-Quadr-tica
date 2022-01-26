import math


a = None
b = None
c = None
x1 = None
x2 = None
delta = None


print("-" * 30)
print("Bem_Vindo(a) ao programa de calculo de equação do 2 grau!")
print("-" * 30)
print("A equação de 2º grau consiste na formula Ax² + Bx + C")
print("Insira os valores de A, B e C.")

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))


def calc_delta(a, b, c):
    delta = (b * b) - 4 * a * c
    return delta


def calc_x1(a, b, delta):
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    return x1


def calc_x2(a, b, delta):
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x2


delta = calc_delta(a, b, c)
x1 = calc_x1(a, b, delta)
x2 = calc_x2(a, b, delta)


print("-" * 30)
print("Valores:")
print(f"A: {a}")
print(f"B: {b}")
print(f"C: {c}")
print(f"DELTA: {delta}")
if delta < 0:
    print("O DELTA é negativo (DELTA < 0), por isso não tem raíz REAL!")
else:
    print(f"X1: {x1}")
    print(f"X2: {x2}")
print("Obrigado por usar o programa!")
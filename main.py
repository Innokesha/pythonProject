#Задание № 1
def is_prime(num):
     for i in range(2, num // 3):
         if num % i == 0:
             return False
     return True
print(is_prime(int(input("Введите число"))))

#Задание № 2
def get_season(a):
    seas = {"Зима": (1, 2, 12),
            "Весна": (3, 4, 5),
            "Лето": (6, 7, 8),
            "Осень": (9, 10, 11)}
    for key in seas.keys():
        while a in seas[key]:
            return(key)
print(get_season(int(input())))

#Задание № 3 (Только способом Евклида. Ну и math)
def gcd(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:    # Эту часть кода(Начинающуюся с if a == 0) можно заменить на return a + b, так как одно из заначений
        return b  # будет равно нулю
    if b == 0:
        return a
c = int(input("Введите первое число:"))
d = int(input("Введите второе число:"))
print(gcd(c, d))

import math

def gcd(a,b):
    return math.gcd(a, b)
c = int(input())
d = int(input())
print(gcd(c, d))



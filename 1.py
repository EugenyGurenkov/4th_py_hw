# Вычислить число c заданной точностью d

# Пример:

# - при d = 3, π = 3.141

a = int(input('Сколько знаков после запятой числа π должно быть: '))
pi = 0

for n in range(0, 100):
    result = round((1/16**n) * ((4/(8*n+1)) - (2/(8*n+4)) - (1/(8*n+5)) - (1/(8*n+6))), a)
    pi += result

print(pi)
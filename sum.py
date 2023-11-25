numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]


def suma(numeros):
    for i in numeros:
        if i % 2 == 0:
            print(f"{i} es par")
        else:
            print(f"{i} no es par")


suma(numeros)

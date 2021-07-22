#  Encontrar o maior número entre três números
#
# Desafio: Escreva um programa que receba três números e encontre o maior dentre eles, sem utilizar rotinas builtin (por exemplo, rotina max do Python).


def retornaMaiorNumero(num1, num2, num3):
    arrNumero = num1, num2, num3
    return(sorted(arrNumero)[len(arrNumero)-1])


if __name__ == "__main__":
    num = retornaMaiorNumero(22,30,10)
    print(num)
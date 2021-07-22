#  Encontrar o maior número entre três números
#
# Desafio: Escreva um programa que receba três números e encontre o maior dentre eles, sem utilizar rotinas builtin (por exemplo, rotina max do Python).


def retornaMaiorNumero(num1, num2, num3):
    arrNumero = num1, num2, num3
    return(sorted(arrNumero)[len(arrNumero)-1])

def retornaMaiorNumeroV2(*num):
    return(sorted(num)[len(num)-1])


if __name__ == "__main__":
    num = retornaMaiorNumero(22,30,10)
    print("1.Maior Número V1: {}".format(num))

    num2 = retornaMaiorNumeroV2(22,30,10)   # Recebe qualquer quantidade de números(parâmetros).
    print("2.Maior Número V2: {}".format(num2))

    num2 = retornaMaiorNumeroV2(22,30,10,50,2,5)
    print("3.Maior Número V2: {}".format(num2))
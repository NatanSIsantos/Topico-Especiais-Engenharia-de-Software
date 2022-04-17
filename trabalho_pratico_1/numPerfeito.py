'''
OBS: Este programa é inspirado no problema 1164 do URI

Este programa serve para testar se um número é perfeito.
Um número perfeito é aquele cuja soma de seus divisores
positivos (exluindo ele mesmo) é igual a ele. Por exemplo:
O número perfeito 6 pode ser encontrado pela soma de seus
divisores 1 + 2 + 3.
'''
def numPerfeito(num):
    soma = 0

    if(num < 1 or num > 10 ** 8): # Verifica se o valor pertence ao intervalo
        return("Entrada Inválida")


    for i in range(1,(num//2)+1):# Testa divisões até o maior divisor possível
        if num % i ==0:          # Verica se o numero testado é um divisor
            soma +=i             # Incrementa o divisor ao somátorio final
    if soma != num:              # Ao fim caso não seja perfeito
        return("nao eh perfeito")# Saída negatica
    else:                        # Se for perfeito
        return("eh perfeito")    # Saída positiva

'''
# Número de testes
qtdNumeros = int(input())
# Laço de testes
for a in range (qtdNumeros):
    # Chamada de teste da função
    numPerfeito(int(input()))
'''
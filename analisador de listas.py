from time import sleep
from datetime import datetime
from random import shuffle


lista, continuar, traços, opções = [], 'l', '-' * 70, 0
cores = ('\033[m', '\033[31m', '\033[32m', '\033[33m', '\033[35m', '\033[36m')

pessoas = int(input('Digite a quantidade de pessoas que você quer colocar na lista: '))
sleep(1)
print(traços)
for cont in range(0, pessoas):
    nome = str(input(f'{cores[4]}Nome da pessoa: {cores[0]}')).title()
    print(traços)
    sleep(0.5)
    lista.append(f'{nome}')
while opções == 0 or opções > 4 or continuar == 'S': 
    opções = int(input(f'''\nLista de opções\n
{cores[1]}[1] Nomes em Ordem Alfabética
{cores[2]}[2] Contando quantas letras tem em uma palavra
{cores[3]}[3] Sortear nomes da lista
\n{cores[5]}Digite a opção que você prefere:{cores[0]} '''))
    sleep(1)
    print(traços)
    if opções == 1:
        lista.sort()
        print(f'Aqui está a lista em ordem alfabética: {cores[4]}{lista}{cores[0]}')
        sleep(1)
        print(traços)
    elif opções == 2:
        for p in lista:
            print(f'O nome {cores[2]}{p}{cores[0]} possuí {cores[5]}{len(p)}{cores[0]} letras')
            sleep(1)
            print(traços)
    elif opções == 3:
        shuffle(lista)
        print(f'Com o sorteio a ordem da lista atual será {cores[3]}{lista}{cores[0]}')
        sleep(1)
        print(traços)
    else:
     print('Número incorreto')
    continuar = str(input('Deseja testar mais funcionalidades? [S/N] ')).upper().strip()[0]
    sleep(1)
    print(traços)
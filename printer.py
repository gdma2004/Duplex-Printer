import PyPDF2, os, time
from PyPDF2 import PdfFileReader, PdfFileWriter
from typing import Sequence
from os import path



# PATH

os.system('sudo clear')

print('######## DUPLEX PYTHON PRINTER #########\n')
local = str(input('Indique a localização do seu arquivo\n\n->  '))
parameter_path = bool(path.exists(local))


if parameter_path == True:
    print('Arquivo encontrado, prosseguindo.\n')
    time.sleep(3)

    abrir_arquivo = open(local, 'rb')

    pdf_ler = PyPDF2.PdfFileReader(abrir_arquivo)

    numero_de_paginas = int(pdf_ler.numPages)



    # COLOCAR AS PÁGINAS NA ORDEM CORRETA PARA A IMPRESSÃO

    sequencia = []

    for j in range(numero_de_paginas):
        lista = numero_de_paginas - j
        if lista % 2 == 0:
            #folhas pares aqui
            sequencia.append(lista)

    for i in range(numero_de_paginas):
        lista = numero_de_paginas - i
        if lista % 2 != 0:
            #folhas impares aqui
            sequencia.append(lista)



    # IMPRIMIR AS PÁGINAS

    sequencia.reverse()
    for num in sequencia:
        if num % 2 != 0:
            #folhas impares
            print('\nPágina {} de {}.'.format(num, numero_de_paginas))
            os.system('sudo lp -P {} -o media=A4 -o number-up=1 -o sides=two-sided-long-edge -o fit-to-page {}'.format(num,local))
            
    confirmacao = str(input('\nApós imprimir a primeira leva, gire seu conjunto de folhas em 180° na horizontal e insira novamente na impressora.\nProsseguir? (y/n)\n\n-> '))
    if confirmacao == 'y':
        sequencia.reverse()
        for num in sequencia:
            if num % 2 == 0:
                #folhas pares
                print('\nPágina {} de {}.'.format(num, numero_de_paginas))
                os.system('sudo lp -P {} -o media=A4 -o number-up=1 -o sides=two-sided-long-edge -o fit-to-page {}'.format(num,local))
    else:
        exit()

else:
    print('\nArquivo não localizado. Use esse modelo de sintaxe:\n-> /home/user/diretorio/arquivo.pdf')
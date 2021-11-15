######################################################################
#  _____              _             _____      _       _             #
# |  __ \            | |           |  __ \    (_)     | |            #
# | |  | |_   _ _ __ | | _____  __ | |__) | __ _ _ __ | |_ ___ _ __  #
# | |  | | | | | '_ \| |/ _ \ \/ / |  ___/ '__| | '_ \| __/ _ \ '__| #
# | |__| | |_| | |_) | |  __/>  <  | |   | |  | | | | | ||  __/ |    #
# |_____/ \__,_| .__/|_|\___/_/\_\ |_|   |_|  |_|_| |_|\__\___|_|    #
#              | |                                                   #
#              |_|                                                   #
######################################################################


# Feito por Gabriel Dantas
# https://github.com/gdma2004

# Script para imprimir frente e verso em qualquer impressora, mesmo que ela não tenha essa função
# O código foi feito com foco em ambientes GNU/Linux e Unix
# Você deve ter os drivers da sua impressora instalados para que o programa funcione




# BIBLIOTECAS

import PyPDF2, os, time, shutil
from PyPDF2 import PdfFileReader, PdfFileWriter
from typing import Sequence
from os import path



# PASTA PRINTER

os.system('sudo clear')
print('######## DUPLEX PYTHON PRINTER #########\n')

home = os.getenv('HOME')

parameter_dir = bool(path.exists('{}/Arquivos_De_Impressão'.format(home)))

if parameter_dir == True:
    pass
else:
    print('Foi criada uma pasta chamada "Arquivos_De_Impressão" na sua home. Mova seus arquivos de impressão para ela.\n')
    os.system('mkdir ~/Arquivos_De_Impressão')

tree = str(input('Exibir arquivos da pasta de impressão? (y/n)\n\n-> '))

if tree == 'y':
    print(' ')
    os.system('tree ~/Arquivos_De_Impressão\n')
else:
    pass



# PATH

local = str(input('\n\nDigite o nome do seu arquivo\n\n-> '))
local_arquivo = ('{}/Arquivos_De_Impressão/'.format(home))
local_adaptado = ('{}{}'.format(local_arquivo,local))
parameter_path = bool(path.exists(local_adaptado))

if parameter_path == True:
    os.system('clear')
    print('Arquivo encontrado, prosseguindo.\n')
    time.sleep(3)



    # COLOCAR AS PÁGINAS NA ORDEM CORRETA PARA A IMPRESSÃO

    def impressao():
        
        print('Número de páginas: {}'.format(numero_de_paginas))
        
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
                print('\nPágina {}.'.format(num))
                os.system('sudo lp -P {} -o media=A4 -o number-up=1 -o sides=two-sided-long-edge -o fit-to-page {}'.format(num,local_adaptado))
                
        confirmacao = str(input('\nApós imprimir a primeira leva, gire seu conjunto de folhas em 180° na horizontal e insira novamente na impressora.\nProsseguir? (y/n)\n\n-> '))
        if confirmacao == 'y':
            sequencia.reverse()
            for num in sequencia:
                if num % 2 == 0:
                    #folhas pares
                    print('\nPágina {}.'.format(num))
                    os.system('sudo lp -P {} -o media=A4 -o number-up=1 -o sides=two-sided-long-edge -o fit-to-page {}'.format(num,local_adaptado))
        else:
            exit()


    # Adicionar 1 folha em branco no final do arquivo caso o número de páginas seja ímpar

    file = open(local_adaptado, 'rb')
    pdf_editar = PyPDF2.PdfFileReader(file)
    outPdf=PyPDF2.PdfFileWriter()
    numero_de_paginas = int(pdf_editar.numPages)


    if numero_de_paginas % 2 == 0:
        pass
    else:
        outPdf.appendPagesFromReader(pdf_editar)
        outPdf.addBlankPage()
        outStream=open('amended.pdf','wb')
        outPdf.write(outStream)
        outStream.close()
        file.close
        shutil.move('amended.pdf',local_adaptado)
    
    
    file = open(local_adaptado, 'rb')
    pdf_editar = PyPDF2.PdfFileReader(file)
    outPdf = PyPDF2.PdfFileWriter()
    numero_de_paginas = int(pdf_editar.numPages)


    impressao()


else:
    print('\nArquivo não localizado.')

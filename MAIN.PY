#importa as bibliotecas
import os
import time

# USUÁRIO INFORMA UM NÚMERO
contador = int(input ('informe um número inteiro'))
os.system('cls')

#conta aparti do número informado até 0
while contador >= 0:
    print (f'contagem regressiva: {contador}...')
    time.sleep (1)
    os.system('cls')
    contador -= 1

print('BOOOM!!!')
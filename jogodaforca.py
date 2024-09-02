import random, time


palavra = ['ABACAXI', 'BANANA', 'MORANGO', 'LIMÂO', 'MARACUJA', 'HONDA', 'HYUNDAI', 'FIAT', 'CHEVROLET', 'MITSUBISHI', 'PANELA', 'FRIGIDEIRA', 'PRATOS', 'GELADEIRA', 'FOGÂO', 'CAMA', 'ESTANTE', 'COMPUTADOR', 'TRAVISSEIRO', 'COBERTOR']
letras_jogador = []
temas = random.choice(palavra)
chances = 8

print('Olá , vamos jogar um jogo da forca??')
time.sleep(2)
print('Vou escolher um tema e você tem que acertar a palavra que escolhi!')
time.sleep(2)
print('Você tem 6 tentativas, vamos lá!')
time.sleep(2)

if temas == ('ABACAXI' or 'BANANA' or 'MORANGO' or 'LIMÂO' or 'MARACUJA'):
    print('O tema é frutas')
if temas == ('HONDA' or 'HYUNDAI' or 'FIAT' or 'CHEVROLET' or 'MITSUBISHI'):
    print('O tema é carros')
if temas == ('GELADEIRA' or 'PANELA' or 'FRIGIDEIRA' or 'PRATOS' or 'FOGÂO'):
    print('O tema é cozinha')
if temas == ('CAMA' or 'ESTANTE' or 'COMPUTADOR' or 'TRAVISSEIRO' or 'COBERTOR'):
    print('O tema é quarto')
else:
    print('') 

while True:
    for letra in palavra:
        if letra.upper() in letras_jogador:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    tentativa = input('Escolha uma letra: ')
    letras_jogador.append(tentativa.upper())

    if tentativa.upper() not in palavra:
        chances -= 1

    ganhou = True
    if letra in palavra:
        if letra.upper not in letras_jogador:
            ganhou = False

    if chances == 0 or ganhou:
        break


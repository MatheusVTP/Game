# Desafio JOKENPO
# Nome: Matheus Vinicius Teixeira 
# Requerimento : Desenvolvedor 
# Linguagem : Python

##################################################################
# VAMOS AOS COMANDOS PARA O JOKENPO!                             #
# PARA JOGAR , VAMOS ULTILIZAR APENAS 1 , 2 , 3 e 4              #
# 1 - PEDRA , 2 - PAPEL , 3 - TESOURA e 4 - PARA SAIR DO JOGO    #
# NA ESCOLHA DE PARTIDAS , ULTILIZAR APENAS NÚMEROS ÍMPARES.     # 
##################################################################

#coding: latin1

import random, time, sys


escolha = ['1','2','3','4']
maquina = (random.choice(escolha))

jogador = 0
pc = 0

nome = input('Olá! Por favor, insira o seu nome para jogarmos JOKENPO: ')
nome_1 = nome.capitalize()

while True:
      resultado_final = input('Vamos jogar na melhora de quantas rodas? Escolha um número. Por exemplo: 3, 5, 7 ou outro número ímpar: ')
      n_rodada = int(resultado_final)

      if n_rodada % 2 == 0:
         print('Você selicionou um número par, escolha partidas em números ímpares')
         time.sleep(0.3)
      else:
         print(f'Certo vamos jogar uma melhor de {n_rodada}')
         break

try:

    print(f'Bem vindo ao JOKENPO {nome_1}!\nMeu nome é Joãozinho e vamos disputar uma melhor de {resultado_final} rodadas! BOA SORTE!' "\n" '[1] Pedra' "\n" '[2] Papel' "\n" '[3] Tesoura' "\n" '[4] Para encerrar o jogo')

    while True:
            
        maquina = (random.choice(escolha))
        if jogador == (n_rodada // 2) + 1:
            print(f'PARABÉNS {nome_1} VOCÊ VENCEU O JOKENPO')
            time.sleep(3)
            break
        if pc == (n_rodada // 2) + 1:
            print(f' PUXA {nome_1} VOCÊ PERDEU O JOKENPO , Joãozinho É O VENCEDOR')
            time.sleep(3)
            break

        resultado = input('Faça sua escolha: ')

        if resultado not in escolha:
            print('OPS! Comando inválido. Ultilize apenas 1, 2 , 3 ou 4')
            continue

        if resultado == '4':
            print('Você encerrou o jogo!')
            time.sleep(5)
            break
        else:
            pass

        print('JO')
        time.sleep(0.2)
        print('KEN')
        time.sleep(0.2)
        print('PO')
        time.sleep(0.2)

        if resultado == '3' and maquina == '2':
            jogador = jogador + 1
            print(f'{nome_1} escolheu Tesoura e Joãozinho Papel, Você venceu essa rodada')
            print(f'O placar é de {jogador} x {pc}')

        if resultado == '2' and maquina == '1':
            jogador = jogador + 1
            print(f'{nome_1} escolheu Papel e Joãozinho Pedra, Você venceu essa rodada')
            print(f'O placar é de {jogador} x {pc}')

        if resultado == '1' and maquina == '3':
            jogador = jogador + 1
            print(f'{nome_1} escolheu Pedra e Joãozinho Tesoura, Você venceu essa rodada')
            print(f'O placar é de {jogador} x {pc}')

        if resultado == '3' and maquina == '1':
            pc = pc + 1
            print(f'{nome_1} escolheu Tesoura e Joãozinho Pedra, Você perdeu essa rodada')
            print(f'O placar é de {jogador} x {pc}')

        if resultado == '1' and maquina == '2':
            pc = pc + 1
            print(f'{nome_1} escolheu Pedra e Joãozinho Papel, Você perdeu essa rodada')
            print(f'O placar é de {jogador} x {pc}')

        if resultado == '2' and maquina == '3':
            pc = pc + 1
            print('Você escolheu Papel e Joãozinho Tesoura, Você perdeu essa rodada')
            print(f'O placar é de {jogador} x {pc}')

        if resultado == maquina:
            if maquina == '1':
                maquina = 'Pedra'
            if maquina == '2':
                maquina = 'Papel'
            if maquina == '3':
                maquina = 'Tesoura'
            
            print(f'Ambos escolheram {maquina}')
            print('Empatou! , proxima rodada na melhor de 5!')
            print(f'O placar e de {jogador} x {pc}')

except ValueError:
    print('Comando inválido, o programa deve ser reiniciado. Ultilize apenas números na escolha!')
    time.sleep(5)
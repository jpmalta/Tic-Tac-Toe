#!/usr/bin/env python
# coding: utf-8

import random

def mostra_tabuleiro(tabuleiro):
    print("-------------")
    for linha in tabuleiro:
        print("|", linha[0], "|", linha[1], "|", linha[2], "|")
        print("-------------")

def verifica_vitoria(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

def jogada_maquina(tabuleiro, jogador, oponente):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                tabuleiro[i][j] = jogador
                if verifica_vitoria(tabuleiro, jogador):
                    return
                tabuleiro[i][j] = " "
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                tabuleiro[i][j] = oponente
                if verifica_vitoria(tabuleiro, oponente):
                    tabuleiro[i][j] = jogador
                    return
                tabuleiro[i][j] = " "
    while True:
        i, j = random.randint(0, 2), random.randint(0, 2)
        if tabuleiro[i][j] == " ":
            tabuleiro[i][j] = jogador
            return

def start_jogo():
    
    # Criação do tabuleiro
    tabuleiro = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]
    
    # Definição dos jogadores
    jogadores = ["X", "O"]
    
    # Pergunta quantos jogadores irão jogar
    player_amount = int(input(f"Terá 1 ou 2 jogadores? "))
    
    if player_amount >= 2:
        jogador_atual = jogadores[0]  # Começa com X
        jogador_maquina = None
    elif player_amount == 1:
        jogador_atual = input(f"Escolha se quer ser [X] ou [O]: ").upper()
        if jogador_atual not in jogadores:
            print("Escolha inválida. Jogador será X por padrão.")
            jogador_atual = jogadores[0]
        jogador_maquina = jogadores[1] if jogador_atual == jogadores[0] else jogadores[0]

    # Mostra o tabuleiro inicial
    mostra_tabuleiro(tabuleiro)

    # Jogo para 1 jogador (Player vs Máquina)
    if player_amount == 1:
        while True:
            # Jogada do jogador humano
            if jogador_atual != jogador_maquina:
                linha = int(input(f"Jogador {jogador_atual}, escolha uma linha (1-3): ")) - 1
                coluna = int(input(f"Jogador {jogador_atual}, escolha uma coluna (1-3): ")) - 1
                
                # Verifica se a posição está ocupada
                while tabuleiro[linha][coluna] != " ":
                    print("Posição ocupada. Escolha outra opção.")
                    linha = int(input(f"Jogador {jogador_atual}, escolha uma linha (1-3): ")) - 1
                    coluna = int(input(f"Jogador {jogador_atual}, escolha uma coluna (1-3): ")) - 1
                
                tabuleiro[linha][coluna] = jogador_atual
                mostra_tabuleiro(tabuleiro)

                # Verifica se o jogador humano venceu
                if verifica_vitoria(tabuleiro, jogador_atual):
                    print(f"Jogador {jogador_atual} venceu!")
                    return
                
                # Verifica se o tabuleiro está cheio (empate)
                if all(cell != " " for row in tabuleiro for cell in row):
                    print("O jogo terminou empatado.")
                    return

                # Passa a vez para a máquina
                jogador_atual = jogador_maquina

            # Jogada da máquina
            elif jogador_atual == jogador_maquina:
                oponente = jogadores[0] if jogador_maquina == jogadores[1] else jogadores[1]
                jogada_maquina(tabuleiro, jogador_maquina, oponente)  # Correção aqui!
                mostra_tabuleiro(tabuleiro)

                # Verifica se a máquina venceu
                if verifica_vitoria(tabuleiro, jogador_maquina):
                    print(f"A máquina ({jogador_maquina}) venceu!")
                    return
                
                # Verifica se o tabuleiro está cheio (empate)
                if all(cell != " " for row in tabuleiro for cell in row):
                    print("O jogo terminou empatado.")
                    return

                # Passa a vez de volta para o jogador
                jogador_atual = oponente

    # Jogo para 2 jogadores (Player vs Player)
    if player_amount == 2:
        while True:
            # Jogada do jogador atual
            linha = int(input(f"Jogador {jogador_atual}, escolha uma linha (1-3): ")) - 1
            coluna = int(input(f"Jogador {jogador_atual}, escolha uma coluna (1-3): ")) - 1
            
            # Verifica se a posição está ocupada
            while tabuleiro[linha][coluna] != " ":
                print("Posição ocupada. Escolha outra opção.")
                linha = int(input(f"Jogador {jogador_atual}, escolha uma linha (1-3): ")) - 1
                coluna = int(input(f"Jogador {jogador_atual}, escolha uma coluna (1-3): ")) - 1
            
            tabuleiro[linha][coluna] = jogador_atual
            mostra_tabuleiro(tabuleiro)

            # Verifica se o jogador atual venceu
            if verifica_vitoria(tabuleiro, jogador_atual):
                print(f"Jogador {jogador_atual} venceu!")
                return
            
            # Verifica se o tabuleiro está cheio (empate)
            if all(cell != " " for row in tabuleiro for cell in row):
                print("O jogo terminou empatado.")
                return

            # Alterna para o próximo jogador
            jogador_atual = jogadores[0] if jogador_atual == jogadores[1] else jogadores[1]

    print("O jogo terminou empatado.")

start_jogo()
#!/usr/bin/env python
# coding: utf-8

# # Parte 1 - Jogo da Velha

# ### Passo 1: Criar uma função que escreve na tela o tabuleiro

# In[ ]:


def mostra_tabuleiro(tabuleiro):
    
    print("-------------") # Marca uma divisão entre telas para controle visual
    
    for linha in tabuleiro:
        
        print("|", linha[0], "|", linha[1], "|", linha[2], "|")
        
        print("-------------") # Marca uma divisão entre telas para controle visual


# ### Passo 2: Criar as regras para que o jogo seja finalizado

# In[ ]:


def verifica_vitoria(tabuleiro, jogador):
    
    # Vamos verificar possibilidade de vitória por sequência horizontal
    for i in range(0,3):
        
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            
            return True
        
    # Vamos verificar possibilidade de vitória por sequência vertical
    for i in range(0,3):
        
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            
            return True
        
    # Vamos verificar possibilidade de vitória na diagonal
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        
        return True
    
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        
        return True
    
    return False


# ### Passo 3: Criar a função que inicializa o jogo

# In[ ]:


def start_jogo():
    
    # Criação da lista que gera o tabuleiro
    tabuleiro = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]
    
    # Jogadores existentes
    jogadores = ["X","O"]
    
    # Define o marcador que inicia o jogo
    jogador_atual = jogadores[0]
    
    # Printa o tabuleiro na tela
    mostra_tabuleiro(tabuleiro)
    
    # Definindo o posicionamento dos marcadores
    for i in range(1,10):
        
        linha = int(input(f"Jogador {jogador_atual} escolha uma linha 1 - 3: ")) - 1
        coluna = int(input(f"Jogador {jogador_atual} escolha uma coluna 1 - 3: ")) - 1
        
        # Verificando se a posicao escolhida e valida
        if tabuleiro[linha][coluna] != " ":
            
            print("Posição ocupada.\nEscolha outra opção.")
            linha = int(input(f"Jogador {jogador_atual} escolha uma linha 1 - 3: ")) - 1
            coluna = int(input(f"Jogador {jogador_atual} escolha uma coluna 1 - 3: ")) - 1
               
        tabuleiro[linha][coluna] = jogador_atual
        mostra_tabuleiro(tabuleiro)
        
        if verifica_vitoria(tabuleiro, jogador_atual):
            
            print(f"Jogador {jogador_atual} venceu!!!")
            return
        
        # Precisamos alterar entre os jogadores
        jogador_atual = jogadores[i % 2]
        
    # Caso nenhuma das condições de vitória sejam encontradas, devemos considerar o resultado de empate
    print("O jogo terminou empatado.")


# In[ ]:


start_jogo()


import numpy as np

def colocar_peca(tabuleiro,linha,coluna,peca):
    #Colocar peça (1 ou 2)
    tabuleiro[linha][coluna]= peca

def verificar_vitoria(tabuleiro, peca):
    # Verificar se jogador venceu
    linhas = np.any(np.all(tabuleiro == peca, axis=1))
    colunas = np.any(np.all(tabuleiro == peca, axis=0))
    diagonais = np.all(np.diag(tabuleiro)== peca) or np.all(np.diag(np.fliplr(tabuleiro)) == peca)

    return any([linhas, colunas, diagonais])

def jogar():
    tabuleiro = np.zeros((3,3))
    peca_atual = 1
    vencedor = False
    empate = False

    # Loop principal do jogo

    while not vencedor and not empate:
        print(tabuleiro)

        while True:
            linha = int(input('Escolha a linha (0,1,2): '))
            coluna = int(input('Escolha a coluna (0,1,2): '))

            if not any(x > 2 for x in [linha, coluna]):
                break
            print('\nEscolha linhas e colunas válidas! De 0 a 2 \n')

        if tabuleiro[linha][coluna] !=0:
            print('\nPosição Ocupada! Jogue novamente\n')
            continue

        # Colocando a peça no tabuleiro e verificando se o jogador atual venceu

        colocar_peca(tabuleiro, linha, coluna, peca_atual)
        vencedor = verificar_vitoria(tabuleiro, peca_atual)

        # Verificar se houve empate

        if np.all(tabuleiro != 0):
            empate = True


        # Passa a vez para o proximo jogador 

        if not vencedor and not empate:
            peca_atual = 2 if peca_atual == 1 else 1

    # Imprmir resultado do jogo

    print(tabuleiro)

    if vencedor:
        print(f'\n\n\tPARABÉNS, JOGADOR {peca_atual} VENCEU! =====================')
    else:
        print('\n\n\tEmpate!=======================')


# Executando o jogo
jogar()


        

        


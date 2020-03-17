# FUNÇÃO: CONDIÇÃO DO 'CARA OU COROA'
def cond_cara_coroa():
    lista_cc = ['cara','coroa']
    valor = input('\n{}, você escolhe cara ou coroa? Digite aqui: ' .format(j1))
    while valor not in lista_cc:
        valor = input("Amigo(a), só tem as opções 'cara' e 'coroa'. Escolha novamente: ")
    return valor

# FUNÇÃO: CONDIÇÃO DE ENTRADA
def cond_entrada():
    try:
        lista_quant_linhas_colunas = ['2','3','4','5','6','7','8','9']
        valor = input('Digite aqui: ')
        while valor not in lista_quant_linhas_colunas:
            valor = input('Valor inválido! Digite novamente: ')
        return int(valor)
    except:
        cond_entrada()
        

# FUNÇÃO: COMER UMA PEÇA
def comer_peca(tabuleiro, linha_origem, coluna_origem, linha_destino, coluna_destino):
    
    if tabuleiro[linha_origem][coluna_origem] == 'P':
        incremento_linha = 1
        
        if linha_destino == linha_origem+2 and coluna_destino == coluna_origem-2:
            incremento_coluna = -1
        else:
            incremento_coluna = 1

    else:
        incremento_linha = -1    
        
        if linha_destino == linha_origem-2 and coluna_destino == coluna_origem-2:
            incremento_coluna = -1
        else:
            incremento_coluna = 1

    peca = tabuleiro[linha_origem][coluna_origem]
    tabuleiro[linha_origem][coluna_origem] = ' '
    tabuleiro[linha_destino][coluna_destino] = peca
    tabuleiro[linha_origem+incremento_linha][coluna_origem+incremento_coluna] = ' '


# FUNÇÃO: COMER QUALQUER POSIÇÃO (COMIDA CONSECUTIVA OU DAMA)
def comer_qq_pos(tabuleiro, linha_origem, coluna_origem, linha_destino, coluna_destino, linha_intermed, coluna_intermed):
    peca = tabuleiro[linha_origem][coluna_origem]
    tabuleiro[linha_origem][coluna_origem] = ' '
    tabuleiro[linha_destino][coluna_destino] = peca
    tabuleiro[linha_intermed][coluna_intermed] = ' '


# FUNÇÃO: COMER CONSECUTIVAMENTE
def comer_consec(tabuleiro, linha_origem, coluna_origem, peca_comer1, peca_comer2):
        
    booleano = False

    while booleano == False:
    
        if (tabuleiro[linha_origem-1][coluna_origem-1] == peca_comer1 or tabuleiro[linha_origem-1][coluna_origem-1] == peca_comer2) and tabuleiro[linha_origem-2][coluna_origem-2] == ' ':
            executar_comida = input("Aperte 'Enter' para comer a peça obrigatória!")
            comer_qq_pos(tabuleiro, linha_origem, coluna_origem, linha_origem-2, coluna_origem-2, linha_origem-1, coluna_origem-1)
            linha_origem -= 2
            coluna_origem -= 2
    
        elif (tabuleiro[linha_origem-1][coluna_origem+1] == peca_comer1 or tabuleiro[linha_origem-1][coluna_origem+1] == peca_comer2) and tabuleiro[linha_origem-2][coluna_origem+2] == ' ':
            executar_comida = input("Aperte 'Enter' para comer a peça obrigatória!")
            comer_qq_pos(tabuleiro, linha_origem, coluna_origem, linha_origem-2, coluna_origem+2, linha_origem-1, coluna_origem+1)
            linha_origem -= 2
            coluna_origem += 2 

        elif (tabuleiro[linha_origem+1][coluna_origem-1] == peca_comer1 or tabuleiro[linha_origem+1][coluna_origem-1] == peca_comer2) and tabuleiro[linha_origem+2][coluna_origem-2] == ' ':
            executar_comida = input("Aperte 'Enter' para comer a peça obrigatória!")
            comer_qq_pos(tabuleiro, linha_origem, coluna_origem, linha_origem+2, coluna_origem-2, linha_origem+1, coluna_origem-1)
            linha_origem += 2
            coluna_origem -= 2 

        elif (tabuleiro[linha_origem+1][coluna_origem+1] == peca_comer1 or tabuleiro[linha_origem+1][coluna_origem+1] == peca_comer2) and tabuleiro[linha_origem+2][coluna_origem+2] == ' ':
            executar_comida = input("Aperte 'Enter' para comer a peça obrigatória!")
            comer_qq_pos(tabuleiro, linha_origem, coluna_origem, linha_origem+2, coluna_origem+2, linha_origem+1, coluna_origem+1)
            linha_origem += 2
            coluna_origem += 2 

        else:
            booleano = True


# FUNÇÃO: OBRIGAR A COMER UMA PEÇA
def obr_comer():
    
    peca = 'B'
    peca_comer1 = 'P'
    peca_comer2 = 'PP'
    incremento_linha1 = -1
    incremento_coluna1 = -1
    incremento_coluna2 = -2
    incremento_linha2 = -2
    incremento_coluna3 = 1
    incremento_coluna4 = 2

    if jogador_da_vez == False:
        peca = 'P'
        peca_comer1 = 'B'
        peca_comer2 = 'BB'
        incremento_linha1 = 1
        incremento_linha2 = 2

    cont_linha = 0
    for linha in tabuleiro:
        cont_coluna = 0
        for valor in linha:
            if valor == peca:
                linha_origem = cont_linha
                coluna_origem = cont_coluna
   
                if (tabuleiro[linha_origem+incremento_linha1][coluna_origem+incremento_coluna1] == peca_comer1 or tabuleiro[linha_origem+incremento_linha1][coluna_origem+incremento_coluna1] == peca_comer2) and tabuleiro[linha_origem+incremento_linha2][coluna_origem+incremento_coluna2] == ' ':
                    executar_comida = input("\nAperte 'Enter' para comer a peça obrigatória!")
                    comer_peca(tabuleiro, linha_origem, coluna_origem, linha_origem+incremento_linha2, coluna_origem+incremento_coluna2)
                    comer_consec(tabuleiro, linha_origem+incremento_linha2, coluna_origem+incremento_coluna2, peca_comer1, peca_comer2)
                    return True
                    

                elif (tabuleiro[linha_origem+incremento_linha1][coluna_origem+incremento_coluna3] == peca_comer1 or tabuleiro[linha_origem+incremento_linha1][coluna_origem+incremento_coluna3] == peca_comer2) and tabuleiro[linha_origem+incremento_linha2][coluna_origem+incremento_coluna4] == ' ':
                    executar_comida = input("\nAperte 'Enter' para comer a peça obrigatória!")
                    comer_peca(tabuleiro, linha_origem, coluna_origem, linha_origem+incremento_linha2, coluna_origem+incremento_coluna4)
                    comer_consec(tabuleiro, linha_origem+incremento_linha2, coluna_origem+incremento_coluna4, peca_comer1, peca_comer2)
                    return True
                    
                
            cont_coluna += 1
        cont_linha += 1
        
    return False


# FUNÇÃO: VALIDAÇÃO DE JOGADA
def validacao_jogada(tabuleiro, linha_origem, coluna_origem, linha_destino, coluna_destino):
    incremento_linha_1 = -1
    incremento_linha_2 = -2
    peca = 'B'

    if not jogador_da_vez:
        peca = 'P'
        incremento_linha_1 = 1
        incremento_linha_2 = 2
        
    if (tabuleiro[linha_origem][coluna_origem] == peca) and (tabuleiro[linha_destino][coluna_destino] == ' ') and (linha_destino == linha_origem+incremento_linha_1 and (coluna_destino == coluna_origem-1 or coluna_destino == coluna_origem+1)):
        return True
    else:
        return False


# FUNÇÃO DAMA: VALIDAÇÃO DE JOGADA
def dama_validacao_jogada(tabuleiro, linha_origem, coluna_origem, linha_destino, coluna_destino):

    if jogador_da_vez == True:
        
        # POSSIBILIDADE DE PERCORRER POR TODA A DIAGONAL
        pos = 1
        
        if tabuleiro[linha_destino][coluna_destino] == ' ' and tabuleiro[linha_origem][coluna_origem] == 'BB':

            # ANÁLISE DA DIAGONAL ESQUERDA PARA CIMA
            if linha_destino < linha_origem and coluna_destino < coluna_origem:
                if tabuleiro[linha_destino][coluna_destino] == tabuleiro[linha_origem-1][coluna_origem-1]:
                    return True
                else:
                    
                    # VERIFICAR SE OS ESPAÇOS SÃO VAZIOS
                    while tabuleiro[linha_destino+pos][coluna_destino+pos] != tabuleiro[linha_origem][coluna_origem]:
                        if tabuleiro[linha_destino+pos][coluna_destino+pos] != ' ':
                            return False
                        pos += 1
                    return True

            # ANÁLISE DA DIAGONAL DIREITA PARA CIMA        
            elif linha_destino < linha_origem and coluna_destino > coluna_origem:
                if tabuleiro[linha_destino][coluna_destino] == tabuleiro[linha_origem-1][coluna_origem+1]:
                    return True
                else:
                    while tabuleiro[linha_destino+pos][coluna_destino-pos] != tabuleiro[linha_origem][coluna_origem]:
                        if tabuleiro[linha_destino+pos][coluna_destino-pos] != ' ':
                            return False
                        pos += 1
                    return True

            # ANÁLISE DA DIAGONAL ESQUERDA PARA BAIXO
            elif linha_destino > linha_origem and coluna_destino < coluna_origem:
                if tabuleiro[linha_destino][coluna_destino] == tabuleiro[linha_origem+1][coluna_origem-1]:
                    return True
                else:
                    while tabuleiro[linha_destino-pos][coluna_destino+pos] != tabuleiro[linha_origem][coluna_origem]:
                        if tabuleiro[linha_destino-pos][coluna_destino+pos] != ' ':
                            return False
                        pos += 1
                    return True

            # ANÁLISE DA DIAGONAL DIREITA PARA BAIXO
            elif linha_destino > linha_origem and coluna_destino > coluna_origem:
                if tabuleiro[linha_destino][coluna_destino] == tabuleiro[linha_origem+1][coluna_origem+1]:
                    return True
                else:
                    while tabuleiro[linha_destino-pos][coluna_destino-pos] != tabuleiro[linha_origem][coluna_origem]:
                        if tabuleiro[linha_destino-pos][coluna_destino-pos] != ' ':
                            return False
                        pos += 1
                    return True
        return False

    else:
        
        # POSSIBILIDADE DE PERCORRER POR TODA A DIAGONAL
        pos = 1
        
        if tabuleiro[linha_destino][coluna_destino] == ' ' and tabuleiro[linha_origem][coluna_origem] == 'PP':

            # ANÁLISE DA DIAGONAL ESQUERDA PARA CIMA
            if linha_destino < linha_origem and coluna_destino < coluna_origem:
                if tabuleiro[linha_destino][coluna_destino] == tabuleiro[linha_origem-1][coluna_origem-1]:
                    return True
                else:
                    
                    # VERIFICAR SE OS ESPAÇOS SÃO VAZIOS
                    while tabuleiro[linha_destino+pos][coluna_destino+pos] != tabuleiro[linha_origem][coluna_origem]:
                        if tabuleiro[linha_destino+pos][coluna_destino+pos] != ' ':
                            return False
                        pos += 1
                    return True

            # ANÁLISE DA DIAGONAL DIREITA PARA CIMA        
            elif linha_destino < linha_origem and coluna_destino > coluna_origem:
                if tabuleiro[linha_destino][coluna_destino] == tabuleiro[linha_origem-1][coluna_origem+1]:
                    return True
                else:
                    while tabuleiro[linha_destino+pos][coluna_destino-pos] != tabuleiro[linha_origem][coluna_origem]:
                        if tabuleiro[linha_destino+pos][coluna_destino-pos] != ' ':
                            return False
                        pos += 1
                    return True

            # ANÁLISE DA DIAGONAL ESQUERDA PARA BAIXO
            elif linha_destino > linha_origem and coluna_destino < coluna_origem:
                if tabuleiro[linha_destino][coluna_destino] == tabuleiro[linha_origem+1][coluna_origem-1]:
                    return True
                else:
                    while tabuleiro[linha_destino-pos][coluna_destino+pos] != tabuleiro[linha_origem][coluna_origem]:
                        if tabuleiro[linha_destino-pos][coluna_destino+pos] != ' ':
                            return False
                        pos += 1
                    return True

            # ANÁLISE DA DIAGONAL DIREITA PARA BAIXO
            elif linha_destino > linha_origem and coluna_destino > coluna_origem:
                if tabuleiro[linha_destino][coluna_destino] == tabuleiro[linha_origem+1][coluna_origem+1]:
                    return True
                else:
                    while tabuleiro[linha_destino-pos][coluna_destino-pos] != tabuleiro[linha_origem][coluna_origem]:
                        if tabuleiro[linha_destino-pos][coluna_destino-pos] != ' ':
                            return False
                        pos += 1
                    return True
        return False

# FUNÇÃO: EXECUTAR JOGADA NORMAL
def jogada_normal(tabuleiro, linha_origem, coluna_origem, linha_destino, coluna_destino):
    peca = tabuleiro[linha_origem][coluna_origem]
    tabuleiro[linha_origem][coluna_origem] = ' '
    tabuleiro[linha_destino][coluna_destino] = peca


# FUNÇÃO DAMA: OBRIGAR A COMER UMA PEÇA
def dama_obr_comer():

    peca = 'BB'
    peca_comer1 = 'P'
    peca_comer2 = 'PP'

    if jogador_da_vez == False:
        peca = 'PP'
        peca_comer1 = 'B'
        peca_comer2 = 'BB'

    lista_cont_comidas = []
    cont_comidas = 0
    
    cont_linha = 0
    for linha in tabuleiro:
        cont_coluna = 0
        for valor in linha:
            if valor == peca:
                linha_origem = cont_linha
                coluna_origem = cont_coluna

                booleano = True
                comidas_jogada_passada = 0

                while booleano:
                    pos1 = 1
                    pos2 = 2
                    duas_pecas_juntas = True
                        
                    while tabuleiro[linha_origem-pos2][coluna_origem+pos2] != '-' and duas_pecas_juntas:

                        if (tabuleiro[linha_origem-pos1][coluna_origem+pos1] == peca_comer1 or tabuleiro[linha_origem-pos1][coluna_origem+pos1] == peca_comer2) and (tabuleiro[linha_origem-pos2][coluna_origem+pos2] == peca_comer1 or tabuleiro[linha_origem-pos2][coluna_origem+pos2] == peca_comer2):
                            duas_pecas_juntas = False
                            
                        elif (tabuleiro[linha_origem-pos1][coluna_origem+pos1] == peca_comer1 or tabuleiro[linha_origem-pos1][coluna_origem+pos1] == peca_comer2) and tabuleiro[linha_origem-pos2][coluna_origem+pos2] == ' ':
                            executar_comida = input("\nAperte 'Enter' para comer a peça obrigatória!")
                            comer_qq_pos(tabuleiro, linha_origem, coluna_origem, linha_origem-pos2, coluna_origem+pos2, linha_origem-pos1, coluna_origem+pos1)
                            linha_origem = linha_origem-pos2
                            coluna_origem = coluna_origem+pos2
                            pos1 = 0
                            pos2 = 1
                            cont_comidas += 1

                        pos1 += 1
                        pos2 += 1

                    pos1 = 1
                    pos2 = 2
                    duas_pecas_juntas = True
                        
                    while tabuleiro[linha_origem-pos2][coluna_origem-pos2] != '-' and duas_pecas_juntas:

                        if (tabuleiro[linha_origem-pos1][coluna_origem-pos1] == peca_comer1 or tabuleiro[linha_origem-pos1][coluna_origem-pos1] == peca_comer2) and (tabuleiro[linha_origem-pos2][coluna_origem-pos2] == peca_comer1 or tabuleiro[linha_origem-pos2][coluna_origem-pos2] == peca_comer2):
                            duas_pecas_juntas = False
                            
                        elif (tabuleiro[linha_origem-pos1][coluna_origem-pos1] == peca_comer1 or tabuleiro[linha_origem-pos1][coluna_origem-pos1] == peca_comer2) and tabuleiro[linha_origem-pos2][coluna_origem-pos2] == ' ':
                            executar_comida = input("\nAperte 'Enter' para comer a peça obrigatória!")
                            comer_qq_pos(tabuleiro, linha_origem, coluna_origem, linha_origem-pos2, coluna_origem-pos2, linha_origem-pos1, coluna_origem-pos1)
                            linha_origem = linha_origem-pos2
                            coluna_origem = coluna_origem-pos2
                            pos1 = 0
                            pos2 = 1
                            cont_comidas += 1

                        pos1 += 1
                        pos2 += 1

                    pos1 = 1
                    pos2 = 2
                    duas_pecas_juntas = True
                        
                    while tabuleiro[linha_origem+pos2][coluna_origem-pos2] != '-' and duas_pecas_juntas:

                        if (tabuleiro[linha_origem+pos1][coluna_origem-pos1] == peca_comer1 or tabuleiro[linha_origem+pos1][coluna_origem-pos1] == peca_comer2) and (tabuleiro[linha_origem+pos2][coluna_origem-pos2] == peca_comer1 or tabuleiro[linha_origem+pos2][coluna_origem-pos2] == peca_comer2):
                            duas_pecas_juntas = False
                            
                        elif (tabuleiro[linha_origem+pos1][coluna_origem-pos1] == peca_comer1 or tabuleiro[linha_origem+pos1][coluna_origem-pos1] == peca_comer2) and tabuleiro[linha_origem+pos2][coluna_origem-pos2] == ' ':
                            executar_comida = input("\nAperte 'Enter' para comer a peça obrigatória!")
                            comer_qq_pos(tabuleiro, linha_origem, coluna_origem, linha_origem+pos2, coluna_origem-pos2, linha_origem+pos1, coluna_origem-pos1)
                            linha_origem = linha_origem+pos2
                            coluna_origem = coluna_origem-pos2
                            pos1 = 0
                            pos2 = 1
                            cont_comidas += 1

                        pos1 += 1
                        pos2 += 1

                    pos1 = 1
                    pos2 = 2
                    duas_pecas_juntas = True
                        
                    while tabuleiro[linha_origem+pos2][coluna_origem+pos2] != '-' and duas_pecas_juntas:

                        if (tabuleiro[linha_origem+pos1][coluna_origem+pos1] == peca_comer1 or tabuleiro[linha_origem+pos1][coluna_origem+pos1] == peca_comer2) and (tabuleiro[linha_origem+pos2][coluna_origem+pos2] == peca_comer1 or tabuleiro[linha_origem+pos2][coluna_origem+pos2] == peca_comer2):
                            duas_pecas_juntas = False
                            
                        elif (tabuleiro[linha_origem+pos1][coluna_origem+pos1] == peca_comer1 or tabuleiro[linha_origem+pos1][coluna_origem+pos1] == peca_comer2) and tabuleiro[linha_origem+pos2][coluna_origem+pos2] == ' ':
                            executar_comida = input("\nAperte 'Enter' para comer a peça obrigatória!")
                            comer_qq_pos(tabuleiro, linha_origem, coluna_origem, linha_origem+pos2, coluna_origem+pos2, linha_origem+pos1, coluna_origem+pos1)
                            linha_origem = linha_origem+pos2
                            coluna_origem = coluna_origem+pos2
                            pos1 = 0
                            pos2 = 1
                            cont_comidas += 1

                        pos1 += 1
                        pos2 += 1

                    if cont_comidas == comidas_jogada_passada:
                        booleano = False

                    comidas_jogada_passada = cont_comidas
                   

            cont_coluna += 1
        cont_linha += 1

    if cont_comidas != 0:
        return True
   
    return False


# FUNÇÃO: JOGADA
def jogada():
        
    # VERIFICAÇÃO EM TODO O TABULEIRO PARA TRANSFORMAR AS DAMAS, SEJA 'P' OU 'B'
    cont_linha = 0
    for linha in tabuleiro:
        cont_coluna = 0
        for valor in linha:
            if valor == 'P' and cont_linha == 9:
                tabuleiro[cont_linha][cont_coluna] = 'PP'
            if valor == 'B' and cont_linha == 2:
                tabuleiro[cont_linha][cont_coluna] = 'BB'
            cont_coluna += 1
        cont_linha += 1

    # IMPRESSÃO DE TABULEIRO            
    print('\n')
    for linha in tabuleiro[1:10]:
        print(linha[1:10])

    if dama_obr_comer():
        print('\nPeça(s) comida(s) com sucesso!')

    elif obr_comer():
        print('\nPeça(s) comida(s) com sucesso!')
        
    else:
        print('\nLinha da peça: ')
        linha_origem = cond_entrada() 

        print('\nColuna da peça: ')    
        coluna_origem = cond_entrada() 

        print('\nLinha da casa que você quer ir: ')
        linha_destino = cond_entrada()
            
        print('\nColuna da casa que você quer ir: ')    
        coluna_destino = cond_entrada()

        if tabuleiro[linha_origem][coluna_origem] == 'PP' or tabuleiro[linha_origem][coluna_origem] == 'BB':
            
            while not dama_validacao_jogada(tabuleiro, linha_origem, coluna_origem, linha_destino, coluna_destino):
                    
                print('\nJogada inválida! Tente novamente.')

                print('\n')
                for linha in tabuleiro[1:10]:
                    print(linha[1:10])
                    
                print('\nLinha da peça: ')
                linha_origem = cond_entrada() 

                print('\nColuna da peça: ')    
                coluna_origem = cond_entrada() 

                print('\nLinha da casa que você quer ir: ')
                linha_destino = cond_entrada()
                
                print('\nColuna da casa que você quer ir: ')    
                coluna_destino = cond_entrada()

            jogada_normal(tabuleiro, linha_origem, coluna_origem, linha_destino, coluna_destino)
  
        else:
            
            while not validacao_jogada(tabuleiro, linha_origem, coluna_origem, linha_destino, coluna_destino):
                
                print('\nJogada inválida! Tente novamente.')

                print('\n')
                for linha in tabuleiro[1:10]:
                    print(linha[1:10])
                    
                print('\nLinha da peça: ')
                linha_origem = cond_entrada() 

                print('\nColuna da peça: ')    
                coluna_origem = cond_entrada() 

                print('\nLinha da casa que você quer ir: ')
                linha_destino = cond_entrada()
                
                print('\nColuna da casa que você quer ir: ')    
                coluna_destino = cond_entrada()

            jogada_normal(tabuleiro, linha_origem, coluna_origem, linha_destino, coluna_destino)


# COMEÇO DO JOGO
import time, random

tabuleiro = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '2', '3', '4', '5', '6', '7', '8', '9', '-', '-'],
             ['-', '2',' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P', '-', '-'],
             ['-', '3','P', ' ', 'P', ' ', 'P', ' ', 'P', ' ', '-', '-'],
             ['-', '4',' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P', '-', '-'],
             ['-', '5',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-'],
             ['-', '6',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-'],
             ['-', '7','B', ' ', 'B', ' ', 'B', ' ', 'B', ' ', '-', '-'],
             ['-', '8',' ', 'B', ' ', 'B', ' ', 'B', ' ', 'B', '-', '-'],
             ['-', '9','B', ' ', 'B', ' ', 'B', ' ', 'B', ' ', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

# ABERTURA DO JOGO
print('\nSeja bem-vindo ao Jogo de Dama!')
j1 = input('\nJogador 1, digite seu nome: ')
j2 = input('Jogador 2, digite seu nome: ')

print('\nOpções: ')
print('\n1. Preto\n2. Branco')
print("\nSerá sorteado por meio de 'cara ou coroa' o jogador que escolherá o primeiro personagem!\nObs.: o jogador que estiver jogando com as peças brancas começa o jogo (juro que não é racismo, é só a regra mesmo).")


# ESCOLHA DA OPÇÃO DO 'CARA OU COROA'
ccj1 = cond_cara_coroa()

if ccj1 == 'cara':
    ccj2 = 'coroa'
    print("{}, você será '{}'".format(j2,ccj2))
else:
    ccj2 = 'cara'
    print("{}, você será '{}'.".format(j2,ccj2))
    

# SORTEIO POR 'CARA OU COROA'
print('\nSorteando...')
time.sleep(3)

if (random.randint(0,1))%2 == 0:
    resultado = 'cara'
else:
    resultado = 'coroa'

print('Resultado: {}!'.format(resultado))


# ESCOLHA DA OPÇÃO DE PERSONAGEM
lista = ['1','2']
if ccj1 == resultado:
    opcaoj1 = input('\n{}, quem você será? Opção 1 ou 2: ' .format(j1))
    while opcaoj1 not in lista:
        opcaoj1 = input('Amigo(a), só tem as opções 1 e 2. Escolha novamente: ')

    if opcaoj1 == '1':
        print('{}, você será a opção 2.'.format(j2))
        ji = j2
        jf = j1
    else:
        print('{}, você será a opção 1.'.format(j2))
        ji = j1
        jf = j2
        
else:
    opcaoj2 = input('\n{}, quem você será? Opção 1 ou 2: ' .format(j2))
    while opcaoj2 not in lista:
        opcaoj2 = input('Amigo(a), só tem as opções 1 e 2. Escolha novamente: ')

    if opcaoj2 == '1':
        print('{}, você será a opção 2.'.format(j1))
        ji = j1
        jf = j2
    else:
        print('{}, você será a opção 1.'.format(j1))
        ji = j2
        jf = j1
        
print('\nTudo pronto! Que começe o jogo!')


# JOGADAS
finish = False

while not finish:

    # JOGADA DO JOGADOR INICIANTE
    jogador_da_vez = True
    print('\nVez do(a) {} (peças brancas)...'.format(ji))
    time.sleep(2)
    jogada()
    pecas_tabuleiro = []
    for linha in tabuleiro[2:10]:
        for valor in linha:
            pecas_tabuleiro.append(valor)
       
    if 'P' not in pecas_tabuleiro and 'PP' not in pecas_tabuleiro:
        print('\nVITÓRIA DO JOGADOR BRANCO!\nParabéns, {}!!!' .format(ji))
        finish = True
        continue


    # JOGADA DO JOGADOR FINAL
    jogador_da_vez = False
    print('\nVez do(a) {} (peças pretas)...'.format(jf))
    time.sleep(2)
    jogada()
    pecas_tabuleiro = []
    for linha in tabuleiro[2:10]:
        for valor in linha:
            pecas_tabuleiro.append(valor)
            
    if 'B' not in pecas_tabuleiro and 'BB' not in pecas_tabuleiro:
        print('\nVITÓRIA DO JOGADOR PRETO!\nParabéns, {}!!!' .format(jf))
        finish = True


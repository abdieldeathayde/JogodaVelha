#Função principal

def vezdejogar(jogador):

    #Jogadas do Jogador 1
    
    if jogador == 'jogador1':
        a = 'erro'
        while a == 'erro':
            joga1 = input('Jogador 1, é a sua vez. Escolha a coordenada onde quer jogar: ')
            if joga1 == 'a1':
                if jogadas['a1'] == ' ':
                    jogadas['a1'] = opcaoj1
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()      
            elif joga1 == 'a2':
                if jogadas['a2'] == ' ':
                    jogadas['a2'] = opcaoj1
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga1 == 'a3':
                if jogadas['a3'] == ' ':
                    jogadas['a3'] = opcaoj1
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga1 == 'b1':
                if jogadas['b1'] == ' ':
                    jogadas['b1'] = opcaoj1
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga1 == 'b2':
                if jogadas['b2'] == ' ':
                    jogadas['b2'] = opcaoj1
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga1 == 'b3':
                if jogadas['b3'] == ' ':
                    jogadas['b3'] = opcaoj1
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga1 == 'c1':
                if jogadas['c1'] == ' ':
                    jogadas['c1'] = opcaoj1
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga1 == 'c2':
                if jogadas['c2'] == ' ':
                    jogadas['c2'] = opcaoj1
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga1 == 'c3':
                if jogadas['c3'] == ' ':
                    jogadas['c3'] = opcaoj1
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            else:
                print('Opção incorreta, digite outra coordenada.\n')
                    
    #Jogadas do Jogador 2

    elif jogador == 'jogador2':
        a = 'erro'
        while a == 'erro':
            joga2 = input('Jogador 2, é a sua vez. Escolha a coordenada onde quer jogar: ')
            if joga2 == 'a1':
                if jogadas['a1'] == ' ':
                    jogadas['a1'] = opcaoj2
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga2 == 'a2':
                if jogadas['a2'] == ' ':
                    jogadas['a2'] = opcaoj2
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga2 == 'a3':
                if jogadas['a3'] == ' ':
                    jogadas['a3'] = opcaoj2
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga2 == 'b1':
                if jogadas['b1'] == ' ':
                    jogadas['b1'] = opcaoj2
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga2 == 'b2':
                if jogadas['b2'] == ' ':
                    jogadas['b2'] = opcaoj2
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga2 == 'b3':
                if jogadas['b3'] == ' ':
                    jogadas['b3'] = opcaoj2
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga2 == 'c1':
                if jogadas['c1'] == ' ':
                    jogadas['c1'] = opcaoj2
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga2 == 'c2':
                if jogadas['c2'] == ' ':
                    jogadas['c2'] = opcaoj2
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            elif joga2 == 'c3':
                if jogadas['c3'] == ' ':
                    jogadas['c3'] = opcaoj2
                    a = 'continue'
                    print(tabuleiro())
                else:
                    erro()
            else:
                print('Opção incorreta, digite outra coordenada.\n')



#Funções secundárias:

#____________________________________

#Função de atualizaçao do tabuleiro

def tabuleiro():
    return '\n  1 2 3 \na {}|{}|{} \n  -----\nb {}|{}|{} \n  -----\nc {}|{}|{} \n'.format(jogadas['a1'], jogadas['a2'], jogadas['a3'], jogadas['b1'], jogadas['b2'], jogadas['b3'], jogadas['c1'], jogadas['c2'], jogadas['c3'])

#Função de erro por jogar em um espaço já ocupado

def erro():
    print('\nVocê não pode jogar aí, escolha uma posição vazia.')

#Função de possibilidades de vitória

def vitoria():
    return jogadas['a1'] == opcaoj2 and jogadas['a2'] == opcaoj2 and jogadas['a3'] == opcaoj2 or jogadas['b1'] == opcaoj2 and jogadas['b2'] == opcaoj2 and jogadas['b3'] == opcaoj2 or jogadas['c1'] == opcaoj2 and jogadas['c2'] == opcaoj2 and jogadas['c3'] == opcaoj2 or jogadas['a1'] == opcaoj2 and jogadas['b1'] == opcaoj2 and jogadas['c1'] == opcaoj2 or jogadas['a2'] == opcaoj2 and jogadas['b2'] == opcaoj2 and jogadas['c2'] == opcaoj2 or jogadas['a3'] == opcaoj2 and jogadas['b3'] == opcaoj2 and jogadas['c3'] == opcaoj2 or jogadas['a1'] == opcaoj2 and jogadas['b2'] == opcaoj2 and jogadas['c3'] == opcaoj2 or jogadas['a3'] == opcaoj2 and jogadas['b2'] == opcaoj2 and jogadas['c1'] == opcaoj2

#____________________________________




#Início do programa
                
print('Bem-vindos ao Jogo da Velha!')

repetir = 's'
while repetir == 's':

    #Criando um tabueiro vazio e as opções iniciais do jogo
    
    jogadas = {'a1': ' ', 'a2': ' ', 'a3': ' ', 'b1': ' ', 'b2': ' ', 'b3': ' ', 'c1': ' ', 'c2': ' ', 'c3': ' '}
    primeiro = ''
    opcaoj1 = ''
    opcaoj2 = ''

    #Início do jogo

    #Definindo quem jogará primeiro e qual símbolo usará
    
    print("\nTirem par ou ímpar para decidirem quem será o primeiro a jogar e quem jogará com 'x' ou 'o'. Quem ganhar o par ou ímpar será o jogador 1, independentemente de jogar primeiro ou não.\n")
    while opcaoj1 != '1' and opcaoj1 != 'x' and opcaoj1 != 'o' :
        opcaoj1 = input("Jogador 1, digite '1' para jogar primeiro ou digite o símbolo que deseja usar pra jogar:  ")
        if opcaoj1 == '1':
            print('\nO Jogador 1 será o primeiro a jogar.')
            primeiro = 'j1'
            while opcaoj2 != 'x' and opcaoj2 != 'o':
                opcaoj2 = input('Jogador 2, digite o símbolo que deseja usar pra jogar: ')
                if opcaoj2 == 'x':
                    print("\nO Jogador 2 jogará com 'x' e o Jogador 1 jogará com 'o'.")
                    opcaoj1 = 'o'
                elif opcaoj2 == 'o':
                    print("\nO Jogador 2 jogará com 'o' e o Jogador 1 jogará com 'x'.")
                    opcaoj1 = 'x'
                else:
                    print('Opção incorreta.')
        elif opcaoj1 == 'x':
            primeiro = 'j2'
            print("\nO Jogador 1 jogará com 'x'. O Jogador 2 jogará com 'o' e será o primeiro a jogar.")
            opcaoj2 = 'o'
        elif opcaoj1 == 'o':
            primeiro = 'j2'
            print("\nO Jogador 1 jogará com 'o'. O Jogador 2 jogará com 'x' e será o primeiro a jogar.")
            opcaoj2 = 'x'
        else:
            print('\nOpção incorreta.\n')

    #Mostrando o tabuleiro vazio antes da primeira jogada
    
    print(tabuleiro())
    
    #Começo das jogadas caso o Jogador 1 seja o primeiro a jogar

    if primeiro == 'j1':
        vezdejogar('jogador1')
        vezdejogar('jogador2')
        vezdejogar('jogador1')
        vezdejogar('jogador2')
        vezdejogar('jogador1')
        if vitoria():
            print('\nO Jogador 1 venceu!')
        else:
            vezdejogar('jogador2')
            if vitoria():
                print('\nO Jogador 2 venceu!')
            else:
                vezdejogar('jogador1')
                if vitoria():
                    print('\nO Jogador 1 venceu!')
                else:
                    vezdejogar('jogador2')
                    if vitoria():
                        print('\nO Jogador 2 venceu!')
                    else:
                        vezdejogar('jogador1')
                        if vitoria():
                            print('\nO Jogador 1 venceu!')
                        else:
                            print('\nDeu velha!')
    
    #Começo das jogadas caso o Jogador 2 seja o primeiro a jogar

    else:
        vezdejogar('jogador2')
        vezdejogar('jogador1')
        vezdejogar('jogador2')
        vezdejogar('jogador1')
        vezdejogar('jogador2')
        if vitoria():
            print('\nO Jogador 2 venceu!')
        else:
            vezdejogar('jogador1')
            if vitoria():
                print('\nO Jogador 1 venceu!')
            else:
                vezdejogar('jogador2')
                if vitoria():
                    print('\nO Jogador 2 venceu!')
                else:
                    vezdejogar('jogador1')
                    if vitoria():
                        print('\nO Jogador 1 venceu!')
                    else:
                        vezdejogar('jogador2')
                        if vitoria():
                            print('\nO Jogador 2 venceu!')
                        else:
                            print('\nDeu velha!')

    #Opção de jogar novamente
    
    repetir = input("Deseja jogar novamente? Se deseja, digite 's', senão digite 'n': ")

#Fim do jogo

print('\nO jogo acabou. Obrigado por jogar!')

#Fim do programa

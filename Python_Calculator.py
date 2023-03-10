# Calculadora em Python

print("\n******************* Python Calculator *******************\n")

print('Lista de operações disponivéis:\n\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão\n')

# 'Funções' já pré estabelecidas para as operações, com a 'palavra reservada' def
def soma(num1,num2):
    return (num1 + num2)

def subtracao(num1,num2):
    return (num1 - num2)

def multiplicacao(num1,num2):
    return (num1 * num2)

def divisao(num1,num2):
    return (num1 / num2)

#Função que retoma as perguntas e estabelecimento das variáveis
def perguntas():
    global operacao, num1, num2
    operacao = int(input('\nDigite a operação desejada: '))
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')

    # Tratamento do tipo de dado de acordo com o input do usuário (decimal ou inteiro)

    if ',' in num1:
        num1 = float(num1.replace(',','.'))
    else:
        num1 = int(num1)
    if ',' in num2:
        num2 = float(num2.replace(',','.'))
    else:
        num2 = int(num2)

# Adicionei o Satatus para conseguir aplicar um laço e fazer a calculadora contiuar rodando até o usuário não querer mais
status = 1

while (status == 1):        # Condicional para o laço
    perguntas()             #Função que retoma as perguntas iniciais
    if (operacao == 1):
        resultado = soma(num1,num2)
        print('\n{} + {} = {}'.format(num1,num2,resultado))
        status = int(input('\nDigite 0 para encerrar a calculadora ou 1 para mais uma operação: '))

    elif (operacao == 2):
        resultado = subtracao(num1,num2)
        print('\n{} - {} = {}'.format(num1,num2,resultado))
        status = int(input('\nDigite 0 para encerrar a calculadora ou 1 para mais uma operação: '))

    elif (operacao == 3):
        resultado = multiplicacao(num1,num2)
        print('\n{} x {} = {}'.format(num1,num2,resultado))
        status = int(input('\nDigite 0 para encerrar a calculadora ou 1 para mais uma operação: '))

    elif (operacao == 4):
        if num2 == 0:
            resultado = 'Infinito'
        else:
            resultado = divisao(num1,num2)
        print('\n{} ÷ {} = {}'.format(num1,num2,resultado))
        status = int(input('\nDigite 0 para encerrar a calculadora ou 1 para mais uma operação: '))

    else:
        print('\nNão existe esta opção')
        status = int(input('\nDigite 0 para encerrar a calculadora ou 1 para reiniciá-la: '))


''' NOVAS FEATURES

- Pensar no tipo de dados do resultado e do imput, pq o usuário pode querer fazer operação com decimal, ou com resultados decimais;
- Tratamento de erros, como divisão por 0
- Adicionar novas operações;
- Pensar em forma de disponibilizar isso com uma interface, de preferencia sem usar html e css

'''
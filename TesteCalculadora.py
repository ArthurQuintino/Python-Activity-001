
velocidade = 0


print("bem vindo a calculadora humildassa que calcula informações sobre: tempo de trajetos, km gastados e a sua velocidade")
pergunta = int(input("oque voce quer descobrir? 1 para tempo, 2 para distancia e 3 para a velocidade"))
print("obs: é apenas aceito numeros em metros ou segundos")
if pergunta == 3:
    distancia = int(input('\n qual a distancia'))
    tempo = int(input('\n qual o tempo'))
    resposta = distancia / tempo
    print(resposta,"m/s")
    questionario = input("\n converter para km/h?")
    if questionario == 'sim':
        print(resposta*3.6, "kms/h")
    elif questionario == 'não':
        print('adeus')


elif pergunta == 2:
    velocidade = int(input('\n qual a velocidade'))
    tempo = int(input('\n qual o tempo'))
    resposta = velocidade * tempo
    print(resposta,"M")
    questionario = input("\n converter para km?")
    if questionario == 'sim':
        print(resposta / 1000, "kms")
    elif questionario == 'não':
        print('adeus')



elif pergunta == 1 :
    distancia = int(input('qual a distancia'))
    velocidade = int(input('qual a velocidade'))
    resposta = distancia / velocidade
    print(resposta, "segundos")
    questionario = input("converter para horas?")
    if questionario == 'sim':
        print((resposta / 60) / 60, "horas")
    elif questionario == 'não':
        print('adeus')


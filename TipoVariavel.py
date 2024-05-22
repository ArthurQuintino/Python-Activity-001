codigo = 10
salario = 1000.00
nome = 'jose'

print("codigo: %d %f " % (codigo, salario))

lucas = 'lucas'
pergunta = input("voce é o lucas?")
if pergunta == 'sim':
    (print("ok"))

else: print("ok")

perguntaidade = int(input("quantos anos voce tem??"))
if perguntaidade <= 15 or perguntaidade <= 30:
    print("ta novinho ainda fi")
elif perguntaidade >= 30 and perguntaidade <= 70:
    print("ta velinho rapaiz")
else: print("ta muito velinho amigo se cuida >:)")

print("logo voce é o %s e tem %d anos" %(lucas, perguntaidade))

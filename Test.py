import json



'''Target Sistemas'''
print(30* '-')
print(1,'\n')


indice = 13
k = 0
SOMA = 0

while k < indice:
    k = k+ 1
    SOMA = SOMA + k
print("Soma vale: ", SOMA) 


print(30 * '-')
print(2)

def seq():
    fbn1 = 0
    fbn2 = 1
    
    num = int(input("Digite o valor: "))
    
    while fbn2 < num:
        fbn3 = fbn1 + fbn2
        fbn1 = fbn2
        fbn2 = fbn3
        
    if fbn2 == num:
        print(num, " Faz parte da sequência Fibonacci!")
        
    else:
        print(num, " Não faz parte da sequência de Fibonacci!")

seq()

print(30 * '-')
print(3)

def JSON():
    with open('dados.json', 'r') as resp:
        dados = json.load(resp)
        
    
    min_valor = 0.0
    max_valor = 0.0
    
    for i in dados:
        if i['valor'] > max_valor:
            max_valor = i['valor']
        if i['valor'] < min_valor and i['valor']  != 0.0:
            min_valor = i['valor']
    
    SOMA = 0.0
    NUMBER_DAYS = 0
    
    for d in dados:
        if d['valor'] != 0.0:
            SOMA += d['valor']
            NUMBER_DAYS += 1    
    MEDIA = SOMA / NUMBER_DAYS
    print(MEDIA)
    
    MEDIA_ACIMA = 0.0
    for d in dados:
        if d['valor'] > MEDIA:
            MEDIA_ACIMA += 1
    
    print(f"Menor valor faturado: R${min_valor:.2f}")
    print(f"Maior valor faturado: R${max_valor:.2f}")
    print(f"Número de dias em que o valor faturado foi acima da média: R${MEDIA_ACIMA:.2f}")
        
JSON()
print(30 * '-')
print(4)



print(30 * '-')
print(5)

def corda():
    palavra = "TANGAMANDAPIANO"
    
    print(palavra)
    print("String invertida: ", palavra[::-1])
corda()

    
def percent():

    valores_faturados = {
        "SP": 67836.43,
	    "RJ" : 6678.66,
	    "MG" : 2922.88,
	    "ES": 27165.48,
	    "Outros" : 19849.53
}
    
    total = sum(valores_faturados.values())
    print(total)
    
    for estado, valor in valores_faturados.items():
        percentual = (valor / valores_faturados) * 100
        print(f"{estado}, precentual R$: {percentual:.2f}%")
percent()
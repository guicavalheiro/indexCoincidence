abc = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

def read_document(name):
    
    with open(name) as f:
        lines = f.readline()
    
    return lines

def conta_letras(texto: str):

    abc_dict = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
        'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0 
    }

    size_text = len(texto)
    somatorio = 0
    for letra in abc:

        count = texto.count(letra)
        #print(f"{letra}: {count}")

        abc_dict[letra] = count
        somatorio += count * (count - 1)
    
    ic = somatorio / (size_text * (size_text - 1))
    return ic    

#import sys
#nome_texto = sys.argv[1]

for i in range (1, 8):
    nome_texto = f'T{i}.txt'
    texto = read_document(nome_texto)
    ic = conta_letras(texto)

    print(f'\nNome texto: {nome_texto}\nIC        : {ic}')



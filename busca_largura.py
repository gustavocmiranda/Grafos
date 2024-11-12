fila = []
largura = [-1, -1, -1, -1, -1, -1, -1, -1]
nivel = [0, 0, 0, 0, 0, 0, 0, 0]
pai = [None, None, None, None, None, None, None, None]

grafo = [[0, 1, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 0, 0, 0, 0],
         [1, 1, 0, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 1, 1, 0],
         [0, 0, 1, 1, 0, 1, 0, 1],
         [0, 0, 0, 1, 1, 0, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 1, 0, 1, 0]]

t = 0

def busca_largura(primeiro: int):
    global t
    fila.append(primeiro)
    largura[primeiro] = t
    while len(fila) != 0:
        v = fila.pop(0)
        for w in range(len(grafo[v])):
            if grafo[v][w] == 1:
                if largura[w] == -1:
                    print(f'visitar aresta {v}{w}')
                    pai[w] = v
                    nivel[w] = nivel[v]+1
                    t += 1
                    largura[w] = t
                    fila.append(w)
                else:
                    if nivel[v] == nivel[w]:
                        if pai[v] == pai[w]:
                            print(f'{v}{w} é aresta-irmao')
                        else:
                            print(f'{v}{w} é aresta-primo')
                    else:
                        if nivel[w] == nivel[v]+1:
                            print(f'{v}{w} é aresta-tio')




inicial = 0
busca_largura(inicial)

print(largura)
print(nivel)
print(pai)
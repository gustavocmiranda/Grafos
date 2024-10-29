pe = [0 for i in range(7)]
ps = [0 for i in range(7)]
pais = [-1 for i in range(7)]


""" vertices = [[0,1,1,0,0,0,0],
                [1,0,1,1,0,0,0],
                [1,1,0,1,1,0,0],
                [0,1,1,0,1,0,0],
                [0,0,1,1,0,1,1],
                [0,0,0,0,1,0,1],
                [0,0,0,0,1,1,0]] """

vertices = [[0, 1, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0],          #      A            E
            [1, 1, 0, 1, 0, 0, 0],          #     B C        F     G     
            [0, 0, 1, 0, 0, 0, 0],          #        D   
            [0, 0, 0, 0, 0, 1, 1],          #
            [0, 0, 0, 0, 1, 0, 0],          #
            [0, 0, 0, 0, 1, 0, 0]]




t = 0
def p(v:int):
    global t
    t = t + 1
    pe[v] = t
    for w in range(len(vertices[v])):
        if vertices[v][w] == 1:
            if pe[w] == 0:
                print(f'aresta visitada {v}{w}')
                pais[w] = v
                p(w)
            else:
                if (ps[w] == 0) and (pais[v] != w):
                    print(f'aresta de retorno {v}{w}')
    
    t = t + 1
    ps[v] = t




print(pe)
print(ps)
print(pais)

p(0)
for te in range(len(pe)):
    if pe[te] == 0:
        p(te)
print("=================================")

print(pe)
print(ps)
print(pais)
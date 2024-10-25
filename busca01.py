def visitar(v):
    marca[v] = 1
    for w in range(len(vertices[v])):
        if vertices[v][w] == 1 and marca[w] == 0:
            visitar(w)
        
vertices = [[0,1,1,0,0,0,0],
            [1,0,1,1,0,0,0],
            [1,1,0,1,1,0,0],
            [0,1,1,0,1,0,0],
            [0,0,1,1,0,1,1],
            [0,0,0,0,1,0,1],
            [0,0,0,0,1,1,0]]

marca = [0,0,0,0,0,0,0]

print(marca)
visitar(0)
print(marca)
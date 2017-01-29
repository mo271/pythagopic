import numpy as np

def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        for bar in  m:
            yield bar
        m = np.dot(m, uad)

def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim

sage: l=[list( i)[:-1]+[gcd([ZZ(j) for j in list(i)])] for i in gen_all_pyth_trips(200000) if i[0]<15001 and i[1]<15001];l=l+[[i[1],i[0],i[2]] for i in l]
sage: 
....: file1=open('./punkte.csv','w')
....: file1.write('a, b, c\n')
....: file2=open('./pripunkte.csv','w')
....: file2.write('a, b, c\n')
....: for line in l:
....:     if line[2]==1:
....:         file=file2
....:     else:
....:         file=file1
....:     file.write(str(line[0])+', '+str(line[1])+', '+str(line[2])+'\n')
....:     file.write(str(-line[0])+', '+str(line[1])+', '+str(line[2])+'\n')
....:     file.write(str(line[0])+', '+str(-line[1])+', '+str(line[2])+'\n')
....:     file.write(str(-line[0])+', '+str(-line[1])+', '+str(line[2])+'\n')
....: file1.close()
....: file2.close()


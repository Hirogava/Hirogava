with open ('example_100kb.csv') as f:
    n=f.readlines()
m=len(n)
a=[]
b=[]
c=[]
d=[]
doms = {}
for x in range(1,m,2):
    a.append(n[x].split(','))
for z in range(len(a)):
    b.append(a[z][2])
for w in range(len(b)):
    c.append(b[w].split('@'))
for y in range(len(c)):
    con=c[y][1]
    if con in doms:
        doms[con] += 1
    else:
        doms[con] = 1
out = []
for key, value in doms.items():
    out.append([value, key])
out.sort(key=lambda x: int(x[0]))
my_file = open("gotovo.csv",'w')
my_file.write("domain, count"+'\n')
for xxx in range(1,len(out)+1):
    my_file.write(f'{out[-xxx][1]}, {out[-xxx][0]}'+'\n')
my_file.close()
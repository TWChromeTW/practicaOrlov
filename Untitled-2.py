f = open("mat_dv.txt")

l = [elem for elem in f]

l8 = []
l9 = []
l10 = []
l11 = []
ballsAlg = []
ballsGeom = []


##print(l)

for i in l:
    st = i.split()
    
    ballsAlg.append(int(st[3]))
    ballsGeom.append(int(st[4]))

    ##print(st)

    if st[2] == '8':
        l8.append(st)
    if st[2] == '9':
        l9.append(st)
    if st[2] == '10':
        l10.append(st)
    if st[2] == '11':
        l11.append(st)

def aga(ll):
    all = []

    for elem in ll:
        all.append(int(elem[3] + elem[4]))
    
    for elem in ll:
        if max(all) == int(elem[3] + elem[4]):
            print(f"Победитель {elem[2]} - {elem[0]} {elem[1]}")

aga(l8)
print("!----!")

aga(l9)
print("!----!")

aga(l10)
print("!----!")

aga(l11)
print("!----!")

for elem in l:
    st = elem.split()

    if max(ballsAlg) == int(st[3]):
        print(f"Всеобщий победитель по алгебре - {st[0]} {st[1]}")

    if max(ballsGeom) == int(st[4]):
        print(f"Всеобщий победитель по геометрии - {st[0]} {st[1]}")

f.close()
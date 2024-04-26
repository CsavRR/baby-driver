class Fuvarok:
    def __init__(self, id, indulas, idotartam, tavolsag, viteldij, borravalo, fizetesmod):
        self.id = id
        self.indulas = indulas
        self.idotartam = idotartam
        self.tavolsag = tavolsag
        self.viteldij = viteldij
        self.borravalo = borravalo
        self.fizetesmod = fizetesmod

    def __str__(self):
        return f'azonosító: {self.id} \nindulás: {self.indulas} \nidotartam: {self.idotartam} \ntavolsag: {self.tavolsag} \nviteldíj: {self.viteldij} \nborravaló: {self.borravalo} \n fizetésmód: {self.fizetesmod}'

f = open('fuvar.csv', 'rt', encoding='UTF-8')
f.readline()
lista = []
for s in f:
    s = s.strip().split(';')
    lista.append(Fuvarok(s[0], s[1], s[2], s[3], float(s[4].replace(',','.')), float(s[5].replace(',','.')), s[6]))

print(f'3. feladat: {len(lista)} fuvar')

bevetel = 0
fuvarszam = 0
for azon in lista:
    if azon.id == '6185':
        bevetel += azon.viteldij + azon.borravalo
        fuvarszam += 1

print(f'4. feladat: {fuvarszam} fuvar alatt {bevetel}$')

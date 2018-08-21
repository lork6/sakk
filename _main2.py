#!/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
# coding=utf-8
import pygame
import os
import sys

print (sys.version + "sdfa")
kocka_meret = 100
per = r"\ "
mappa = os.path.dirname(__file__) + r"{}kepek{}".format(per[0], per[0])
formatum = ".png"

def lepesek_lista_Csinalasa():
    global fekete_lepesek_lista, feher_lepesek_lista
    try:
        lista += feher_lepesek_lista
    except:
        pass
    fekete_lepesek_lista = list()
    feher_lepesek_lista = list()
    for babu in obj_lista:
        babu.lepesEllenorzo()
        if babu.szine == "feher":
            feher_lepesek_lista += babu.hovaLephet_coord
        else:
            fekete_lepesek_lista += babu.hovaLephet_coord
    try:
        print(lista == feher_lepesek_listab)
    except:
        pass
    #print(fekete_lepesek_lista)
    #print(feher_lepesek_lista)

def kiraly_lephet_sakk(hova, kiraly_szine):
    if kiraly_szine == "feher":
        return not hova in fekete_lepesek_lista
    else:
        return not hova in feher_lepesek_lista
    # azaz léphet oda a király töbi esetben meg nem

def coordSzamolo(coord):
    # itt vissza adja azt a pontos coord-inátát amint a gép nek kell hogy kit tudja írni
    return (coord[0] * kocka_meret, coord[1] * kocka_meret)


def coordVissza(coord):
    # itt vissza adja azt a coord-inátát ami nekem kell a programhoz
    return (int(coord[0] / kocka_meret), int(coord[1] / kocka_meret))


def lepesSzamolo(coord, lepes):
    lista = list()
    for i in range(lepes):
        lep = [x + y for x, y in zip(coord, lepes[i])]
        lista.append(lep)


def hova_nem_lephet():
    # ez behatárolja táblámat és létre hoz egy olyan listát ami a pálya szélét jelenit
    lista = list()
    kulso = [0, 9]
    for i in range(len(kulso)):
        for j in range(9):
            lista.append((kulso[i], j))
            lista.append((j, kulso[i]))
    return lista


def vanOttBabu(x, y, vissza=True, delete=None):
    # meg nézi a függvény hogy az adot helye van-e bármien bábu
    coord = (x, y)
    if vissza:
        # ez csak néhány helyen kell ahol még nincsen vissza fejtve a coord
        coord = coordVissza(coord)
    for i in range(len(obj_lista)):

        if coord == obj_lista[i].coord:
            if delete is not None:
                return i
            return obj_lista[i]
    return False


def vanOttTabla(x, y, vissza=True):
    coord = [x, y]
    if vissza:
        coord = coordVissza(coord)
    for i in range(len(boardLista)):

        if coord == tuple(boardLista[i].coord):
            return boardLista[i]
    return False


class Babu(pygame.sprite.Sprite):
    szinek = ["feher", "fekete"]
    Ki_lephet = 0

    def __init__(self, szine, coord):
        super(Babu, self).__init__()
        self.lepet = 0
        self.szine = szine
        self.coord = coord
        self.hovaLephet_coord = list()
        self.hovaUt_coord = list()
        self.hanyadikLepes = 0

    @classmethod
    def valtas(cls):
        # melyik szin léphet azt állitom be
        if cls.Ki_lephet is 1:
            cls.Ki_lephet = 0
        else:
            cls.Ki_lephet = 1

    def lepesEllenorzo(self):
        for i in range(len(self.hovaLephet)):
            self.volt_coord = self.coord
            for j in range(8):
                adat = self.coordLepteto(i, self.volt_coord)
                if adat is not True:
                    break

    def coordAdd(self, i, coord):
        return tuple(map(lambda x, y: x + y, coord, self.hovaLephet[i]))

    def coordLepteto(self, hanyadik, coord=None, hova=None, sanc=False):
        if coord is None and hova is None and sanc == False:
            adat = self.coordAdd(hanyadik, self.coord)

        elif hova != None and sanc == False:
            adat = tuple(map(lambda x, y: x + y, self.coord, hova[hanyadik]))

        elif sanc == False:
            adat = tuple(map(lambda x, y: x + y, coord, self.hovaLephet[hanyadik]))

        elif sanc:
            adat = tuple(map(lambda x, y: x + y, coord, self.hovaSanc[hanyadik]))

        if hova is None:
            hova = True

        else:
            hova = False
        return self.hovaLephet_add(adat, hanyadik, hova)

    def hovaLephet_add(self, mit, hanyadik, hova=True):
        ottBabu = vanOttBabu(mit[0], mit[1], False)
        if mit in coordinatak and mit not in self.hovaLephet_coord and ottBabu == False and hova and self.nev != "kiraly":
            self.hovaLephet_coord.append(mit)
            self.volt_coord = mit
            return True
        # elif hova is not True and ottBabu is not False:

        elif ottBabu is not False:
            if self.nev is not "gyalog":
                if self.hovaLephet[hanyadik] in self.hovaUt and ottBabu.szine is not self.szine:
                    self.hovaLephet_coord.append(mit)

            elif ottBabu.szine is not self.szine and hova is not True:
                self.hovaLephet_coord.append(mit)

            return False

    def delete_babu(self):
        obj_lista.remove(self)
        babu_csapat.remove(self)

    def lephetRajzolo(self, valami=False):
        if self.lepet is 1 or valami:
            kor_lista.clear()
            kor_csapat.empty()
            self.lepet = 0

        elif self.lepet is 0:
            self.lepesEllenorzo()
            for i in range(len(self.hovaLephet_coord)):
                adat = Kor(self.hovaLephet_coord[i])
                kor_lista.append(adat)
                kor_csapat.add(adat)
            kor_csapat.draw(screen)

    def kepBetolt(self):
        self.image = pygame.Surface((kocka_meret, kocka_meret))
        # nem teljse :( még kellenek a képek hogy be tudjam másolni)
        self.image = pygame.image.load(os.path.join('kepek', self.kep_file))
        # töltse be a képet a meg felelő helyre
        self.rect = self.image.get_rect()
        self.set_position()

    def set_position(self, x=None, y=None, sanc=False):
        if x is not None and y is not None:
            coord = coordSzamolo((x, y))
            self.lepesEllenorzo()
            # self.lephetRajzolo()
            if (x, y) in self.hovaLephet_coord and self.szine == self.szinek[self.Ki_lephet]:
                vanOtt = vanOttBabu(x, y, False)
                Babu.valtas()
                if vanOtt is not False:
                    vanOtt.delete_babu()
                self.rect.x = coord[0]
                self.rect.y = coord[1]
                self.coord = (x, y)
                print(self.coord)
                lepesek_lista_Csinalasa()
                self.lepet += 1
                if self.nev is "gyalog":
                    self.lepesek()
                elif self.nev == "kiraly":
                    self.sancLepesek()
                self.hanyadikLepes += 1
                
                self.hovaLephet_coord = list()
                

            elif sanc:
                self.rect.x = coord[0]
                self.rect.y = coord[1]
                self.coord = (x, y)
                self.lepet += 1
                lepesek_lista_Csinalasa()

        else:
            self.coords = coordSzamolo(self.coord)
            self.rect.x = self.coords[0]
            self.rect.y = self.coords[1]

    def set_file_nev(self):
        self.kep_file = self.szine + "_" + self.nev + formatum


class Gyalog(Babu):
    def __init__(self, szine, coord):
        super(Gyalog, self).__init__(szine, coord)
        self.nev = "gyalog"
        self.set_file_nev()

        if self.coord[1] < 4:
            self.hovaLephet = [(0, 1), (0, 2)]
            self.hovaUt = [(1, 1), (-1, 1)]
        else:
            self.hovaLephet = [(0, -1), (0, -2)]
            self.hovaUt = [(1, -1), (-1, -1)]

    def lepesEllenorzo(self):
        self.hovaLephet_coord.clear()
        # k = 0

        for i in range(len(self.hovaLephet)):  # int(len(self.hovaLephet)/8)
            adat = self.coordLepteto(i)
            if adat is not True and self.nev is "gyalog":
                break

        for i in range(len(self.hovaUt)):
            # print(self.nev)
            adat = self.coordLepteto(i, hova=self.hovaUt)
        self.lepesek()

    def lepesek(self):  # egy ből pos nézzen és azzal dolgozon
        if self.hanyadikLepes == 0 and self.lepet is 1:
            self.hanyadikLepes += 1
            del (self.hovaLephet[1])


class Lo(Babu):
    def __init__(self, szine, coord):
        super(Lo, self).__init__(szine, coord)
        # super(Babu, self).__init__()
        self.hovaLephet = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
        self.hovaUt = self.hovaLephet
        self.nev = "lo"
        self.set_file_nev()

    def lepesEllenorzo(self):
        self.hovaLephet_coord.clear()
        for i in range(len(self.hovaLephet)):
            adat = self.coordLepteto(i)
            if adat != True and self.nev is "gyalog": # kitalálni mért kell az id hogy ha gyalog a neve akkor break eljen?
                break

class Bastja(Babu):
    def __init__(self, szine, coord):
        super(Bastja, self).__init__(szine, coord)
        # super(Babu, self).__init__()
        self.hovaLephet = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        # self.hovaLephet_kitolt()
        # print(self.hovaLephet, "lista")
        self.hovaUt = self.hovaLephet
        self.nev = "bastja"
        self.set_file_nev()


class Futo(Babu):
    def __init__(self, szine, coord):
        super(Futo, self).__init__(szine, coord)
        self.hovaLephet = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        self.hovaUt = self.hovaLephet
        self.nev = "futo"
        self.set_file_nev()


class Kiraly(Babu):  # TODO: oldara lépés nem müködik
    def __init__(self, szine, coord):
        super(Kiraly, self).__init__(szine, coord)
        self.hovaLephet = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        self.hovaSanc = [(1, 0), (2, 0), (-1, 0), (-2, 0), (3, 0), (4, 0), (-3, 0)]
        self.hovaUt = self.hovaLephet
        self.nev = "kiraly"
        self.sanc = False
        self.set_file_nev()

    def hovaLephet_add(self, mit, hanyadik, hova=True):
        ottBabu = vanOttBabu(mit[0], mit[1], False)
        ottSakk = kiraly_lephet_sakk(mit, self.szine)
        if ottBabu is not False and ottSakk:
            if self.hovaLephet[hanyadik] in self.hovaUt and ottBabu.szine != self.szine:  # if self.nev == "kiraly":  # and hanyadik <= 3:
                self.hovaLephet_coord.append(mit)

        elif hanyadik <= 8 and ottSakk:
            self.hovaLephet_coord.append(mit)
            self.volt_coord = mit
        else:
            return False

    def lepesek(self):  # Todo: csak akor lehessen ketött lépni ha a bástja felé lép ( lehet hogy nem müködik amásik irányba mert öda hármat kell lépni)
        if self.hanyadikLepes == 0 and self.lepet == 0:
            self.hovaSanc_coords = list()
            for i in range(len(self.hovaSanc)):
                self.volt_coord = self.coord

                print("SIKER")
                # nem növekszika táv. csak maga körul nézi meg
                # adat = self.coordLepteto(i, self.volt_coord, sanc=True)
                # if adat is not True:
                #   break

    def sancLepesek(self):
        if self.hanyadikLepes == 0:
            babuhelyek = [(self.coord[0] + 1, self.coord[1]), (self.coord[0] - 1, self.coord[1]), (self.coord[0] - 2, self.coord[1]),
                          (self.coord[0] - 3, self.coord[1]), (self.coord[0] + 1, self.coord[1])]  # elso a jobra lévö szoval balra kell léptetni a bástját
            for j, i in enumerate(babuhelyek):
                print(i)
                ottBabu = vanOttBabu(i[0], i[1], False)

                try:
                    if ottBabu.nev == "bastja":
                        if j == 0:
                            coord = (i[0] - 2, i[1])
                        else:
                            coord = (i[0] + 3, i[1])
                        print("áthejezve")
                        # Todo: most a király messzebb tud lépni és magáva tudja vinni a bástját is
                        ottBabu.set_position(coord[0], coord[1], sanc=True)
                        break
                except:
                    pass


class Kiralyno(Babu):
    def __init__(self, szine, coord):
        super(Kiralyno, self).__init__(szine, coord)
        self.nev = "kiralyno"
        self.hovaLephet = [(0, 1), (1, 0), (0, -1), (-1, 0),
                           (1, 1), (-1, -1), (1, -1), (-1, 1)]
        self.hovaUt = self.hovaLephet
        self.set_file_nev()


class Tabla(pygame.sprite.Sprite):
    def __init__(self, szine, coord):
        super(Tabla, self).__init__()
        self.coord = coord
        self.szine = szine
        self.alapszin = szine
        self.kivalasztottSzin = (75, 255, 0)
        self.korSzine = szine
        self.elso = 0
        self.image = pygame.Surface((kocka_meret, kocka_meret))
        self.kitolt()
        self.rect = self.image.get_rect()
        # self.image = pygame.draw.rect(screen, self.szine, [self.coord[0]*lepes,self.coord[1]*lepes,lepes,lepes])
        self.rect.x = coord[0] * lepes
        self.rect.y = coord[1] * lepes

    def kitolt(self):
        self.image.fill(self.szine)

    def szined(self):
        return self.szine

    def helyed(self):
        return self.coord

    def szinValtasZ(self):
        self.szine = self.kivalasztottSzin
        # self.korSzine = self.kivalasztottSzin
        self.kitolt()

    def szinValtasS(self):
        self.szine = self.alapszin
        self.kitolt()


class Kor(pygame.sprite.Sprite):
    def __init__(self, coord):
        super(Kor, self).__init__()
        r = 15
        self.coord = coord
        # self.szine = szine
        # self.alapszin = szine
        self.kivalasztottSzin = (75, 255, 0)
        self.elso = 0
        self.image = pygame.Surface((r, r))
        self.szine = self.kivalasztottSzin
        self.kitolt()

        self.rect = self.image.get_rect()

        self.rect.x = coord[0] * lepes + 50 - 7
        self.rect.y = coord[1] * lepes + 50 - 7

    def kitolt(self):
        self.image.fill(self.szine)
    # self.image.convert()

    def szined(self):
        return self.szine

    def helyed(self):
        return self.coord


def tabla_coords():
    lista = list()
    for i in range(0, 8):
        for j in range(0, 8):
            lista.append((j, i))
    return lista


coordinatak = tabla_coords()
tabla_erendez = [1, 2, 3, 4, 5, 3, 2, 1,
                 6, 6, 6, 6, 6, 6, 6, 6,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 6, 6, 6, 6, 6, 6, 6, 6,
                 1, 2, 3, 4, 5, 3, 2, 1]

szinek = ["fekete", "feher"]
obj_lista = list()
# print(coordinatak)
j = 0
babuk = ["Bastja", "Lo", "Futo", "Kiralyno", "Kiraly", "Gyalog"]
for i in range(len(tabla_erendez)):
    tabla_id = tabla_erendez[i] - 1
    if i > 18:
        j = 1
    if tabla_id >= 0:
        if tabla_id is 0:
            babu = Bastja(szinek[j], coordinatak[i])
        if tabla_id is 1:
            babu = Lo(szinek[j], coordinatak[i])
        if tabla_id is 2:
            babu = Futo(szinek[j], coordinatak[i])
        if tabla_id is 3:
            babu = Kiralyno(szinek[j], coordinatak[i])
        if tabla_id is 4:
            babu = Kiraly(szinek[j], coordinatak[i])
        if tabla_id is 5:
            babu = Gyalog(szinek[j], coordinatak[i])
        obj_lista.append(babu)

lepesek_lista_Csinalasa()

pygame.init()

meret = 800
WHITE = (220, 220, 220)
BLACK = (78, 60, 7)
szin = (WHITE, BLACK)

screen = pygame.display.set_mode((meret, meret), pygame.RESIZABLE)
pygame.display.set_caption('Sakk 2')
clock = pygame.time.Clock()
JatekVege = False
babu_csapat = pygame.sprite.Group()
kocka_csapat = pygame.sprite.Group()
kor_csapat = pygame.sprite.Group()
kor_lista = list()
kantintVa = 0

szinValtas = 0
lepes = 100
boardLista = list()
for i in range(len(obj_lista)):
    obj_lista[i].kepBetolt()
    babu_csapat.add(obj_lista[i])

for x in range(0, 8):
    for y in range(0, 8):
        valami = Tabla(szin[szinValtas], [x, y])
        # kor = Kor(szin[szinValtas], [x,y])
        # valami = pygame.draw.rect(screen, szin[szinValtas], [x*lepes,y*lepes,lepes,lepes])
        boardLista.append(valami)
        # kor_lista.append(kor)
        kocka_csapat.add(valami)
        # kor_csapat.add(kor)
        if szinValtas == 0:
            szinValtas = 1
        else:
            szinValtas = 0
    if szinValtas == 0:
        szinValtas = 1
    else:
        szinValtas = 0
babu_csapat.draw(screen)
0
old_adat = 0
while not JatekVege:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            JatekVege = True
        if pygame.mouse.get_pressed()[0]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                adat = vanOttBabu(mx, my)
                adat2 = vanOttTabla(mx, my)
                mcoord = coordVissza((mx, my))
                # print(mcoord)
                if kantintVa is 1:
                    if old_adat == adat:
                        kantintVa = 0

                    else:
                        old_adat.set_position(mcoord[0], mcoord[1])
                        kantintVa = 0
                    old_adat.lephetRajzolo(valami=True)
                    old_adat2.szinValtasS()
                # old_adat2[1].szinValtasS()

                elif adat is not False:
                    kantintVa = 1
                    old_adat = adat
                    old_adat2 = adat2
                    adat2.szinValtasZ()
                    adat.lephetRajzolo()
            # adat2[1].szinValtasZ()

    # screen.fill(BLACK)
    # for i in range(len(boardLista)):
    # boardLista[i].update()
    kocka_csapat.draw(screen)
    babu_csapat.draw(screen)
    kor_csapat.draw(screen)
    pygame.display.update()

    clock.tick(30)


pygame.quit()
quit()

# babu = Babu("fekete", (1, 2))
# print(babu.lepesSzama)
# print(sys.version)

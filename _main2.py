import pygame
import os
import sys


kicka_meret = 100
per = r"\ "
mappa = os.path.dirname(__file__) + r"{}kepek{}".format(per[0], per[0])
formatum = ".png"


class Babu(pygame.sprite.Sprite):
    szinek = ["feher", "fekete"]
    Ki_lephet = 0

    @classmethod
    def valtas(cls):
        if cls.Ki_lephet is 1:
            cls.Ki_lephet = 0
        else:
            cls.Ki_lephet = 1

    def __init__(self, szine, coord):
        super(Babu, self).__init__()
        self.__lepet = 0
        self.__szine = szine
        self.__coord = coord
        self.__hovaLephet_coord = list()
        self.__hovaUt_coord = list()

    def delete_babu(self):
        obj_lista.remive(self)
        babu_csapat.remove(self)

    @property
    def lepesSzama(self):
        return self.__lepet

    @property
    def szine(self):
        return self.__szine

    @property
    def helyed(self):
        return self.__coord

    def lephetRajzolo(self, valami=False):
        if self.lepet is 1 or valami:
            kor_lista.clear()
            kor_csapat.empty()
            self.lepet = 0

        elif self.lepet is 0:
            self.lepesSzamolo()
            for i in range(len(self.hovaLephet_coord)):
                adat = Kor(self.hovaLephet_coord[i])
                kor_lista.append(adat)
                kor_csapat.add(adat)
            kor_csapat.draw(screen)

    def kepBetolt(self):
        self.image = pygame.Surface((kocka_meret, kocka_meret))
        # nem teljse :( még kellenek a képek hogy be tudjam másolni)
        print("121")
        print(mappa)
        self.image = pygame.image.load(mappa + self.kep_file)
        # töltse be a képet a meg felelő helyre
        self.rect = self.image.get_rect()
        self.set_position()

    def set_file_nev(self):
        self.kep_file = self.szine + "_" + self.nev + formatum

class Gyalog(Babu):
    def __init__(self, szine, coord):
        super(Gyalog, self).__init__()


babu = Babu("fekete", (1, 2))
print(babu.lepesSzama)
print(sys.version)

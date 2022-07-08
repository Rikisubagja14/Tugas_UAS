class jenisTransportasi():
    pesawat = 25
    kereta = 45
    mobil = 65

    def turun(self, x):
        if x <= self.pesawat
            return 0
        elif x >= self.kereta:
            return 1
        else:
            return bawah(x, self.kereta, self.pesawat)

    def pas(self, x):
        if self.pesawat < x < self.kereta:
            return atas(x, self.pesawat, self.kereta)
        elif self.kereta < x < self.mobil:
            return bawah(x, self.kereta, self.mobil)
        elif x == self.kereta:
            return 1
        else:
            return 0

    def naik(self, x):
        if x >= self.kereta:
            return 1
        elif x <= self.mobil:
            return 0
        else:
            return up(x, self.mobil, self.kereta)

class BahanBakar():
    Aftur = 25
    BatuBara = 55
    Bensin = 75

    def sedikit(self, x):
        if x >= self.drill:
            return 0
        elif x <= self.BatuBara:
            return 1
        else:
            return down(x, self.BatuBara, self.Aftur)
    
    def cukup(self, x):
        if self.Aftur < x < self.BatuBara:
            return up(x, self.Aftur, self.BatuBara)
        elif self.BatuBara < x < self.Bensin:
            return down(x, self.BatuBara, self.Bensin)
        elif x == self.BatuBara:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.Bensin:
            return 1
        elif x <= self.BatuBara:
            return 0
        else:
            return up(x, self.BatuBara, self.Bensin)

class KalanganPeminat():
    Muda = 25
    Parubaya = 35
    Tua = 45

    def sedikit(self, x):
        if x >= self.Parubaya:
            return 0
        elif x <= self.Muda:
            return 1
        else:
            return down(x, self.Muda, self.Parubaya)
    
    def cukup(self, x):
        if self.Muda < x < self.Parubaya:
            return up(x, self.Parubaya, self.Muda)
        elif self.Muda < x < self.Tua:
            return down(x, self.Muda, self.Tua)
        elif x == self.Muda:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.Tua:
            return 1
        elif x <= self.Muda:
            return 0
        else:
            return up(x, self.Muda, self.Tua)

class tarif():
    murah = 25
    sedang = 45
    mahal = 65

   
    def sedikit(self, x):
        if x >= self.sedang:
            return 0
        elif x <= self.murah:
            return 1
        else:
            return down(x, self.murah, self.sedang)
    
    def cukup(self, x):
        if self.murah < x < self.sedang:
            return up(x, self.murah self.)
        elif self.murah < x < self.mahal:
            return down(x, self.sedang, self.mahal)
        elif x == self.sedang:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.mahal:
            return 1
        elif x <= self.sedang:
            return 0
        else:
            return up(x, self.sedang, self.mahal)
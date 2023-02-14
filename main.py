import copy
# ===================================== Hatalar Kısmı =================================

class BiletAdetKontrol:
    def __init__(self,adet):
        self.adet = adet
    
    def KucukDegerHatasi(self):
        raise Exception(f"Sıfırdan Küçük Bilet Alamazsınız. Girilen Değer: {self.adet}\n")
    def BuyukDegerHatasi(self):
        raise Exception(f"Ondan Fazla Bilet Alamazsınız. Girilen Değer: {self.adet}\n")

# ===================================== Dosya İşlem Kısmı =================================
class DosyaDegerAl:
    def __init__(self,kategori):
        self.kategori = kategori
        self.MaxBilet = 0
        self.BiletFiyat = 0
        self.minBilet1 = 0
        self.maxBilet1 = 0
        self.yuzdeDeger1 = 0
        self.minBilet2 = 0
        self.maxBilet2 = 0
        self.yuzdeDeger2 = 0
    def DegerAl(self):
        with open('indirim.txt', 'r') as f:
            deger = {}
            minBiletAdet = []
            maxBiletAdet = []
            uygulanacakYuzde = []
            
            for line in f:
                deger = line.split("-")
                
                if 'M' in deger:
                    self.MaxBilet = int(deger[1])
                if self.kategori in deger:
                    if self.kategori == '4':
                        if len(deger) > 2:
                            minBiletAdet.append(deger[1])
                            maxBiletAdet.append(deger[2])
                            uygulanacakYuzde.append(deger[3])
                        else:
                            self.BiletFiyat = int(deger[1])
                    else:
                        if len(deger) > 2:
                            minBiletAdet.append(deger[1])
                            maxBiletAdet.append(deger[2])
                            uygulanacakYuzde.append(deger[3])
                        else:
                            self.BiletFiyat = int(deger[1])
        if self.kategori == '4': # 4. Kategori için özel durum.
            self.minBilet1 = int(minBiletAdet[0])
            self.maxBilet1 = int(maxBiletAdet[0])
            self.yuzdeDeger1 = int(uygulanacakYuzde[0])

            self.minBilet2 = int(minBiletAdet[1])
            self.maxBilet2 = int(maxBiletAdet[1])
            self.yuzdeDeger2 = int(uygulanacakYuzde[1])

            self.minBilet3 = int(minBiletAdet[2])
            self.maxBilet3 = int(maxBiletAdet[2])
            self.yuzdeDeger3 = int(uygulanacakYuzde[2])
        else:
            self.minBilet1 = int(minBiletAdet[0])
            self.maxBilet1 = int(maxBiletAdet[0])
            self.yuzdeDeger1 = int(uygulanacakYuzde[0])

            self.minBilet2 = int(minBiletAdet[1])
            self.maxBilet2 = int(maxBiletAdet[1])
            self.yuzdeDeger2 = int(uygulanacakYuzde[1])
            
# ===================================== Kategorilerde Kullanılan Fonksiyonlar Kısmı =================================          
def BiletAdet(MaxBilet):
        while True:
            adet = int(input("Bilet Adetini Giriniz (1-10) -> "))
            Kontrol = BiletAdetKontrol(adet)
            if(adet < 0):
                try:
                    Kontrol.KucukDegerHatasi()
                except Exception as error:
                    print(error)
            else:
                if(adet > MaxBilet):
                    try:
                        Kontrol.BuyukDegerHatasi()
                    except Exception as error:
                        print(error)
                else:
                    return adet
def ToplamUcretHesapla(kategori,biletAdet,minBilet1,minBilet2,minBilet3,maxBilet1,maxBilet2,maxBilet3,BiletFiyat,yuzdeDeger1,yuzdeDeger2,yuzdeDeger3):
        toplam = 0
        if kategori == '4': # 4. Kategori için özel durum
            if(biletAdet >= minBilet1 and biletAdet <= maxBilet1):
                toplam += (BiletFiyat * biletAdet)
                indirimliFiyat = toplam - ((yuzdeDeger1/100)*toplam)
            elif(biletAdet >= minBilet2 and biletAdet <= maxBilet2):
                toplam += (BiletFiyat * biletAdet)
                indirimliFiyat = toplam - ((yuzdeDeger2/100)*toplam)
            elif(biletAdet >= minBilet3 and biletAdet <= maxBilet3):
                toplam += (BiletFiyat * biletAdet)
                indirimliFiyat = toplam - ((yuzdeDeger3/100)*toplam)
        else:
            if(biletAdet >= minBilet1 and biletAdet <= maxBilet1):
                toplam += (BiletFiyat * biletAdet)
                indirimliFiyat = toplam - ((yuzdeDeger1/100)*toplam)
            elif(biletAdet >= minBilet2 and biletAdet <= maxBilet2):
                toplam += (BiletFiyat * biletAdet)
                indirimliFiyat = toplam - ((yuzdeDeger2/100)*toplam)
            else:
                toplam += (BiletFiyat * biletAdet)
                indirimliFiyat = toplam
        return indirimliFiyat
# ===================================== 1. ve 3. Kategori Kısmı =================================
class Kategori1:
    def __init__(self,kategori,ilkSira,ilkKoltuk):
        # Default olarak alınan Kategori Bilgisi, Kategorinin ilk sırası ve ilk koltuk numarası
        self.kategori = kategori
        self.ilkSira = int(ilkSira)
        self.ilkKoltuk = int(ilkKoltuk)
        # Koltukları oluşturmak için kullanılacak matris listeler
        self.liste1 = [ [0] * 10 for i in range(10) ]
        # Dosyadan çekdiğimiz değerleri gerekli atamalar yapmılası
        DosyaDeger = DosyaDegerAl(self.kategori)
        DosyaDeger.DegerAl()
        self.MaxBilet = DosyaDeger.MaxBilet
        self.BiletFiyat = DosyaDeger.BiletFiyat
        self.minBilet1 = DosyaDeger.minBilet1
        self.maxBilet1 = DosyaDeger.maxBilet1
        self.yuzdeDeger1 = DosyaDeger.yuzdeDeger1
        self.minBilet2 = DosyaDeger.minBilet2
        self.maxBilet2 = DosyaDeger.maxBilet2
        self.yuzdeDeger2 = DosyaDeger.yuzdeDeger2
        self.minBilet3 = 0
        self.maxBilet3 = 0
        self.yuzdeDeger3 = 0
        # Toplam Biletin Hesaplanması
        rows = len(self.liste1)
        cols = len(self.liste1[0])
        self.toplamBilet = rows * cols
        self.kalanBilet = self.toplamBilet
        self.toplamCiro = 0

    # Kategori 1 ve Kategori 3'ün koltuklarının oluşturulduğu kısım
    def KoltukOluşturma(self):
        for i in range(10):
            for j in range(10):
                self.liste1[i][j] = "-"

    # Rezerve işleminin yapıldığı kısım
    def KoltukDuzenle(self):
        print("Kalan Bilet Adeti = ",self.kalanBilet)
        biletAdet = self.BiletAdet()
        sayac = 0
        print(biletAdet)
        if(biletAdet < self.kalanBilet):
            print("Rezerve Edilen Koltuklar (Sıra-Koltuk) : ",end="")
            for i in range(10):
                if(biletAdet == sayac):
                    break
                for j in range(10):
                    if(self.liste1[i][j] != "X"):
                        self.liste1[i][j] = "X"
                        print(f"{i+self.ilkSira} - {j+self.ilkKoltuk},",end=" ")
                        sayac += 1
                        self.kalanBilet -= 1
                    if(biletAdet == sayac):
                        break
            # Ödenecek ücretin hesaplandığı kısım
            gercekTutar = int(biletAdet) * int(self.BiletFiyat)
            toplamUcret = self.ToplamUcret(biletAdet)
            print(f"Bilet Adeti = {biletAdet}, Toplam Ücret = {gercekTutar}, İndirim Tutarı = {gercekTutar - toplamUcret}, Ödenecek Ücret = {toplamUcret}")
            self.toplamCiro += toplamUcret
        else:
           print(f"Kalan bilet sayısından fazla değer girdiniz.Kalan Bilet {self.kalanBilet}, Girilen Değer: {biletAdet}")

    # 1. Kategori ve 3. Kategori En son Koltuk düzeni Gosterilen kısım.
    def KoltukGoster(self):
        for i in range(10):
            for j in range(10):
                print(self.liste1[i][j],end="")
            print("\n",end="")
    def KoltukGoster_2(self):
        list1 = copy.deepcopy(self.liste1)
        return list1

    # Bilet sayısının alındığı ve kontrol edildiği kısım.
    def BiletAdet(self):
        adet = BiletAdet(self.MaxBilet)
        return adet

    # Ücretin hesaplandığı ve kontrol edildiği kısım.
    def ToplamUcret(self,biletAdet):
        indirimliFiyat = ToplamUcretHesapla(self.kategori,biletAdet,self.minBilet1,self.minBilet2,self.minBilet3,self.maxBilet1,self.maxBilet2,
        self.maxBilet3,self.BiletFiyat,self.yuzdeDeger1,self.yuzdeDeger2,self.yuzdeDeger3)
        return indirimliFiyat

# ===================================== 2. ve 4. Kategori Kısmı ====================================
class Kategori2:
    def __init__(self,kategori,ilkSira1,ilkKoltuk1,ilkSira2,ilkKoltuk2):
        # Default olarak alınan Kategori Bilgisi, Kategorinin ilk sırası ve ilk koltuk numarası
        self.kategori = kategori
        self.ilkSira1 = int(ilkSira1)
        self.ilkKoltuk1 = int(ilkKoltuk1)
        self.ilkSira2 = int(ilkSira2)
        self.ilkKoltuk2 = int(ilkKoltuk2)
        # Koltukları oluşturmak için kullanılacak matris listeler
        self.liste1 = [ [0] * 5 for i in range(10) ]
        self.liste2 = [ [0] * 5 for i in range(10) ]
        # Dosyadan çekdiğimiz değerleri gerekli atamalar yapmılası
        DosyaDeger = DosyaDegerAl(self.kategori)
        DosyaDeger.DegerAl()
        self.MaxBilet = DosyaDeger.MaxBilet
        self.BiletFiyat = DosyaDeger.BiletFiyat
        self.minBilet1 = DosyaDeger.minBilet1
        self.maxBilet1 = DosyaDeger.maxBilet1
        self.yuzdeDeger1 = DosyaDeger.yuzdeDeger1
        self.minBilet2 = DosyaDeger.minBilet2
        self.maxBilet2 = DosyaDeger.maxBilet2
        self.yuzdeDeger2 = DosyaDeger.yuzdeDeger2
        self.minBilet3 = 0
        self.maxBilet3 = 0
        self.yuzdeDeger3 = 0
        if self.kategori == '4': # Kategori 4 için özel durum
            self.minBilet3 = DosyaDeger.minBilet3
            self.maxBilet3 = DosyaDeger.maxBilet3
            self.yuzdeDeger3 = DosyaDeger.yuzdeDeger3
        # Toplam Biletin Hesaplanması
        rows = len(self.liste1)
        cols = len(self.liste1[0])
        self.toplamBilet = rows * cols * 2
        self.kalanBilet = self.toplamBilet
        self.toplamCiro = 0

    # Ketegori 2 ve Kategori 4'ün oluşturulduğu kısım
    def KoltukOluşturma(self):
        for i in range(10):
            for j in range(5):
                self.liste1[i][j] = "-"
                self.liste2[i][j] = "-"

    # Rezerve işlemi yapılan kısım
    def KoltukDuzenle(self):
        print("Kalan Bilet Adeti = ",self.kalanBilet)
        biletAdet = self.BiletAdet()
        sayac = 0
        if(biletAdet < self.kalanBilet):
            print("Rezerve Edilen Koltuklar (Sıra-Koltuk) : ",end="")
            for i in range(10):
                if(biletAdet == sayac):
                    break
                # liste1 kontrolü
                for j in range(4,-1,-1):
                    if(self.liste1[i][j] != "X"):
                        self.liste1[i][j] = "X"
                        print(f"{i+self.ilkSira1} - {j+self.ilkKoltuk1},",end=" ")
                        sayac += 1
                        self.kalanBilet -= 1
                    if(biletAdet == sayac):
                        break
                if(biletAdet == sayac):
                    break
                # liste2 kontrol
                for j in range(5):
                    if(self.liste2[i][j] != "X"):
                        self.liste2[i][j] = "X"
                        print(f"{i+self.ilkSira2} - {j+self.ilkKoltuk2},",end=" ")
                        sayac += 1
                        self.kalanBilet -= 1
                    if(biletAdet == sayac):
                        break
                if(biletAdet == sayac):
                    break
            # Ödenecek ücretin hesaplandığı kısım
            gercekTutar = int(biletAdet) * int(self.BiletFiyat)
            toplamUcret = self.ToplamUcret(biletAdet)
            print(f"Bilet Adeti = {biletAdet}, Toplam Ücret = {gercekTutar}, İndirim Tutarı = {gercekTutar - toplamUcret}, Ödenecek Ücret = {toplamUcret}")
            self.toplamCiro += toplamUcret
        else:
            print(f"Kalan bilet sayısından fazla değer girdiniz.Kalan Bilet {self.kalanBilet}, Girilen Değer: {biletAdet}")

    # 2. ve 4. Kategori Koltuklar 1. Kısım.
    def KoltukGoster1(self):
        for i in range(10):
            for j in range(5):
                print(self.liste1[i][j],end="")
            print("\n",end="")
    def KoltukGoster1_2(self):
        list1 = copy.deepcopy(self.liste1)
        return list1

    # 2. ve 4. Kategori Koltuklar 2. Kısım.
    def KoltukGoster2(self):
        for i in range(10):
            for j in range(5):
                print(self.liste2[i][j],end="")
            print("\n",end="")
    def KoltukGoster2_2(self):
        list2 = copy.deepcopy(self.liste2)
        return list2

    # Bilet sayısının alındığı ve kontrol edildiği kısım.
    def BiletAdet(self):
        adet = BiletAdet(self.MaxBilet)
        return adet

    # Ücretin hesaplandığı ve kontrol edildiği kısım.
    def ToplamUcret(self,biletAdet):
        indirimliFiyat = ToplamUcretHesapla(self.kategori,biletAdet,self.minBilet1,self.minBilet2,self.minBilet3,self.maxBilet1,self.maxBilet2,self.maxBilet3
        ,self.BiletFiyat,self.yuzdeDeger1,self.yuzdeDeger2,self.yuzdeDeger3)
        return indirimliFiyat

# ===================================== Main Kısım ====================================
# Kategorilerde koltukların oluşumu. Kategori classının nesnesinde sırayla alınan değerler: 
# -> ('Kategori Numarası',Kategorideki ilk Sırası, Kategorideki ilk Koltuk Numarası) 
kategori1 = Kategori1('1',1,6)
kategori2 = Kategori2('2',1,1,1,16)
kategori3 = Kategori1('3',11,6)
kategori4 = Kategori2('4',11,1,11,16)

kategori1.KoltukOluşturma()
kategori2.KoltukOluşturma()
kategori3.KoltukOluşturma()
kategori4.KoltukOluşturma()
durum = False
while durum != True:
    print("=========== Ana Menü ===========")
    print("1. Rezervasyon\n2. Salonu Yazdır\n3. Yeni Etkinlik\n4. Toplam Ciro\n0. Çıkış")
    secim = int(input("Seçiminiz ? -> "))
    if(secim == 0):
        durum = True
    else:
        if(secim == 1):
            print("======= Rezervasyon ========")
            kategori = int(input("Kategori (1-4): "))
            if(kategori == 1):
                kategori1.KoltukDuzenle()
                kategori1.KoltukGoster()
            elif(kategori == 2):
                kategori2.KoltukDuzenle()
                kategori2.KoltukGoster1()
                kategori2.KoltukGoster2()
            elif(kategori == 3):
                kategori3.KoltukDuzenle()
                kategori3.KoltukGoster()
            elif(kategori == 4):
                kategori4.KoltukDuzenle()
                kategori4.KoltukGoster1()
                kategori4.KoltukGoster2()
            else:
                print("Hatalı Kategori Seçimi Yaptınız!")
            
            durum = False

        elif(secim == 2):
            print("======= Salon ========")
            # Kategorilerin Koltuk düzeninin alındığı kısım
            salonK2_1 = kategori2.KoltukGoster1_2()
            salonK1_1 = kategori1.KoltukGoster_2()
            salonK2_2 = kategori2.KoltukGoster2_2()
            salonK4_1 = kategori4.KoltukGoster1_2()
            salonK3_1 = kategori3.KoltukGoster_2()
            salonK4_2 = kategori4.KoltukGoster2_2()
            
            # Koltukların düzenli şekilde birleştirildiği kısım
            for i in range(10):
                salonK2_1[i].extend(salonK1_1[i])
                salonK2_1[i].extend(salonK2_2[i])
            for i in range(10):
                salonK4_1[i].extend(salonK3_1[i])
                salonK4_1[i].extend(salonK4_2[i])

            # Salonun yazdırıldığı kısım
            for r in range(10):
                for c in range(20):
                    print(salonK2_1[r][c],end="")
                print("\n",end="")

            for r in range(10):
                for c in range(20):
                    print(salonK4_1[r][c],end="")
                print("\n",end="")
            
            # Salon görünümünü güncel tutmak için sıfırlama
            salonK2_1.clear()
            salonK1_1.clear()
            salonK2_2.clear()
            salonK4_1.clear()
            salonK3_1.clear()
            salonK4_2.clear()
            durum = False

        elif(secim == 3):
            print("======= Yeni Etkinlik ========")
            kategori1 = Kategori1('1',1,6)
            kategori2 = Kategori2('2',1,1,1,16)
            kategori3 = Kategori1('3',11,6)
            kategori4 = Kategori2('4',11,1,11,16)

            kategori1.KoltukOluşturma()
            kategori2.KoltukOluşturma()
            kategori3.KoltukOluşturma()
            kategori4.KoltukOluşturma()
            print("Yeni Etkinlik Başlatıldı.")
            print("\n")
            durum = False
        elif(secim == 4):
            print("======= Salon Ciro ========")
            SalonCiro = 0
            SalonCiro += kategori1.toplamCiro + kategori2.toplamCiro + kategori3.toplamCiro + kategori4.toplamCiro
            print("Salonun Toplam Cirosu = ",SalonCiro)
            print("\n")

            durum = False
        else:
            print("Hatalı Seçim Yaptınız!")
            durum = False
    

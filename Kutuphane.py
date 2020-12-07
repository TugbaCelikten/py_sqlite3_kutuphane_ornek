import sqlite3
import time

class Kitap():
    def __init__(self,isim,yazar,yayinevi,tur,baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self):
        return "Kitap ismi: {}\n Yazar: {} \n Yayınevi: {} \n Tür: {} \n Baskı: {}".format(self.isim,
                                                                                           self.yazar,
                                                                                           self.yayinevi,
                                                                                           self.tur,
                                                                                           self.baski)

class Kutuphane():
    def __init__(self):
        self.DBBaglantiOlustur()

    def DBBaglantiOlustur(self):
        # -----------"KUTUPHANE.db" isimli veritabanini olusturuyoruz ve baglaniyorz-----------
        self.baglanti = sqlite3.connect("KUTUPHANE.db")

        # ----- olusturdugumuz veritabani uzerinde islemleri gerceklestirecek cursor olusturuyoruz-------
        self.cursor = self.baglanti.cursor()

        # ----- olusturdugumuz cursor ile tablolari olusturuyoruz-------
        srg_crt_table = "Create table if not exists KITAP (isim TEXT, yazar TEXT, yayinevi TEXT, tur TEXT, baski INT)"

        self.cursor.execute(srg_crt_table)
        self.baglanti.commit()

    def DBBaglantiKapat(self):
        self.baglanti.close()

    def KitapListele(self):
        srg_kitap_listele = "select * from KITAP"
        self.cursor.execute(srg_kitap_listele)
        lst_kitap = self.cursor.fetchall()

        if(len(lst_kitap) == 0):
            print("Kütüphanede hiç kitap bulunmuyor")
        else:
            for i in lst_kitap: # i_demet
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def KitapSorgula(self,isim):
        srg_kitap_sorgula = "select * from KITAP where isim = ?"
        self.cursor.execute(srg_kitap_sorgula,(isim,))
        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Aradıgınız kitap bulunamadı")
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)

    def KitapEkle(self,kitap):
        srg_kitap_ekle = "insert into KITAP values(?,?,?,?,?)"
        self.cursor.execute(srg_kitap_ekle,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))
        self.baglanti.commit()

    def KitapSil(self,isim):
        srg_kitap_sil = "delete from KITAP where isim = ?"
        self.cursor.execute(srg_kitap_sil,(isim,))
        self.baglanti.commit()

    def BaskiYukselt(self,isim):
        srg_baski_sorgula = "select * from KITAP where isim = ?"
        self.cursor.execute(srg_baski_sorgula,(isim,))

        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Bu isimde bir kitap bulunamadi")
        else:
            baski = kitaplar[0][4]
            baski+=1
            srg_baski_yukselt = "update KITAP set baski = ? where isim = ?"
            self.cursor.execute(srg_baski_yukselt,(baski,isim))
            self.baglanti.commit()

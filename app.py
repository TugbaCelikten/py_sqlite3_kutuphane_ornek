from Kutuphane import *

print("""--------------------------
Kütüphaneye hoşgeldiniz..

İşlemler:
1. Tüm Kitapları Listele
2. Kitap Sorgula
3. Kitap Ekle
4. Kitap Sil
5. Baski Yükselt

Çıkmak için 'q' tuşuna basınız
--------------------------""")

kutuphane = Kutuphane()

while True:
    islem = input("Yapmak istediğiniz işlem: ")

    if(islem == "q"):
        print("Program sonlandırılıyor..")
        break

    elif(islem == "1"):
        kutuphane.KitapListele()

    elif (islem == "2"):
        isim = input("Almak istediginiz kitap ismini giriniz")
        print("Aradiginiz kitap sorgulanıyor")
        time.sleep(2)
        kutuphane.KitapSorgula(isim)

    elif (islem == "3"):
        print("Lütfen eklemek istediğiniz kitap bilgilerini giriniz")
        isim = input("Kitap Adı:")
        yazar = input("Yazar:")
        yayinevi = input("Yayınevi:")
        tur = input("Tur:")
        baski = int(input("Baski Yili: "))
        kitap = Kitap(isim,yazar,yayinevi,tur,baski)
        print("Kitap ekleniyor. Lütfen bekleyiniz..")
        time.sleep(2)
        kutuphane.KitapEkle(kitap)
        print("Ekleme işlemi tamamlanmistir.")

    elif (islem == "4"):
        isim = input("Silmek istediginiz kitap ismini giriniz:")
        cvp = input("{} adli kitabi silmek üzeresiniz. Devam etmek istiyor musunuz?(E/H)".format(isim))
        cvp = cvp.upper()
        if(cvp == "E"):
            print("Kitap siliniyor.. Lütfen bekleyiniz")
            time.sleep(2)
            kutuphane.KitapSil(isim)
            print("Silme işlemi başarıyla tamamlanmıştır.")

    elif (islem == "5"):
        isim = input("Lütfen baskisini yukseltmek istediginiz kitap ismini giriniz:")
        # kitaplar = kutuphane.KitapSorgula(isim)
        # for i in kitaplar:
        #     if(isim == i[0][1]):
        #         print("{} isimli kitabin {} olan baskisi {} olarak guncellenecektir. "
        #               "Devam etmek istiyor musunuz?(E/H)".format(i[0][1],i[0][4]))
        #         cvp = cvp.upper()
        #         if(cvp == "E"):
        kutuphane.BaskiYukselt(isim)
        print("Baski yukseltme islemi basari ile gerceklesmistir.")

    else:
        print("Geçersiz bir işlem numarası girdiniz. "
              "Lütfen yapmak istediğiniz işlem numarasını 'İşlemler' listesinden kontrol ederek tekrar giriniz. ")
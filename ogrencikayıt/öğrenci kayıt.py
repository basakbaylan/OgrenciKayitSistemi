ogrenciAdList=[]
ogrenciSoyadList=[]
ogrenciCinsiyetList=[]
ogrenciDogumyılList=[]
ogrenciTcList=[]


def OgrenciKayıt(ogrenciAdList, ogrenciSoyadList, ogrenciCinsiyetList, ogrenciDogumyılList, ogrenciTcList):
    ad = input("İsim:")
    soyad = input("Soyad:")
    cinsiyet = input("Cinsiyet kız/erkek:")
    while True:
        dogumtarihi = input("Doğum Tarihi:")
        if dogumtarihi.isdigit() and len(dogumtarihi) == 8:
            ogrenciDogumyılList.append(dogumtarihi)
            break
        else:
            print("Lütfen sadece rakam girin ve eksik girmediğinizden emin olun")
    while True:
        tc = input("Tc Giriniz:")
        if tc.isdigit() and len(tc) == 11:
            ogrenciTcList.append(tc)
            break
        else:
            print("Geçersiz TC. lÜTFEN GEÇERLİ BİR TC girin")
    print("KAYIT TAMAMLANDI.")
    ogrenciAdList.append(ad)
    ogrenciSoyadList.append(soyad)
    ogrenciCinsiyetList.append(cinsiyet)

def OgrenciGuncelle(ogrenciAdList, ogrenciSoyadList, ogrenciCinsiyetList, ogrenciDogumyılList, ogrenciTcList):
    if not ogrenciAdList or not ogrenciSoyadList or not ogrenciCinsiyetList or not ogrenciDogumyılList:
        print("Listeler boş. Önce öğrenci ekleyin.")
        return

    try:
        indeks = int(input("Güncellemek istediğiniz öğrencinin indeksini girin: "))
        ogrenciAdList[indeks] = input("Yeni adı giriniz: ")
        ogrenciSoyadList[indeks] = input("Yeni soyad giriniz: ")
        ogrenciCinsiyetList[indeks] = input("Yeni cinsiyet giriniz: ")
        yeni_dogum_yili = input("Yeni doğum yılı giriniz: ")
        if yeni_dogum_yili.isdigit():
            ogrenciDogumyılList[indeks] = int(yeni_dogum_yili)
        else:
            print("Geçersiz doğum yılı. Lütfen doğru bir tam sayı girin.")

        yeni_tc = input("Yeni TC kimlik numarası giriniz: ")
        if yeni_tc.isdigit():
            ogrenciTcList[indeks] = int(yeni_tc)
        else:
            print("Geçersiz TC kimlik numarası. Lütfen doğru bir tam sayı girin.")

        print("Güncelleme işlemi gerçekleştirildi.")
        print(ogrenciAdList, ogrenciSoyadList, ogrenciCinsiyetList, ogrenciDogumyılList, ogrenciTcList)

    except IndexError:
        print("Geçersiz indeks. Lütfen geçerli bir indeks girin.")
    except ValueError:
        print("Geçersiz değer. Lütfen doğru formatta bir değer girin.")


def OgrenciSilme(ogrenciAdList,ogrenciSoyadList,ogrenciCinsiyetList, ogrenciDogumyılList, ogrenciTcList):
    if not ogrenciAdList or not ogrenciSoyadList or not ogrenciCinsiyetList or not ogrenciDogumyılList:
        print("Listeler boş. Önce öğrenci ekleyin.")
        return
    silinecek_indeks=int(input("Silmek istediğiniz öğrencinin indeksini girin"))
    ogrenciAdList.pop(silinecek_indeks)
    ogrenciSoyadList.pop(silinecek_indeks)
    ogrenciCinsiyetList.pop(silinecek_indeks)
    ogrenciDogumyılList.pop(silinecek_indeks)
    ogrenciTcList.pop(silinecek_indeks)
    print("Silme işlemi gerçekleştirildi")
    print(ogrenciAdList, ogrenciSoyadList, ogrenciCinsiyetList, ogrenciDogumyılList, ogrenciTcList)


while True:
    print("---ÖĞRENCİ KAYIT SİSTEMİNE HOŞGELDİNİZ---")
    secim=int(input("1-Öğrenci Kayıt\n2-Öğrenci Kayıt Güncelleme\n3-Öğrenci Silme\n4-Öğrenci Listesi\nLütfen Seçim Yapın:"))
    if secim==1:
        print("Öğrenci Kayıt")
        OgrenciKayıt(ogrenciAdList, ogrenciSoyadList, ogrenciCinsiyetList, ogrenciDogumyılList,ogrenciTcList)

    elif secim==2:
        print("Öğrenci Kayıt Güncelleme")
        OgrenciGuncelle(ogrenciAdList, ogrenciSoyadList, ogrenciCinsiyetList, ogrenciDogumyılList,ogrenciTcList)


    elif secim==3:
        print("Öğrenci Silme")
        OgrenciSilme(ogrenciAdList, ogrenciSoyadList, ogrenciCinsiyetList, ogrenciDogumyılList,ogrenciTcList)

    elif secim==4:
        print("Öğrenci Listesi")
        print(ogrenciAdList,ogrenciSoyadList,ogrenciCinsiyetList,ogrenciDogumyılList,ogrenciTcList)

    else:
        print("Girilen rakama ait bir seçenek bulunmuyor")
        continue
try:
    secim = int(input("1-Öğrenci Kayıt\n2-Öğrenci Kayıt Güncelleme\n3-Öğrenci Silme\n4-Öğrenci Listesi\nLütfen Seçim Yapın:"))
except:
    print("HATALI TUŞLAMA")






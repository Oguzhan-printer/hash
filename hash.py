# 1. Aşağıdaki listedeki tekrar eden elemanları kaldırarak benzersiz bir liste oluşturup yazdırın:
numbs = [8, 3, 8, 1, 2, 3, 5, 5]

for i in numbs:
    if numbs.count(i) > 1:
        numbs.remove(i)
print(numbs)


# 2.Aşağıdaki sözlüğe "ülke": "Japonya" anahtar-değerini ekleyin ve sözlüğü yazdırın:
sanatci = {"isim": "Haruki"}
sanatci["ülke"] = "Japonya"
print(sanatci)

#3.Kullanıcıdan bir kitap adı ve kaç tane almak istediğini alın. Stok yeterliyse siparişi tamamlayın, değilse "Yetersiz stok" mesajı verin:
kitap_stok = {"1984": 4, "Sefiller": 2, "Martı": 5}

a =(input('Almak istediğiniz kitap adı:'))
b =input('Kaç tane almak istersiniz: ')

if a in kitap_stok and int(b) <= kitap_stok[a] :
   c =kitap_stok[a] - int(b)
   print(f"{b} tane {a} kitabınızın stokta {c} tane bulunmaktadır siparişiniz alınmıştır.")
else:
    print("Yetersiz stok")

#4.Aşağıdaki sözlükten 2015 yılından sonra çıkmış ürünleri listeleyin:
urunler = {
"Telefon": {"yil": 2019},
"Televizyon": {"yil": 2014},
"Laptop": {"yil": 2021}
}
for i in urunler:
    if urunler[i]["yil"] > 2015:
        print(i)


#5.Aşağıdaki sözlükte "hobiler" listesine "yüzme" ifadesini ekleyin ve sonucu yazdırın:,
profil = {
"isim": "Nihan",
"hobiler": ["yoga", "resim"]
}
profil["hobiler"].append("yüzme")
print(profil)

#6.Aşağıdaki sözlükte yer alan tüm anahtar-değer çiftlerini key: value formatında satır satır yazdırın:
kurs = {
"ad": "Veri Bilimi",
"süre": "6 hafta",
"seviye": "Orta"
}

for anahtar, deger in kurs.items():
    print(f"{anahtar} : {deger}")


#7.Aşağıdaki sözlükten puanı 85 ve üzeri olan öğrencilerin adlarını yazdırın:
notlar = {
"Ekin": 91,
"Barış": 76,
"Deniz": 88,
"Umut": 63
}

for i in notlar:
    if notlar[i] >= 85:
        print(i)


#8.Kullanıcıdan bir şehir adı alıp aşağıdaki sözlükten bilgi getirin. Eğer şehir bulunmuyorsa “Veri yok” yazsın:
sehir_bilgi = {
"Berlin": {"nüfus": 3_600_000},
"Madrid": {"nüfus": 3_200_000}
}

bilgi = input("Nüfusunu öğrenmek istediğiniz şehiri giriniz: ")
if bilgi in sehir_bilgi:
  print(sehir_bilgi[bilgi]["nüfus"])
else:
  print("Veri yok")

#9.Aşağıdaki sözlükte her ürünün fiyatına %15 zam yaparak güncellenmiş sözlüğü yazdırın:
fiyatlar = {
"masa": 1200,
"sandalye": 450,
"lamba": 300
}

for key, value in fiyatlar.items():
  zam = value * 1.15
  print(f"{key} Yeni fiyat: {zam}")

#10.İç içe geçmiş sözlükte “aktif” olan projeleri listeleyin:
projeler = {
"ProjeX": {"durum": "aktif", "süre": 3},
"ProjeY": {"durum": "tamamlandı", "süre": 6},
"ProjeZ": {"durum": "aktif", "süre": 2}
}

for i in projeler:
    if projeler[i] ["durum"] == "aktif":
       print("Aktif projeler:" , i)

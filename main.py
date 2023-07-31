import random
print('''

    ######### TAS KAGIT MAKAS OYUNU  ########
    
    Oynamak icin tas, kagit veya makas yaziniz
    
         Oyundan cikmak icin q yaziniz!
        
           ~~~~IYI EGLENCELER~~~~


      ''')



# Bir fonksiyon belirlenir ve Random kutuphanesi kullanilir.
def pc_secimi():
    secim = random.choice([
                            "tas",
                            "kagit",
                            "makas"
                          ])
    return secim

oyuncu_skoru = 0
pc_skoru = 0

# Oyunu sonsuz bir döngü içinde başlat.

while True:

    # Oyuncunun hamlesini al ve küçük harflere dönüştür.

    oyuncu_hamlesi = input("tas? kagit? makas? ").lower()

    # Eğer oyuncu "bitti" yazarsa, oyunu bitir ve çık.

    if oyuncu_hamlesi == "bitti":
        print("Oyun Bitmistir. Iyi Gunler Dilerim")
        break
    # Geçersiz bir giriş yapıldığında oyuncuya uyarı ver ve tekrar al.

    if oyuncu_hamlesi not in ["tas", "kagit", "makas"]:
        print("Lutfen Dogru karakter giris yapin")
        continue
    # Oyuncu ve bilgisayarın hamleleri karşılaştırılarak skorlar belirlenir.

    pc_hamle = pc_secimi()
    print("Bilgisayar:", pc_hamle)

    # Bilgisayarın seçimi ile oyuncunun seçimi aynıysa, berabere.

    if pc_hamle == oyuncu_hamlesi:
        print("Berabere!")

    # Bilgisayar kazandıysa skorunu arttır ve kullanıcıya bildir.

    elif pc_hamle == "tas" and oyuncu_hamlesi == "makas":
        print("Kaybettiniz")
        pc_skoru +=1
    elif pc_hamle == "kagit" and oyuncu_hamlesi == "tas":
        print("Kaybettiniz")
        pc_skoru +=1
    elif pc_hamle == "makas" and oyuncu_hamlesi == "kagit":
        print("Kaybettiniz")
        pc_skoru +=1

    else:

        print(" Kazandiniz :)")
        oyuncu_skoru += 1
        # Oyuncu kazandıysa skorunu arttır ve kullanıcıya bildir.
        # Oyuncu ve bilgisayarın mevcut skorlarını göster.

    print ("Oyuncu Skoru:", oyuncu_skoru, "\nPc skoru:", pc_skoru)

# Bilgisayar veya Oyuncu 5 puan kazanırsa oyunu bitir ve döngüyü kır.

    if oyuncu_skoru == 5 or pc_skoru == 5:
        if oyuncu_skoru == 5:
            print("****___ KAZANDINIZ ___****, Ama bugun de sansliydin")
        else:
            print("Ben kazandim, Hamd olsun =)")
        break

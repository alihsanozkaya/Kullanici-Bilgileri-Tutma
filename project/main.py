import databaseCreating, databaseProcess
def menuFonksiyonu(secim):
    if secim == 1:
        dataBaseAdi = input("Database adı: ")
        databaseCreating.dataBaseOlustur(dataBaseAdi)
    elif secim == 2:
        databaseProcess.sutunlariOlusturma()
    elif secim == 3:
        databaseProcess.veriGetirme()
    elif secim == 4:
        databaseProcess.tumVerileriGetirme()
    else:
        print("Geçersiz seçim")
        
def gosterme():
    print("1- Database oluşturmak")
    print("2- Databaseye sütun oluşturmak")
    print("3- Databasedeki isteninlen sütundaki veriyi getirmek")
    print("4- Databasedeki tüm verileri getirmek")
gosterme()
secim = int(input("Seçiminizi yapınız: "))
menuFonksiyonu(secim)

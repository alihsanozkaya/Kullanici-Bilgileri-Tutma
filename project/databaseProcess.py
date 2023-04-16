import sqlite3

def sutunlariOlusturma():
    dataBaseAdi = input("Eklemek istediğiniz databasenin adı: ")
    baglan = sqlite3.connect(f'{dataBaseAdi}', uri=True)
    tabloAdi = input("Tablo adı giriniz: ")
    tabloDegiskenleriSayisi = int(input("Kaç sütun oluşturacaksınız: "))
    imlec = baglan.cursor()
    sutunAdlari = []
    sutunTipleri = []
    for sutun in range(tabloDegiskenleriSayisi):
        sutunAdi = input("Sütun adı: ")
        sutunAdlari.append(sutunAdi)
        sutunTipi = input("Sütun tipi: ")
        sutunTipleri.append(sutunTipi)
    sutunAdlariTup = tuple(sutunAdlari)
    sutunTipleriTup = tuple(sutunTipleri)
    sutunlar = ', '.join([f"{sutunAdi} {sutunTipi}" for sutunAdi, sutunTipi in zip(sutunAdlariTup, sutunTipleriTup)])
    imlec.execute(f"CREATE TABLE IF NOT EXISTS {tabloAdi}({sutunlar})")
    veriTuple = tuple(input(f"{sutunAdi} verisini girin: ") for sutunAdi in sutunAdlari)
    imlec.execute(f"INSERT INTO {tabloAdi} VALUES{veriTuple}")
    baglan.commit()
    baglan.close()
  
def veriGetirme():
    dataBaseAdi = input("Verileri almak istediğiniz databasenin adı: ")
    tabloAdi = input("Tablo adı giriniz: ")
    sutunAdi = input("Sutün adı giriniz: ")
    
    baglan = sqlite3.connect(f'{dataBaseAdi}', uri=True)
    imlec = baglan.cursor()
    
    imlec.execute(f"SELECT {sutunAdi} FROM {tabloAdi}")
    
    veriler = imlec.fetchall()
    
    for veri in veriler:
        print(veri)
        
    baglan.commit()
    baglan.close()

def tumVerileriGetirme():
    dataBaseAdi = input("Verileri almak istediğiniz databasenin adı: ")
    tabloAdi = input("Tablo adı giriniz: ")
    
    baglan = sqlite3.connect(f'{dataBaseAdi}', uri=True)
    imlec = baglan.cursor()
    
    imlec.execute(f"PRAGMA table_info({tabloAdi})")
    sutunBilgileri = imlec.fetchall()
    sutunBasliklari = [sutun[1] for sutun in sutunBilgileri]
    
    imlec.execute(f"SELECT * FROM {tabloAdi}")
    
    veriler = imlec.fetchall()
    
    print(sutunBasliklari)
    for veri in veriler:
        print(veri)
        
    baglan.commit()
    baglan.close()

    
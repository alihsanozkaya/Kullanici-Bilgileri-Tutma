import sqlite3

def dataBaseOlustur(adi):
    olustur = sqlite3.connect(f'{adi}')
    olustur.close()
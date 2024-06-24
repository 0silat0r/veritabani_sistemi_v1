import os
import subprocess
import time
import sqlite3

def clear():
    os.system("clear")

clear()
while True:
    try:
        print("Veritabani Yönetim Terminali")
        print("0silat0r tarafindan programlandi.")
        
        secim = int(input("1- Veritabani Olustur\n2- Kolon Olustur\n3- Yönetim Panelini Ac\n4- Cikis\nLutfen seciminizi yapin\n: "))
        if secim == 1:
            veritabani_adi = input("Olusturulacak Veritabaninin Adi: ")
            subprocess.run(["touch", f"{veritabani_adi}.db"])
            print("Veritabani olusturuldu!")
            time.sleep(3)
            clear()
        
        elif secim == 2:
            veritabani_adi = input("Baglanti Yapilacak Veritabani: ")
            connection = sqlite3.connect(veritabani_adi)
            print("Baglanti saglandi!\n")
            cur = connection.cursor()
            
            kolon_adi = input("Olusturulacak Kolonun Adi: ")
            cur.execute(f"CREATE TABLE IF NOT EXISTS {kolon_adi}(ID integer PRIMARY KEY, ADI text NOT NULL, SOYADI text NOT NULL)")
            cur.close()
            connection.close()
            print("Kolon olusturuldu!")
            time.sleep(3)
            clear()    
        
        elif secim == 3:
            subprocess.run(["python3","program.py"])
            print("Yönetim paneli kapatildi!")
            time.sleep(3)
            clear()
                    
        elif secim == 4:
            print("Cikis yapiliyor lutfen bekleyin...")
            time.sleep(3)        
            clear()
            break

    except ValueError:
        print("Lutfen sayisal bir deger girmeye calisin.")
        continue
    except KeyboardInterrupt:
        print("\nProgramdan cikis yapildi!")
        break

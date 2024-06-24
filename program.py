from tkinter import *
import tkinter as tk
import sqlite3

program = Tk()
program.title("Veritabani Yönetim Sistemi")
program.geometry("750x350")

bilgi = Label(program, text="")
def veri_ekle():
    veritabani_dosyasi = e1.get()
    kolon_adi = e2.get()
    sira = e3.get()
    adi = e4.get()
    soyadi = e5.get()
    
    connection = sqlite3.connect(veritabani_dosyasi)
    cur = connection.cursor()
    cur.execute(f"INSERT INTO {kolon_adi} (ID, ADI, SOYADI) VALUES({sira}, '{adi}', '{soyadi}')")
    cur.close()
    connection.close()
    
    bilgi = Label(program, text="Veri Eklendi!", fg="black", font=("tahoma",15,"normal"))
    bilgi.pack()
    bilgi.after(3000, lambda: bilgi.destroy())

    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

main_label = Label(program, text="Veritabani Yönetim Sistemi", fg="white", bg="green", font=("tahoma", 15, "normal"))
main_label.pack()

l1 = Label(program, text="Baglanti Kurulacak Veritabani Dosyasinin Adi:", fg="black", font=("tahoma",15,"normal"))
l1.pack(padx=(0,280))
e1 = Entry(program, width="30")
e1.pack(padx=(0,520))

l2 = Label(program, text="Kolon Adi:", fg="black", font=("tahoma", 15, "normal"))
l2.pack(padx=(0,620))
e2 = Entry(program, width="30")
e2.pack(padx=(0,520))

l2 = Label(program, text="ID:", fg="black", font=("tahoma", 15, "normal"))
l2.pack(padx=(0,700))
e3 = Entry(program, width="30")
e3.pack(padx=(0,520))

l3 = Label(program, text="Adi:", fg="black", font=("tahoma",15,"normal"))
l3.pack(padx=(0,690))
e4 = Entry(program, width="30")
e4.pack(padx=(0, 520))

l4 = Label(program, text="Soyadi:", fg="black", font=("tahoma",15,"normal"))
l4.pack(padx=(0,660))
e5 = Entry(program, width="30")
e5.pack(padx=(0,520))

b1 = Button(program, text="Veri Ekle", fg="white", bg="green", font=("tahoma",15,"normal"), command=veri_ekle)
b1.pack(padx=(0,620))

b2 = Button(program, text="Cikis", fg="white", bg="red", font=("tahoma",15,"normal"), command=program.destroy, width="15")
b2.pack(padx=(0,570))

program.mainloop()

 from _typeshed import Self
from typing import DefaultDict


class mahasiswa:
    '''dasar kelas untuk semua karyawan'''
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim): #definisi fungsi
        self.nama = nama
        self.nim = nim
        mahasiswa.jumlah_mahasiswa += 1 #atribut private
        
    def tampilkan_jumlah(self):
        print("total mahasiswa:", mahasiswa.jumlah_mahasiswa)

    def tampilkan_profil(self):
        print("Nama :",self.nama)
        print("nim :", self.nim)

# Membuat objek pertama dari kelas mahasiswa
mahasiswa1 = mahasiswa("bagas",312110053)
# Membuat objek kedua dari kelas mahasiswa
mahasiswa2 = mahasiswa("warmad",312110532)

mahasiswa1.tampilkan_profil()
mahasiswa2.tampilkan_profil()
print("Total mahasiswa :", mahasiswa.jumlah_mahasiswa)

delattr(mahasiswa1, 'nama')


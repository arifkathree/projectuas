from model.daftar_nilai import tambah_data, hapus_data, ubah_data
from view.view_nilai import cari

def masukan_data():
    print("================")
    print("| Masukan Data |")
    print("================")

    nama = input("Masukan Nama        = ")
    nim = int(input("Masukan NIM         = "))
    tugas = int(input("Masukan Nilai Tugas = "))
    uts = int(input("Masukan Nilai UTS   = "))
    uas = int(input("Masukan Nilai UAS   = "))
    nilai_akhir = float(30/100*tugas)+(35/100*uts)+(35/100*uas)
    tambah_data(nama, nim, tugas, uts, uas, nilai_akhir)

def cari_hapus():
    hapus_data(input("Masukan Data Yang Ingin Dihapus = "))

def cari_ubah():
    ubah_data(input("Masukan Nama Yang Ingin Di Ubah = "))

    print("=====================")
    print("| Masukan Data Baru |")
    print("=====================")

    nama = input("Masukan Nama        = ")
    nim = int(input("Masukan NIM         = "))
    tugas = int(input("Masukan Nilai Tugas = "))
    uts = int(input("Masukan Nilai UTS   = "))
    uas = int(input("Masukan Nilai UAS   = "))
    nilai_akhir = float(30/100*tugas)+(35/100*uts)+(35/100*uas)
    tambah_data(nama, nim, tugas, uts, uas, nilai_akhir)
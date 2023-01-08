data = {}

def tambah_data(nama, nim, tugas, uts, uas, nilai_akhir):
    data[nama] = nama, nim, tugas, uts, uas, nilai_akhir

def ubah_data(nama):
    if nama in data.keys():
        del data[nama]
    else:
        print(f"Data Dengan Nama {nama} Tidak Ditemukan!")

def hapus_data(nama):
    if nama in data.keys():
        del data[nama]
        print(f"Data Dengan Nama {nama} Berhasil Dihapus")
        return True
    else:
        print(f"Data Dengan Nama {nama} Tidak Ditemukan! ")
        print()
        return False


def cari_data():
    from view.view_nilai import cari
    cari(input("Masukan Nama yang ingin di Cari = "))
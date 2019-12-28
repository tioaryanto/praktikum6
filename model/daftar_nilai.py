data = {}


def tambah_data(nama,nim,tugas,uts,uas):
    akhir = round((float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35), 2)
    data[nama] = nama,nim,tugas,uts,uas,akhir


def edit_data(nama):
    if nama in data.keys():
        del data[nama]
        print("\n===Masukan Pembaruan Data===")
        from view.input_nilai import inputan
        inputan()
    else:
        print("==========================")
        print("| Data {} tidak ditemukan |".format(nama))
        print("==========================")
        print("    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")


def cari_data(nama):
    if nama in data.keys():
        print("\n|===================================================================|")
        print("|      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
        print("|===================================================================|")
        print("| {0:15} | {1:16} | {2:5} | {3:5} | {4:5} | {5:5} |".format(nama, data[nama][1], data[nama][2],data[nama][3],data[nama][4], data[nama][5]))
        print("|===================================================================|")
    else:
        print("===========================")
        print("| Data {} tidak ditemukan |".format(nama))
        print("===========================")


def delete_data(nama):
    if nama in data.keys():
        del data[nama]
        print('nama berhasil di hapus')
        return True
    else:
        print("===========================")
        print("| Data {} tidak ditemukan |".format(nama))
        print("===========================")
    return False
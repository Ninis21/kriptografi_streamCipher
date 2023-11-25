#enkripsi ASCII dengan kode biner
def enkripsi_ascii(teks):
    hasil_enkripsi = ""
    for karakter in teks:
        kode_ascii = ord(karakter)
        kode_biner = bin(kode_ascii)[2:]  #mengabaikan awalan "0b" pada hasil biner
        hasil_enkripsi += kode_biner + " "
    return hasil_enkripsi

#dekripsi ASCII dari kode biner
def deskripsi_ascii(teks):
    teks_biner = teks.split()
    hasil_deskripsi = ""
    for biner in teks_biner:
        kode_ascii = int(biner, 2)
        karakter = chr(kode_ascii)
        hasil_deskripsi += karakter
    return hasil_deskripsi

if __name__ == '__main__':
    print ('-----------------------------------')
    print ('    Nama        : Munis Zulhusni   ')
    print ('    Nim         : A11.2021.13693   ')
    print ('    Kelas       : A11.4302         ')
    print ('-----------------------------------')   
    
    option = int (input ('1. Enkripsi\n2. Deskripsi\nPilih Option              : '))
    if option == 1:
        teks = input ('Masukan pesan (Plaintext) : ')
        hasil_enkripsi = enkripsi_ascii(teks)
        print('Hasil Enkripsi            :',hasil_enkripsi)
        
    elif option == 2:
        teks = input ('Masukan pesan (Chipertext): ')
        hasil_deskripsi = deskripsi_ascii(teks)
        print('Hasil Deskripsi           :',hasil_deskripsi)
    else:
        print ('TIDAK VALID! PILIH OPSI LAIN!')    


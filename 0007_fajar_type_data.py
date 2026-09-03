#tugas1
# Deklarasi variabel
nama = "Fajar kurniawan" # nama → string
umur = 18                # umur → integer
berat = 55.5             # berat → float

# Menampilkan data
print("Nama   :", nama)
print("Umur   :", umur, "tahun")
print("Berat  :", berat, "Kg")

#tugas2
angka_string = "123"
angka_float = 45.67
angka_integer = 89

# 1. Konversi angka_string menjadi integer
hasil_1 = int(angka_string)


# 2. Konversi angka_float menjadi integer
hasil_2 = int(angka_float)

# 3. Konversi angka_integer menjadi float
hasil_3 = float(angka_integer)

# 4. Konversi angka_integer menjadi string
hasil_4 = str(angka_integer)

# Menampilkan hasil
print((hasil_1), "type=", type(hasil_1))
print((hasil_2), "type=", type(hasil_2))
print((hasil_3), "type=", type(hasil_3))
print((hasil_4), "type=", type(hasil_4))

#3. Buat program yang:
#a. Meminta input usia (integer)
#b. Meminta input tinggi badan (float)
#c. Meminta input nama (string)


# TUGAS NOMOR 3
usia = int(input("Masukkan usia anda :"))              # Meminta input usia (integer)
tinggi = float(input("Masukkan tinggi badan anda :"))  # Meminta input tinggi badan (float)
nama = input("Masukkan nama anda :")                   # Meminta input nama (string)

# hasil
print("Nama          : ", (nama))   # menampilkan hasil nama
print("Usia          : ", (usia))   # menampilkan hasil usia
print("Tinggi badan  : ", (tinggi)) # menampilkan hasil tinggi

# operasi logika atau boolean 
# not, or, and, xor 
#not
#print("=== NOT ===")
#a = True
#b = not a
#print("data a =", a)
#print("data b =", b)

#print("===OR===")
#a = True
#b = False
#c = a or b
#print(a,"OR",b,"=" ,c)

#print("===AND===")
from binascii import b2a_qp
from operator import truediv
#a = True
#b = False
#c = a and b
#print (a,"AND",b,"=",c)

#a = False
#b = True
#c = a and b
#print(a,"AND",b,"=",c)

#a = True
#b = True
#c = a and b
#print(a,"AND",b,"=",c)

#print("===xor===")
#a = True
#b = False
#c = a ^ b
#print(a,"^",b,"=",c)

#a = False
#b = False
#c = a ^ b
#print(a,"^",b,"=",c)

#a = True
#b = True
#c = a ^ b
#print(a,"^",b,"=",c)

  #++++++3--------10++++++

#inputUser = float(input( "Masukkan angka yang bernilai\n" "kurang dari 3\n" "atau\n" "lebih besar dari 10\n: "))

# Memeriksa angka kurang dari 3
#isKurangDari = inputUser < 3
#print("Kurang dari 3 =", isKurangDari)

# Memeriksa angka lebih dari 10
#isLebihDari = inputUser > 10
#print("Lebih dari 10 =", isLebihDari)

# Gabungkan dengan OR
#isCorrect = isKurangDari or isLebihDari

#print("Angka yang Anda masukkan memenuhi syarat =", isCorrect)
#print("========================================")

#nama = input("Siapa nama anda? ")

#if nama == "ucup":
   # print("Kamu ganteng abiiez!")
   # print("Kamu juga keren banget")

#print("akhir dari program")

#nama = input("Siapa nama anda? ")

#if nama == "ucup":
    #print("Hai ganteng abiiz!!!")

#elif nama == "paijo":
    #print("Hai si kece bangeets!!!")

#elif nama == "mario":
    #print("Hai humoris!!!")

#else:
    #print("Au ah gak kenal!!!")

#print("Akhir dari program")

print("===Latihan soal===")
usia = int(input("Masukkan usia: "))

if usia >= 0 and usia <= 12:
   print("Anak-anak")
elif usia >= 13 and usia <= 17:
    print("Remaja")
elif usia >= 18 and usia <= 59:
    print("Dewasa")
elif usia >= 60:
    print("Lansia")
else:
    print("Usia tidak valid")
print("progam finish")

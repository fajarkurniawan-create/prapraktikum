# Perulangan (loop)  
#angka = 1 
#print(angka) 
#angka = angka + 1 
#print(angka) 
#angka = angka + 1
#print(angka)
#for
#angka2 = [0, 1, 2, 3, 4]
#for i in angka2:
    #print(f"i sekarang → {i}")
#dengan range
#angka3 = range(5)
#for i in angka3:
 #print(f"i sekarang → {i}") 
#print("akhiri dari program\n") 
#angka4 = range(1,10)
#for i in angka4:
 # print(f"sekarang →{i}")
  #print ("saya keren")
  #print("akhiri dari progam\n")
#for dengan string
#data_str = "saya fajar"
#for huruf in data_str:
  #print(huruf)
#print("akhiri progam\n")

#while loop
#angka = 0
#while angka < 5 :
 # angka += 1
 # print(angka)

#past continou and break 
#past
#angka = 0
#while angka < 5:
    #angka += 1

    #if angka == 3:
        #pass
#print(angka)

# continou
#angka = 0

#while angka < 5:
   # angka += 1
  #  print(angka)

   # if angka == 3:
#        continue

  #  print("whasssup")
#break 
#for i in range(1, 6):
    #if i == 3:
        #break
   # print(i)

from operator import truediv
print("TUGAS\n")
#1
for angka in range(1, 51):

    if angka % 2 == 0:
        print(angka, "adalah genap")

    else:
        print(angka, "adalah ganjil")

 #2
for angka in range(2, 101):

    prima = True

    for pembagi in range(2, angka):

        if angka % pembagi == 0:
            prima = False
            break

    if prima:
        print(angka)
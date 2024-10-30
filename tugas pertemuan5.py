

#BUATLAH VARIABLE DENGAN BEBERAPA ELEMENT DALAM LIST
myList=["Blacky","mobil","2000cc","hitam",4]
myList.append("90juta") 
myList.append("roda empat")
myList.insert(2,"civic")
print(myList)


print('ini adalah program sederhana untuk menghitung luas bangun datar')
print("pilih menu angka 1-3 : \n1. Persegi\n2. Lingkaran\n3.Segitiga")
pilihmenu =int(input("silahkan pilih menu dengan mengetikan angka 1-3"))
#print(pilihmenu)

match pilihmenu:
    case 1:
        print("ini adalah menu untuk menghitung luas persegi")
        sisi= int(input("silahkan masukkan nilai yang mau di hitung"))
        hitung= sisi * sisi 
        print(f"Luas persegi adalah: {hitung}")
    case 2:
        print("Luas Lingkaran = phi*r*r")
        r= int (input ("masukkan angka anda"))
        phi=3.14
        luas=phi*r*r
        print(int(luas))
    case 3:
        print('Ini adalah operasi luas segitiga')
        alas= int(input('masukkan alas'))
        tinggi=int(input('masukkan tinggi'))

        luas_segitiga= int(1/2*alas*tinggi)
        print (f"Luas segitiga=1/2*",alas,tinggi, "=", luas_segitiga)
    case _:
        print("Pilihlah dengan bijak")
        








 
    
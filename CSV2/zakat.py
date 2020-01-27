nama=[]
gaji=[]
emas=[]
zakat=[]
pertahun=[]
perbulan=[]
nisab=[]
print ("+———————————————–+")
print ("| Penghitung Zakat Penghasilan |")
print ("| menurut pendapatan kasar (brutto) |")
print ("| |")
print ("+———————————————–+")
data=int(input("Masukan banyak data : "))
print("==========================================")

for i in range(data):
    a = input("Masukan nama : ")
    nama.append(a)
    b = int(input("Masukan harga emas saat ini: "))
    emas.append(b)
    c = int(input("Masukkan penghasilan Anda per bulan : "))
    gaji.append(c)
    print("")

    for i in range(data):
        d = 12 * gaji[i]
        pertahun.append(d)
        e = 0.025 * pertahun[i]
        zakat.append(e)
        f = 85 * emas[i]
        nisab.append(f)
        g = zakat[i] / 12
        perbulan.append(g)

        for i in range(data):
            print ("")
            print("—————————————-")
            print(" Zakat Penghasilan (Brutto)")
            print("—————————————-")
            print("Nama :",nama[i])
            print("Harga 1 gram emas :","Rp.",emas[i])
            print("Penghasilan per bulan :","Rp.",gaji[i])
            print("Penghasilan per tahun :","Rp.",pertahun[i])
            print("Harga nishab (85 gram emas) :","Rp.",nisab[i])
            print("Zakat penghasilan :","2.5% x",pertahun[i],"=","Rp.",zakat[i])
            if pertahun[i] >= nisab[i]:
                print("Keterangan : WAJIB Zakat Rp.",zakat[i],"/tahun")
                print(" atau Rp. ",perbulan[i],"/bulan")
                print("")
                if pertahun[i] <= nisab[i]:
                    print("Keterangan : Anda belum termasuk Wajib Zakat")


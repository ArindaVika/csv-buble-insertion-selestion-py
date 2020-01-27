import csv
import os

while True :
  menu = ['1. Data barang', '2. Pencarian Barang', '3. Penjualan', '4.Stok']
  submenu1 = ['1.list barang', '2.input barang', '3.insertion sort','4.buble sort','5.selection sort','6.kembali ke menu utama']
  DATABASE_FILE = 'database.csv'
  database = []
#jika huruf bersar semua itu konstanta
#diseynery berpaangan 
# jika menyimpan nilai itu namanya variabek gak harus ada sama dengannyaa
# join itu bisa meng print dengan fungsi menggabungkan


  #load data dari csv
  with open (DATABASE_FILE) as db_file:  
      csv_reader = csv.reader(db_file,delimiter=",") 
      #delimiter pemisah menggunakan koma
      for row in csv_reader :
         #mengulang BARIS SEBANYAK DI CSV READER
          database.append(row) 
          #append (menambah)
      id_barang=int(database[len(database)-1][0])+1 
      # int -1 buat mengetahui data terakhir lalu database +1 buat menambah id terakhir
      

  os.system("clear")
  print('\t'.join(menu)) # untuk tab
  aksi = int (input ("pilihan: "))

  if aksi == 1:
    while True :
      print('\t'.join(submenu1))  
      #biar menjoin nya mentab submenu1
      aksiMenu1 = int (input ("pilih: "))
      
      if aksiMenu1 == 1:
          #menampilkan data dari array database
              print("%2s \t %10s \t %10s" %("ID","NAMA","HARGA"))
              for row in database :  #mengulang database untuk memasukkan ke row
                  print("%2s \t %10s \t %10s" %(row[0],row[1],row[2]))
                  #ngeprint buat format (2string) dulu teros diisi datanya
              print("")
          
      elif aksiMenu1 == 2 :
          with open (DATABASE_FILE, mode='a') as db_file :  
              csv_writer = csv.writer(db_file) 
              #writer=menambah baris baru  di file  
              #quotechar = tamda kutip buat data yang mengandung koma
              while True :
                  nama_barang = input ("Masukkan Nama:")
                  if nama_barang =='=':
                      break
                  harga_barang = input ("Masukkan Harga:")
                  csv_writer.writerow([id_barang,nama_barang,harga_barang])
                  #menambahkan data di baris baru 
                  database.append([id_barang,nama_barang,harga_barang])
                  # menambah file csv baru ke dalam database
                  id_barang+=1
                  os.system("clear")
                  print ("Barang telah ditambahkan")

      elif aksiMenu1 == 3:
        for i in range (len(database)):
          database[i][2]=int(database[i][2])

        print(database)
        b=len(database)
        for x in range(1,b,1):
          #print(x)
          for y in range(x,0,-1):
            if database[y][2]<database[y-1][2]:
              temp=database[y]
              database[y]=database[y-1]
              database[y-1]=temp
        print("%2s \t %10s \t %10s" %("ID","NAMA","HARGA"))
        for row in database : 
                print("%2s \t %10s \t %10s" %(row[0],row[1],row[2]))
      elif aksiMenu1 == 4:
        print(database)

        for i in range (len(database)):
          database[i][2]=int(database[i][2])
        #data = database.copy()
        
        b=len(database)
        for x in range(b-1,0,-1):
          for y in range(x):
            if database[y][2]>database[y+1][2]:
              temp=database[y+1]
              database[y+1]=database[y]
              database[y]=temp
        print("%2s \t %10s \t %10s" %("ID","NAMA","HARGA"))
        for row in database : 
                print("%2s \t %10s \t %10s" %(row[0],row[1],row[2]))
      elif aksiMenu1 == 5:
        for i in range (len(database)):
          database[i][2]=int(database[i][2])

        max = len(database)-1
        for i in range(max):
          x=i
          #print('Proses ke-',(x+1))
          for j in range ((x+1),max+1,+1):
            if database[x][2] > database[j][2]:
              x=j
          temp = database[x]
          database[x] = database[i]
          database[i] = temp
        print("%2s \t %10s \t %10s" %("ID","NAMA","HARGA"))
        for row in database : 
                print("%2s \t %10s \t %10s" %(row[0],row[1],row[2]))
      elif aksiMenu1 == 6:
        break
      else :
        print("salah input")
      
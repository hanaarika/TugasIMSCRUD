from ctypes.wintypes import INT
import mysql.connector #melakukan import konektor mysql
import os #melakukan import os yang akan digunakan untuk membersihkan layar

db = mysql.connector.connect( #menghubungkan dengan mysql
    host="localhost", #nama host
    user="root", #nama user
    password="", #password
    database="PreTestPraktikumIMS" #nama database
)

def insert_data_peserta(db): #fungsi ini digunakan untuk input data peserta
    os.system('cls') #untuk membersihkan layar
    print('==============================================================')
    print('                     INPUT DATA PESERTA')
    print('==============================================================')
    nama_depan = input("Masukkan nama depan     : ") #user memasukkan nama depan peserta
    nama_belakang = input("Masukkan nama belakang  : ") #user memasukkan nama belakang peserta
    alamat = input("Masukkan alamat         : ") #user memasukkan alamat peserta
    no_telp = input("Masukkan no telepon     : ") #user memasukkan no telpon peserta
    if len(no_telp) <= 11: #jika nomor telepon kurang dari 11 angka maka
        print('Nomor Telepon Anda kurang dari 8 digit') #tampilan tulisan akan seperti ini
        insert_data_peserta(db) #kemudian kembali ke fungsi awal
        quit()
    val = (nama_depan, nama_belakang, alamat, no_telp) #value/isi yang akan dimasukkan ke database
    cursor = db.cursor() #pembuatan objek cursor
    sql = "INSERT INTO tb_peserta (nama_depan, nama_belakang, alamat, no_telp) VALUES (%s, %s, %s, %s)" #memasukkan data ke kolom-kolom di tabel peserta dengan value yang sudah dibuat
    cursor.execute (sql, val) #digunakan untuk mengeksekusi query
    db.commit()
    print("\nData peserta berhasil disimpan!".format(cursor.rowcount)) #Output yang tampil ketika data berhasil disimpan

def insert_data_pertandingan(db): #fungsi ini digunakan untuk input data pertandingan
    os.system('cls') #untuk membersihkan layar
    print('==============================================================')
    print('                   INPUT DATA PERTANDINGAN')
    print('==============================================================')
    id_peserta_a = input("Masukkan id peserta 1:  ") #user memasukkan id peserta pertama
    id_peserta_b = input("Masukkan id peserta 2:  ") #user memasukkan id peserta kedua
    val = (id_peserta_a, id_peserta_b) #value/isi yang akan dimasukkan ke database
    cursor = db.cursor() #pembuatan objek cursor
    sql = "INSERT INTO tb_pertandingan (id_peserta_a, id_peserta_b) VALUES (%s, %s)" #memasukkan data ke kolom-kolom di tabel pertandingan dengan value yang sudah dibuat
    cursor.execute (sql, val) #digunakan untuk mengeksekusi query
    db.commit()
    print("\nData pertandingan berhasil disimpan".format(cursor.rowcount)) #Output yang tampil ketika data berhasil disimpan

def show_ranking(db): #fungsi yang digunakan untuk menunjukkan ranking peserta
    os.system('cls') #untuk membersihkan layar
    cursor = db.cursor() #pembuatan objek cursor
    print('==============================================================')
    print('                   DATA RANKING PERTANDINGAN')
    print('==============================================================')
    sql = "SELECT @rownum:=@rownum+1 'rank', p.* FROM tb_pertandingan p, (SELECT @rownum:=0) r ORDER BY hasil DESC LIMIT 10" #menampilkan peringkat sesuai hasil pertandingan
    cursor.execute(sql) #digunakan untuk mengeksekusi query
    results = cursor.fetchall() #menampilkan hasil dari perintah query sebelumnya
    
    if cursor.rowcount < 0: #jika data kurang dari 0, maka
        print("Tidak ada data") #akan keluar tampilan seperti ini
    else:
        for data in results: #jika ada data, maka
            print(data) #seluruh data akan ditampilkan

def show_data_pertandingan(db): #fungsi untuk menampilkan data pertandingan
    os.system('cls') #untuk membersihkan layar
    print('==============================================================')
    print('                     DATA PERTANDINGAN')
    print('==============================================================')
    cursor = db.cursor() #pembuatan objek cursor
    sql = "SELECT * FROM tb_pertandingan" #menampilkan seluruh isi tabel pertandingan
    cursor.execute(sql) #digunakan untuk eksekusi query
    results = cursor.fetchall() #menampilkan hasil dari perintah query sebelumnya

    if cursor.rowcount < 0: #jika data kurang dari 0, maka
        print("Tidak ada data") #akan keluar tampilan seperti ini
    else:
        for data in results: #jika ada data, maka
            print(data) #seluruh data akan ditampilkan

def show_data(db): #fungsi untuk menampilkan data peserta
    os.system('cls') #untuk membersihkan layar
    print('==============================================================')
    print('                        DATA PESERTA')
    print('==============================================================')
    cursor = db.cursor() #pembuatan objek cursor
    sql = "SELECT * FROM tb_peserta" #menampilkan seluruh isi tabel peserta
    cursor.execute(sql) #digunakan untuk eksekusi query
    results = cursor.fetchall() #menampilkan hasil dari perintah query sebelumnya

    if cursor.rowcount < 0: #jika data kurang dari 0, maka
        print("Tidak ada data") #akan keluar tampilan seperti ini
    else:
        for data in results: #jika ada data, maka
            print(data) #seluruh data akan ditampilkan

def update_data_peserta(db): #fungsi untuk mengubah data peserta
    print('==============================================================')
    print('                     UPDATE DATA PESERTA')
    print('==============================================================')
    os.system('cls') #membersihkan layar
    cursor = db.cursor() #pembuatan objek cursor
    show_data(db) #pemanggilan fungsi show_data
    id = input("Pilih id peserta:   ") #user memasukkan id peserta
    os.system('cls') #membersihkan layar

    print("PILIH DATA YANG AKAN DIUBAH")
    print("1. Data Pribadi")
    print("2. Data Ranking")
    pilihan = input("\nPilih: ") #user memilih data yang akan diubah sesuai pilihan yang disediakan

    if pilihan == "1": #jika user memilih 1, maka
        os.system('cls') #membersihkan layar
        print('==============================================================')
        print('                     UPDATE DATA PESERTA')
        print('==============================================================')
        #user akan mengisi beberapa data di bawah ini
        nama_depan = input("Masukkan nama depan     : ") #user memasukkan nama depan peserta
        nama_belakang = input("Masukkan nama belakang  : ") #user memasukkan nama belakang peserta
        alamat = input("Masukkan alamat         : ") #user memasukkan alamat peserta
        no_telp = input("Masukkan no telepon     : ") #user memasukkan no telpon peserta
        if len(no_telp) <= 11: #jika nomor telepon kurang dari 11 angka maka
            print('Nomor Telepon Anda kurang dari 8 digit') #tampilan tulisan akan seperti ini
            insert_data_peserta(db) #kemudian kembali ke fungsi awal
            quit()
        sql = "UPDATE tb_peserta SET nama_depan=%s, nama_belakang=%s, alamat=%s, no_telp=%s WHERE id=%s" #dilakukan update data pada beberapa kolom sesuai input user sebelumnya
        val = (nama_depan, nama_belakang, alamat, no_telp, id) #value/isi yang akan dimasukkan ke database
        cursor.execute(sql, val) #digunakan untuk eksekusi query
        db.commit() 
        print("\nData berhasil diubah".format(cursor.rowcount)) #tampilan setelah data berhasil diubah
    elif pilihan == "2": #jika user memilih 2, maka
        os.system('cls') #membersihkan layar
        print('==============================================================')
        print('                     UBAH RANKING PESERTA')
        print('==============================================================')
        id_rank = input("Masukkan Ranking ID: ")#user memasukkan id rank
        sql = "UPDATE tb_peserta SET id_rank=%s WHERE id=%s" #dilakukan update pada kolom di tabel peserta sesuai input yang dimasukkan
        val = (id_rank, id) #value/isi yang akan dimasukkan ke database
        cursor.execute(sql, val) #digunakan untuk eksekusi query
        db.commit()
        print("\nData berhasil diubah".format(cursor.rowcount)) #tampilan setelah data berhasil diubah
    else:
        print("Pilihan tidak tersedia") #jika pilihan tidak tersedia

def update_data_pertandingan(db): #fungsi untuk update data pertandingan
    os.system('cls') #membersihkan layar
    cursor = db.cursor() #pembuatan obje cursor
    show_data_pertandingan(db) #memanggil fungsi show_data_pertandingan
    print('==============================================================')
    print('                    UBAH DATA PERTANDINGAN')
    print('==============================================================')
    id = input("Ketik ID Pertandingan:   ") #user memasukkan id pertandingan yang ingin diubah
    os.system('cls') #membersihkan layar
    print('==============================================================')
    print('                    UBAH DATA PERTANDINGAN')
    print('==============================================================')
    print("PILIH DATA YANG AKAN DIUBAH")
    print("1. Data Peserta")
    print("2. Data Pertandingan")
    pilihan = input("\nPilih: ") #user memasukkan pilihan sesuai pilihan diatas

    if pilihan == "1": #jika pilihan 1, maka
        os.system('cls') #membersihkan layar
        print('==============================================================')
        print('                     UBAH DATA PESERTA')
        print('==============================================================')
        id_peserta_a = input("Masukkan id peserta 1:  ") #user memasukkan id peserta pertama
        id_peserta_b = input("Masukkan id peserta 2:  ") #user memasukkan id peserta kedua
        sql = "UPDATE tb_pertandingan SET id_peserta_a=%s, id_peserta_b=%s WHERE id=%s" #dilakukan update pada kolom di tabel pertandingan sesuai dengan inputan yang dimasukkan tadi
        val = (id_peserta_a, id_peserta_b, id) #value/isi yang dimasukkan ke database
        cursor.execute(sql, val) #digunakan untuk eksekusi query
        db.commit()
        print("\nData berhasil diubah".format(cursor.rowcount)) #tampilan setelah data berhasil diubah
    elif pilihan == "2": #jika pilihan 2, maka
        os.system('cls') #membersihkan layar
        print('==============================================================')
        print('                    UBAH DATA PERTANDINGAN')
        print('==============================================================')
        hasil = input("Masukkan hasil akhir: ") #user memasukkan hasil akhir turnamen
        mulai = input("Masukkan waktu mulai: ") #user memasukkan waktu mulai
        selesai = input("Masukkan waktu selesai: ") #user memasukkan waktu selesai
        sql = "UPDATE tb_pertandingan SET hasil=%s, mulai=%s, selesai=%s WHERE id=%s" #update pad kolom di tabel pertandingan sesuai input user
        val = (hasil, mulai, selesai, id) #value/isi yang dimasukkan ke database
        cursor.execute(sql, val) #digunakan untuk eksekusi query
        db.commit()
        print("\nData berhasil diubah".format(cursor.rowcount)) #tampilan setelah data berhasil diubah
    else:
        print("Pilihan tidak tersedia") #jika pilihan tidak tersedia
    
def delete_data_peserta(db): #fungsi untuk menghapus data peserta
    os.system('cls') #membersihkan layar
    cursor = db.cursor() #pembuatan objek cursor
    show_data(db) #memanggil fungsi show_data
    print('==============================================================')
    print('                     HAPUS DATA PESERTA')
    print('==============================================================')
    id = input("Pilih id peserta: ") #user menginput id peserta yang ingin dihapus
    sql = "DELETE FROM tb_peserta WHERE id=%s" #perintah sql untuk menghapus data sesuai id yang diinginkan user
    val = (id,) #value/isi yang akan dihapus
    cursor.execute(sql, val) #digunakan untuk eksekusi query
    db.commit()
    print("Data berhasil dihapus".format(cursor.rowcount)) #tampilan setelah data berhasil dihapus

def delete_data_pertandingan(db): #fungsi untuk menghapus data pertandingan
    os.system('cls') #membersihkan layar
    cursor = db.cursor() #pembuatan objek cursor
    show_data_pertandingan(db) #memanggil fungsi show_data_pertandingan
    print('==============================================================')
    print('                   HAPUS DATA PERTANDINGAN')
    print('==============================================================')
    id = input("Pilih id pertandingan: ") #user menginput id pertandingan yang ingin dihapus
    sql = "DELETE FROM tb_pertandingan WHERE id=%s" #perintah sql untuk menghapus data sesuai id yang diinginkan user
    val = (id,) #value/isi yang akan dihapus
    cursor.execute(sql, val) #digunakan untuk eksekusi query
    db.commit()
    print("Data berhasil dihapus".format(cursor.rowcount)) #tampilan setelah data berhasil dihapus

def show_menu(db): #fungsi untuk menunjukkan menu
    print('==============================================================')
    print('                         PILIH MENU')
    print('==============================================================')
    print("1. Insert Data Peserta")
    print("2. Update Data Peserta")
    print("3. Insert Data Pertandingan")
    print("4. Update Data Pertandingan")
    print("5. Delete Data Peserta")
    print("6. Delete Data Pertandingan")
    print("7. Data Peserta")
    print("8. Data Pertandingan")
    print("9. Data Ranking")
    print("0. Exit Program")
    menu = input("\nPilih menu: ") #user memasukkan menu yang diinginkan

    os.system('cls') #membersihkan layar

    if menu == "1": #jika pilihan 1, maka
        insert_data_peserta(db) #memanggil fungsi insert_data_peserta
    elif menu == "2": #jika pilihan 2, maka
        update_data_peserta(db) #memanggil fungsi update_data_peserta
    elif menu == "3": #jika pilihan 3, maka
        insert_data_pertandingan(db) #memanggil fungsi insert_data_pertandingan
    elif menu == "4": #jika pilihan 4, maka
        update_data_pertandingan(db) #memanggil fungsi update_data_pertandingan
    elif menu == "5": #jika pilihan 5, maka
        delete_data_peserta(db) #memanggil fungsi delete_data_peserta
    elif menu == "6": #Jika pilihan 6, maka
        delete_data_pertandingan(db) #memanggil fungsi delete_data_pertandingan
    elif menu == "7": #Jika pilihan 7, maka
        show_data(db) #memanggil fungsi show_data
    elif menu == "8": #Jika pilihan 8, maka
        show_data_pertandingan(db) #memanggil fungsi show_data_pertandingan
    elif menu == "9": #Jika pilihan 9, maka
        show_ranking(db) #memanggil fungsi show_ranking
    elif menu == "0": #jika pilihan 0, maka
        exit() #keluar program

if __name__ == "__main__":
    while(True): #perulangan menu
        show_menu(db)
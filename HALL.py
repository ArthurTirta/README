from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import json
import sys
import os
import fitz
import shutil
import webbrowser

# ///////////////////////////milik pemilihan dokumen
def kembalikan_ke_halutama():
    Widget.close()
    jendela_hal_utama.show()
def about_gambar():
    global Widget
    Widget = QWidget()
    Widget.setWindowTitle("About Us")
    Widget.setGeometry(100,30,1200,700)
    layout=QVBoxLayout()
    Widget.setWindowIcon(icon)

    pixmap= QPixmap("ABOUT US.jpg")
    skala_pixmap=pixmap.scaled(window_width,window_height)
    label_background = QLabel(Widget)
    label_background.setPixmap(skala_pixmap)
    label_background.setGeometry(0,0,window_width,window_height)




    kembali= QPushButton("Kembali")
    layout.addWidget(kembali)        
    layout.setContentsMargins(1000,0,100,650)
    kembali.clicked.connect(kembalikan_ke_halutama)
    Widget.setLayout(layout)
    Widget.show()
    jendela_hal_utama.close()

    
    
def tmbl_kembali_pemilihan():
    jendela_pemilihan.close()
    jendela_hal_utama.show()
def tmbl_kembali_pembayaran():
    jendela_pembayaran.close()
    jendela_pemilihan.show()
def beri_hak_akses():
    with open('daftar_akun.json', 'r') as file:
        data = json.load(file)
        for dokumen in data:
            if input_nama.text() in dokumen["nama"]:
                dokumen["buku"].append(selected_item.text())

            with open('daftar_akun.json', 'w') as file:
                json.dump(data, file, indent=4)
        QMessageBox.warning(jendela_pembayaran, 'Peringatan', "Pembayaran Berhasil" )

                    
def pembayaran_dokumen():
    global tombol_cari
    
    tombol_cari = QPushButton('sudah', jendela_pembayaran)
    tombol_cari.move(405, 650)
#mulai_apakah sudah mebayar
#mulai_apakah sudah mebayar(ya)
    tombol_cari.clicked.connect(beri_hak_akses)
    # tombol_cari.clicked.connect(login)

    tombol_buat = QPushButton('kembali', jendela_pembayaran)
    tombol_buat.clicked.connect(tmbl_kembali_pembayaran)
    # tombol_buat.clicked.connect(Buatakun)
    tombol_buat.move(675, 650)

    jendela_pembayaran.show()
    jendela_pemilihan.close()


def pemilihan_dokumen():
    global selected_item
#mulai_pengguna memilih dokumen
    selected_item = list_widget.currentItem()

#akhir_pengguna memilih dokumen
    with open('data_buku.json', 'r') as file:
        data = json.load(file)

        for dokumen in data:
   
            print(selected_item.text())
            print(dokumen["Nama_dokumen"])
            if selected_item.text() in dokumen["Nama_dokumen"]:
                print("ada dokumennya di database")
                alamat = (dokumen["path_dok"])
            #mulai Cek apakah dokumen berbayar
                #mulai_ kondisi dokumen tidak berbayar 
                print(alamat)
                if dokumen["Harga Dokumen"] == False :
                        print (" harga kosong _if")
                        webbrowser.open(alamat, new=2)
                #akhir_ kondisi dokumen tidak berbayar       
                #mulai_ kondisi dokumen  berbayar 
                else:
        
                    with open('daftar_akun.json', 'r') as file:
                        
                        data_akun = json.load(file)
             
                        for dokumen_akun in data_akun:
                            print(input_nama.text())
                            print(dokumen_akun['nama'])
                            if input_nama.text() in dokumen_akun['nama']:
                                print("berhasil masuk percabangan")
                            #mulai_ apakah sudah pernah membayar
                                #apakah sudah pernah membayar (ya)
                                print(selected_item.text())
                                print(dokumen_akun["buku"])
                                if selected_item.text() in dokumen_akun["buku"]:

                                    webbrowser.open(alamat, new=2)
                                #apakah sudah pernah membayar (tidak)
                                else:
                                    pembayaran_dokumen()
                            #mulai_ apakah sudah pernah membayar
                #akhir_ kondisi dokumen  berbayar 
            #akhir_cek apakah dokumen berbayar
def cari_dokumen():
    global nama_item_klik
    global y
    y = int 
    y = 10
    x = 1
    value_kata_kunci = 0
    value_batas_tahun = 0
    batas_tahun = 0
    if len(input_cari.text()) >=1:
        value_kata_kunci +=1
        kata_kunci = (input_cari.text().lower(),input_cari.text().upper() ,input_cari.text().capitalize() )
    if len(input_cari_tterbit.text())>=1:
        value_batas_tahun +=1
        batas_tahun= int(input_cari_tterbit.text())
    
    print (value_batas_tahun)
    print (value_kata_kunci)
    print(kata_kunci)  
    print(batas_tahun)
    if value_batas_tahun == 1 and value_kata_kunci == 1:
            if kata_kunci:
                list_widget.clear()
                try:
                    with open("data_buku.json", 'r') as file:
                        data=json.load(file)
                        
                        for dokumen in data:
                          
                            for x in kata_kunci:
                        
                                if x in dokumen["Nama_dokumen"]:
                                
                    
                                    if batas_tahun <= dokumen["Tahun_terbit"]:  
                                        # print (dokumen["Nama_dokumen"])
                                        # print(batas_tahun)
                                        # print(dokumen["Tahun_terbit"])
                                        # mulai_nambah item di list pencarian dokumen
                                        list_widget.addItem(dokumen["Nama_dokumen"])
                                        # akhir_nambah item di list pencarian dokumen
                                        nama_item_klik = dokumen["Nama_dokumen"]
                               
                except FileNotFoundError:
                    QMessageBox.warning(jendela_pemilihan, 'Peringatan', "File  tidak ditemukan." )
    else:
        QMessageBox.warning(jendela_pemilihan, 'Peringatan', "Mohon semua data diisi " )

def pencarian_dokumen():
    input_cari.setText(input_search.text())
    list_widget.itemClicked.connect(pemilihan_dokumen)# layout_web.addWidget(web_view)
    layout.addLayout(layout_web)
    jendela_pemilihan.setLayout(layout)
    jendela_pemilihan.show()
    jendela_hal_utama.hide()

# ///////////////////////////////////////////////////////////////////////////////////

def membuka_dok1(event):
    webbrowser.open("D:\Kuliah\Praktik Algoritma Pemrograman\Tubes Alpro\Kodingan Laode\Preview\Laporan Praktikum Variabel, Konsol IO, dan Konversi Tipe Data.pdf", new=2)
def membuka_dok2(event):
    webbrowser.open("D:\Kuliah\Praktik Algoritma Pemrograman\Tubes Alpro\Kodingan Laode\Preview\Modul Kimia Dasar Semester Gasal 2023_2024.pdf", new=2)
def membuka_dok3(event):
    webbrowser.open("D:\Kuliah\Praktik Algoritma Pemrograman\Tubes Alpro\Kodingan Laode\Preview\Modul Praktikum Alpro.pdf", new=2)

def tombol_kembali_halutama():
    main_window.show()
    jendela_hal_utama.destroy()

def tombol_kembali_daftar():
    main_window.show()
    jendela_daftar.destroy()

def tombol_kembali_upload():
    jendela_hal_utama.show()
    jendela_upload.close()

  
    

def login(): # cek username & password di database
    y = 0 
    with open("daftar_akun.json", "r") as readfile:
            data = json.load(readfile)  #ini ngambil data akun
    for database in data:      #mulai memerikas akun
        if input_nama.text() == (database["nama"]) and input_password.text() == (database["password"]):     # inti 
                # status_label_login = ("Username atau Password Benar")
                y+=1
                halaman_utama()
        else:
                # status_label_login = ("Username atau Password Salah")
                pass
                
    if y>=1:
        QMessageBox.warning(main_window,"Peringatan","Username atau Password Benar")
    else:
        QMessageBox.warning(main_window,"Peringatan","Username atau Password Salah")



# /////////////////////milik upload dokumen////////////////////////////////////////////////////
def cek_syarat_upload():
    # radio_ditekan(state)

    global value_input_harga_dokumen
    global Gratis # bisa dihilangkan 
    global harga_dokumen
    global value_tterbit_dok
    global value_nama_dok      
    global value_path
    global tahun_terbit
    # tahun_terbit = 0zxcvbnmz
     
    tahun_terbit = int(input_tterbit_dokumen.text())
    harga_dokumen=int(input_harga_dokumen.text())
    cek_keberadaa_harga= len(input_harga_dokumen.text())
    if value_opsi_berbayar == 1: # gratiis = 0 namun berbayar = 1
        if cek_keberadaa_harga == 0: #kondisi ketika Qlineedit tidak diisi angka
            
            value_input_harga_dokumen = 0
            
            #mohon mengisi harga dokumen
        else: # konidisi ketika Qlineedit disii angka
            value_input_harga_dokumen = 1
            if harga_dokumen == 0 :
                Gratis= True
                harga_dokumen = 0
            else :
                Gratis = False
                #harga dokumen akan terisi sesuai keingnan pengunggah
                #harga dokumen = input_harga _dokumen.text()
    else :
        value_input_harga_dokumen = 1
        harga_dokumen = 0
        Gratis = True
    
     # ////////cek apakah tterbit sudh diisi
    if input_tterbit_dokumen == "":
            value_tterbit_dok= 0
    else:
            value_tterbit_dok = 1
    # /////cek nama apakah sduh diisi
    if input_nama_dokumen == "":
            value_nama_dok = 0
    else:
            value_nama_dok = 1
    # /////////cek apakah destination path ada
    if sudah_pilih_folder == 0:
            value_path = 0
    else:
            value_path = 1
        
def pdf_to_gambar(pdf_path):
    # Render halaman pertama menjadi citra
    pdf_document = fitz.open(pdf_path)
    page = pdf_document[0]
    image = page.get_pixmap()
    pdf_document.close()

    # konversi citra menjadi pixmap
    image_pixmap = QPixmap.fromImage(QImage(image.samples, image.width, image.height, image.stride, QImage.Format_RGB888))
    return image_pixmap

def show_pdf_preview():
    global destination_path
    global v_upload_button
    global sudah_pilih_folder
    
    v_upload_button = 1
    file_explorer = QFileDialog()
    file_explorer.setNameFilter("PDF Files (*.pdf)")
    file_explorer.setWindowTitle("Select a PDF file")
    if file_explorer.exec_() == QFileDialog.Accepted:
        selected_file = file_explorer.selectedFiles()[0]

        # Konversi halaman pertama pdf menjadi pixmap
        pixmap = pdf_to_gambar(selected_file)
        label.setPixmap(pixmap)
        label.adjustSize()
        label.show()

        # Membuat folder 'pdffile' jika belum ada
        pdf_folder = "pdffile" #rubah menajdi teks yang akan diupload
        os.makedirs(pdf_folder, exist_ok=True)

        # Membuat Nama Folder (00001, 00002, dst.)
        subfolder_name = f"{len(os.listdir(pdf_folder)) + 1:05d}" #rubah menajdi teks yang akan diupload
        subfolder_path = os.path.join(pdf_folder, subfolder_name)
        os.makedirs(subfolder_path)

        # Copy dan rename folder
        destination_path = os.path.join(subfolder_path, f"{input_nama_dokumen.text()}.pdf")
        shutil.copy(selected_file, destination_path)

       
        # label = QLabel()
        # label.setScaledContents(True)
        label.mousePressEvent = on_label_clicked # Saat label ditekan , akan menjalankan fungsi
        v_layout_utama.addWidget(label)
        
        sudah_pilih_folder += 1
       
def radio_ditekan(state):
    global value_opsi_berbayar

    if state:
     # mulai _ketika Qradiobutton ditekan
        label_harga.setEnabled(True)
        # mulai_pengguna memasukkan harga dokumen
        input_harga_dokumen.setEnabled(True)
        # akhir_pengguna memasukkan harga dokumen
        value_opsi_berbayar = 1
        input_harga_dokumen.setText("0")
    # akhir _ketika Qradiobutton ditekan
    else:
        # mulai _ketika Qradiobutton tidak ditekan
        label_harga.setEnabled(False)
        input_harga_dokumen.setEnabled(False)
        value_opsi_berbayar = 0
        # akhir _ketika Qradiobutton tidak ditekan
        

def on_label_clicked(event):
    # Membuat path dari label
    
    pdf_folder = "pdffile"
    latest_subfolder = max(os.listdir(pdf_folder), key=int, default='00000')
    latest_subfolder_path = os.path.join(pdf_folder, latest_subfolder)

    # Fitur membuka file semisal gambar di klik
    pdf_files = [f for f in os.listdir(latest_subfolder_path) if f.endswith(".pdf")]
    if pdf_files:
        pdf_file_path = os.path.join(latest_subfolder_path, pdf_files[-1])
        webbrowser.open(pdf_file_path, new=2)

def upload_dok():
# mulai_pengcekan syarat upload dokumen
    cek_syarat_upload()
# akhir_pengecekan syarat upload dokumen

# mulai_percabangan syarat upload dokumen
    if value_nama_dok ==1 and value_tterbit_dok ==1 and value_input_harga_dokumen ==1 and value_path ==1:
# akhir percabangan syarat upload dokumen
        with open("data_buku.json", "r") as readfile:
            data = json.load(readfile)  #ini ngebaca data dari json

        new_entry = {
            "Nama_dokumen": (input_nama_dokumen.text()), # ini diisi QlineEdit.text()
            "Tahun_terbit": (tahun_terbit),       # ini juga diisi QlineEdit.text()
            "Harga Dokumen" :(harga_dokumen),
            "path_dok": (destination_path)
        }

        data.append(new_entry) #ini gabungin data lama sama data yg mau ditambah

        with open("data_buku.json", "w") as writefile:
            json.dump(data, writefile, indent=4) #ini yang nulis data ke json

        QMessageBox.warning(jendela_upload, 'Peringatan', "Selamat dokumen telah berhasil terupload" )
    else:
        QMessageBox.warning(jendela_upload, 'Peringatan', "Mohon periksa kembali data anda " )



def UploadButton():
    global value_upload_button
    global sudah_pilih_folder
    if value_upload_button == 0:
        global jendela_upload
        global input_nama_dokumen
        global input_tterbit_dokumen
        global v_layout_utama
        global value_nama_dok
        global value_tterbit_dok

        jendela_upload = QWidget()
        jendela_upload.setWindowTitle("Unggah Dokumen")
        jendela_upload.setGeometry(100, 30, 1200, 700)  
        jendela_upload.setWindowIcon(icon)
        
        pixmap=QPixmap("Gambar WhatsApp 2023-11-15 pukul 06.14.45_43e17c74.jpg")
        scaled_pixmap= pixmap.scaled(window_width,window_height)

        background_label= QLabel(jendela_upload)
        background_label.setPixmap(scaled_pixmap)
        background_label.setGeometry(0,0,window_width,window_height)

        v_layout_utama = QVBoxLayout()
        h_layout_name = QHBoxLayout()
        h_layout_tahun = QHBoxLayout()
        h_layout_harga = QHBoxLayout()
        h_layout_tombol = QHBoxLayout()
        h_layout_radio = QHBoxLayout()
        Default_Font= QFont("TimesNewroman",14)

        label_nama = QLabel(jendela_upload)
        label_nama.setText("Nama Dokumen            :")
        label_nama.setFont(Default_Font)
        h_layout_name.addWidget(label_nama)
# mulai_input(nama dokumen)
        input_nama_dokumen = QLineEdit(jendela_upload)
        input_nama_dokumen.setPlaceholderText("Masukkan nama dokumen")
        input_nama_dokumen.setFont(Default_Font)
        h_layout_name.addWidget(input_nama_dokumen)
## akhir_input(nama dokumen)
        
        label_tterbit = QLabel(jendela_upload)
        label_tterbit.setText("Tahun Terbit Dokumen :")
        label_tterbit.setFont(Default_Font)
        
        h_layout_tahun.addWidget(label_tterbit)
# mulai_input(tahun terbit dokumen)
        input_tterbit_dokumen = QLineEdit(jendela_upload)
        input_tterbit_dokumen.setPlaceholderText("Masukkan tahun terbit dokumen")
        input_tterbit_dokumen.setFont(Default_Font)
        input_tterbit_dokumen.setText("0")
        h_layout_tahun.addWidget(input_tterbit_dokumen)
# akhir_input(nama dokumen)

        global opsi_berbayar
        global value_opsi_berbayar
        value_opsi_berbayar = 0
# mulai_input(berbayar atau nggak?)
        opsi_berbayar = QRadioButton('Berbayar ?')
        opsi_berbayar.setFont(Default_Font)
    #mulai_percabangan dokumen berbayar
        opsi_berbayar.toggled.connect(radio_ditekan)
    #akhir_percabangan dokumen berbayar    
        h_layout_radio.addWidget(opsi_berbayar)
# mulai_input(berbayar atau nggak?)

        global label_harga
        label_harga = QLabel(jendela_upload)
        label_harga.setText("Harga Dokumen           :")
        label_harga.setFont(Default_Font)
        h_layout_harga.addWidget(label_harga)
        label_harga.setEnabled(False)

        global input_harga_dokumen
        input_harga_dokumen =QLineEdit(jendela_upload)
        input_harga_dokumen.setPlaceholderText("Masukkan Harga Dokumen")
        input_harga_dokumen.setFont(Default_Font)
        h_layout_harga.addWidget(input_harga_dokumen)
        input_harga_dokumen.setEnabled(False)
   
        v_layout_utama.addLayout(h_layout_name)
        v_layout_utama.addLayout(h_layout_tahun)
        v_layout_utama.addLayout(h_layout_harga)
        v_layout_utama.addLayout(h_layout_radio)
        v_layout_utama.addLayout(h_layout_tombol)

        # ////////////////////////////////////
        global label
        label = QLabel()
        label.setScaledContents(True)

        tombol_pilih_pdf = QPushButton("Pilih PDF")
        tombol_pilih_pdf.clicked.connect(show_pdf_preview) 

        tombol_kembali= QPushButton( "Kembali")
        tombol_kembali.clicked.connect(tombol_kembali_upload)

# mulai_unggah dokumen
# mulai_Upload dokumen
        tombol_upload=QPushButton("Upload Dokumen")
        tombol_upload.clicked.connect(upload_dok)
# akhir_Upload dokumen
# akhir_unggah dokumen

        h_layout_tombol.addWidget(tombol_pilih_pdf)
        h_layout_tombol.addWidget(tombol_upload)
        h_layout_tombol.addWidget(tombol_kembali)

        jendela_upload.setLayout(v_layout_utama)

        value_upload_button +=1

        jendela_upload.show()
        jendela_hal_utama.close()
    else:
        jendela_upload.show()
        jendela_hal_utama.close()
    sudah_pilih_folder = 0

def halaman_utama(): # flowchart halaman utama
    global perulangan_halutama
    global input_search
    v_layout_upload = QHBoxLayout()
    dok_1 =QLabel()
    dok_2 =QLabel()
    dok_3 =QLabel()

    gambar_dok1 = pdf_to_gambar("D:\Kuliah\Semester 1\Praktik Algoritma Pemrograman\Tubes Alpro\Kodingan Laode\Preview\Laporan Praktikum Variabel, Konsol IO, dan Konversi Tipe Data.pdf")#masukkan jalur dokumen kalian di antara prtik dua
    gambar_dok2 = pdf_to_gambar("D:\Kuliah\Semester 1\Praktik Algoritma Pemrograman\Tubes Alpro\Kodingan Laode\Preview\Modul Kimia Dasar Semester Gasal 2023_2024.pdf")#masukkan jalur dokumen kalian di antara prtik dua
    gambar_dok3 = pdf_to_gambar("D:\Kuliah\Semester 1\Praktik Algoritma Pemrograman\Tubes Alpro\Kodingan Laode\Preview\Modul Praktikum Alpro.pdf")#masukkan jalur dokumen kalian di antara prtik dua

    edit_gambar_dok1 = gambar_dok1.scaledToWidth(260)
    edit_gambar_dok2 = gambar_dok2.scaledToWidth(260)
    edit_gambar_dok3 = gambar_dok3.scaledToWidth(260)
    
    #awal_fungsi pemilihan dokumen
    dok_1.mousePressEvent = membuka_dok1 #ketika gambar dok1 dipencet , fungsi (membuka_dok1) berjalan
    dok_2.mousePressEvent = membuka_dok2
    dok_3.mousePressEvent = membuka_dok3

   
    if perulangan_halutama == 0:
        dok_1.setPixmap(edit_gambar_dok1)
        dok_2.setPixmap(edit_gambar_dok2)
        dok_3.setPixmap(edit_gambar_dok3)

        v_layout_upload.addWidget(dok_1)
        v_layout_upload.addWidget(dok_2)
        v_layout_upload.addWidget(dok_3)
        
        v_layout_upload.setContentsMargins(50, 120, 10, 10)
        jendela_hal_utama.setLayout(v_layout_upload)

        label_cari = QLabel('Search', jendela_hal_utama)
        label_cari.setStyleSheet('color: black;')
        label_cari.move(320, 186)
        label_cari.setFont(QFont('SansSerif', 13))

        input_search = QLineEdit (jendela_hal_utama)
        input_search.setFont(QFont('SansSerif', 12))
        input_search.move(400, 184)
        input_search.setFixedWidth(320)

        tombol_search = QPushButton(jendela_hal_utama)
        tombol_search.setGeometry(730, 178, 60, 40)
        tombol_search.setStyleSheet("QPushButton { border-image: url(tombol search.jpg); }")
        
        tombol_kembali = QPushButton(jendela_hal_utama)
        tombol_kembali.setGeometry(10, 10, 60, 60)
        tombol_kembali.setStyleSheet("QPushButton { border-image: url(kembali.jpg); }")#masukk foto ikon kemabli di dalam kurung buka
        tombol_kembali.clicked.connect(tombol_kembali_halutama)

        label_kembali = QLabel('Kembali', jendela_hal_utama)
        label_kembali.setStyleSheet('color: black;')
        label_kembali.move(12, 67)
        label_kembali.setFont(QFont('SansSerif', 13))       

        tombol_about = QPushButton(jendela_hal_utama)
        tombol_about.setGeometry(1130, 10, 60, 60)
        tombol_about.setStyleSheet("QPushButton { border-image: url(about.jpg); }")#masukkan foto ikon tombol about di dalam kurung buka
        tombol_about.clicked.connect(about_gambar)

        label_about = QLabel('About Us', jendela_hal_utama)
        label_about.setStyleSheet('color: black;')
        label_about.move(1100, 67)
        label_about.setFont(QFont('SansSerif', 13))

        tombol_uploud = QPushButton(jendela_hal_utama)
        tombol_uploud.setGeometry(540, 600, 70, 70)
        tombol_uploud.setStyleSheet("QPushButton { border-image: url(upload.jpg); }")#masukkan foto ikon tombol upload di dalam kurung buka

        tombol_uploud.clicked.connect(UploadButton)

        label_upload = QLabel('Upload', jendela_hal_utama)
        label_upload.setStyleSheet('color: black;')
        label_upload.move(543, 670)
        label_upload.setFont(QFont('SansSerif', 13))
# mulai_Pencarian dokumen
        tombol_search.clicked.connect(pencarian_dokumen)#masukkan foto ikon tombol pencarian/ search didalam kurung buka

# akhir_pencarian dokumen
        perulangan_halutama += 1

        jendela_hal_utama.show()
        main_window.close()

    else:
        jendela_hal_utama.show()
        main_window.close()
   

#fungsi untuk jendela daftar akun

def Buatakun(): # jendela daftar akun
    global perulangan_buatakun
    

 
    
    if perulangan_buatakun == 0 :
        def cek_krkteruser():
            global value_username
            global status_user
            if len(username_input.text()) >= 8:
                status_user = ("Username  = Baik\n")
                value_username = 1
            else:
                status_user = ("Maaf Username anda terlalu pendek\n")
                value_username = 0
            
        def cek_krkterpw():
            global value_password
            global status_pw
            if len(password_input.text()) >= 8:
                status_pw = ("Password = Baik\n")
                value_password = 1
            else:
                status_pw = ("Maaf Password anda terlalu pendek\n")
                value_password = 0

        def cek_v_password():
            global value_v_password
            global status_v_password
            if (password_input.text()) == (v_password_input.text()):
                value_v_password = 1
                status_v_password = ("Ok sama")

            else:
                value_v_password = 0
                status_v_password = ("maaf tidak sama")
                
        def pesan_login():
            global kuncilogin
            QMessageBox.warning(window_daftar, 'Peringatan', status_user + status_pw )  #/ bisa ditambhkan di parameternya untuk cek kesamaan pw dan verif pw ( + status_v_password)   
            if value_password == 1 and value_username == 1 and value_v_password == 1:

                # data masuk ke database
                with open("daftar_akun.json", "r") as readfile:
                    data = json.load(readfile)  #ini ngebaca data dari json

                new_entry = {
                    "nama": (username_input.text()), # ini diisi QlineEdit.text()
                    "password": (password_input.text()),       # ini juga diisi QlineEdit.text()
                    "Ttl": (ttl_input.text()),    
                    "buku":[""]
                }


                data.append(new_entry) #ini gabungin data lama sama data yg mau ditambah

                with open("daftar_akun.json", "w") as writefile:
                    json.dump(data, writefile, indent=4) #ini yang nulis data ke json
                #akhir dari  data masuk ke database

                status_label.setText('Selamat akun anda telah terdaftar')
                # kuncilogin = 1
            else:
                status_label.setText("Maaf akun anda belum terdaftar, silahkan coba lagi")
            
        ttl_input = QDateEdit(window_daftar)
        ttl_input.setCalendarPopup(True) 
        
        username_input = QLineEdit(window_daftar)
        username_input.setPlaceholderText("Enter username")

        password_input = QLineEdit(window_daftar)
        password_input.setPlaceholderText("Enter password")

        v_password_input = QLineEdit(window_daftar)
        v_password_input.setPlaceholderText("Enter password")

        status_label = QLabel()

        tombol_daftar = QPushButton('Daftar', window_daftar)

        tombol_loginnext = QPushButton("Kembali", window_daftar)

        v_password_input.setEchoMode(QLineEdit.Password)


        #atribut widget
        tatlet.addWidget(QLabel('Date of Birth:'))
        tatlet.addWidget(ttl_input)
        tatlet.addWidget(QLabel('Username:'))
        tatlet.addWidget(username_input)
        tatlet.addWidget(QLabel('Password:'))
        tatlet.addWidget(password_input)
        tatlet.addWidget(QLabel('Verified Password:'))
        tatlet.addWidget(v_password_input)
        tatlet.addWidget(status_label)
        tatlet.addLayout(palet)
        palet.addWidget(tombol_daftar)
        palet.addWidget(tombol_loginnext)

        # Bagian tombol
        tombol_daftar.clicked.connect(cek_krkteruser) # cek karakater username
        tombol_daftar.clicked.connect(cek_krkterpw)# cek karakater password
        tombol_daftar.clicked.connect(cek_v_password)# cek karakater verified password

        tombol_daftar.clicked.connect(pesan_login) #pemeriksa apakah data inputan sesuai? 


        tombol_loginnext.clicked.connect(tombol_kembali_daftar)

        window_daftar.setLayout(tatlet)
        window_daftar.setLayout(palet)

        jendela_daftar.setCentralWidget(window_daftar)

        perulangan_buatakun +=1
        print(f"{perulangan_buatakun}")

        jendela_daftar.show()
        main_window.hide()
    else:
        jendela_daftar.show()
        main_window.hide()


#jendela login    start
app = QApplication(sys.argv)


main_window = QWidget()
main_window.setWindowTitle('ReadMe')
main_window.setGeometry(100, 30, 1200, 700)  # Atur ukuran awal jendela
global window_height
global window_width
window_width = main_window.frameGeometry().width()
window_height = main_window.frameGeometry().height()

# icon = QIcon('Logo ReadMe.jpg')
# main_window.setWindowIcon(icon)

icon_pixmap = QPixmap('Logo ReadMe.jpg')
icon = QIcon(icon_pixmap)
main_window.setWindowIcon(icon)




pixmap = QPixmap('Login.jpg')  # Masukkan gambar latar belakan jendela login
scaled_pixmap = pixmap.scaled(window_width, window_height)  # Sesuaikan gambar dengan ukuran jendela

Default_Font= QFont("TimesNewroman",14)

background_label = QLabel(main_window)
background_label.setPixmap(scaled_pixmap)
background_label.setGeometry(0, 0, window_width, window_height)  # Atur ukuran label sesuai dengan jendela

# status_label_login  = QLabel(main_window)
# status_label_login.setFont(Default_Font)
# status_label_login.move(350,100)
# status_label_login.setFixedWidth(1000)


input_nama = QLineEdit(main_window)
input_nama.move(400, 300,)
input_nama.setFixedWidth(400)
input_nama.setPlaceholderText("Masukkan username")

label_nama = QLabel(main_window)
label_nama.setText("Nama :")
label_nama.setFont(Default_Font)
label_nama.move(250, 295,)
label_nama.setFixedWidth(400)

input_password = QLineEdit(main_window)
input_password.move(400, 435)
input_password.setFixedWidth(400)
input_password.setPlaceholderText("Masukkan Password anda")
input_password.setEchoMode(QLineEdit.Password)


label_password = QLabel(main_window)
label_password.setText("Password :")
label_password.setFont(Default_Font)
label_password.move(250, 435,)
label_password.setFixedWidth(400)



bigucapan = QLabel(main_window)
bigucapan.setText("Selamat Datang")
Default_Font.setPointSize(40)
bigucapan.setFont(Default_Font)
bigucapan.move(360,180)
bigucapan.setFixedWidth(1000)



tombol_cari = QPushButton('LOGIN', main_window)
tombol_cari.move(560, 500)
tombol_cari.clicked.connect(login)

tombol_buat = QPushButton('Buat Akun', main_window)
tombol_buat.clicked.connect(Buatakun)
tombol_buat.move(560, 545)

main_window.show()
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#jendela pencarian
value_pencarian= 0
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#jendela upload

value_upload_button = 0

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Jendela halaman utama

perulangan_halutama = 0
# mulia_tampilan halaman utama
jendela_hal_utama = QWidget()
jendela_hal_utama.setWindowTitle('Halaman Utama')
jendela_hal_utama.setGeometry(90, 30, 1200, 700)  
jendela_hal_utama.setWindowIcon(icon)


window_width = jendela_hal_utama.frameGeometry().width()
window_height = jendela_hal_utama.frameGeometry().height()



pixmap = QPixmap('hal utama.jpg')#masukkan foto background jendela halaman utama
scaled_pixmap = pixmap.scaled(window_width, window_height)  

background_label = QLabel(jendela_hal_utama)
background_label.setPixmap(scaled_pixmap)
background_label.setGeometry(0, 0, window_width, window_height) 
#akhir_tampilan halaman utama
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#jendela daftar akun 

perulangan_buatakun = 0
jendela_daftar = QMainWindow()
jendela_daftar.setGeometry(100, 30, 1200, 700)
window_daftar = QWidget()
window_daftar.setWindowTitle('Daftar Akun')
tatlet = QVBoxLayout()
palet = QHBoxLayout()

pixmap_daftar_akun = QPixmap('Login.png')#masukkan foto background jendela login
scaled_pixmap = pixmap_daftar_akun.scaled(window_width, window_height)  


jendela_daftar.setWindowIcon(icon)

background_label = QLabel(jendela_daftar)
background_label.setPixmap(scaled_pixmap)
background_label.setGeometry(0, 0, window_width, window_height) 

# ///////////////////////////////
# jendela pemilihan

jendela_pemilihan = QWidget()
jendela_pemilihan.setWindowTitle('Pemilihan Dokumen')
jendela_pemilihan.setGeometry(100, 30, 1200, 700)
jendela_pemilihan.setWindowIcon(icon)

layout = QVBoxLayout()
#mulai_tmepat untuk memasukkan nama dokumen
input_cari = QLineEdit()
# akhir_ tmepat untuk memasukkan nama dokumen
button_cari = QPushButton('Cari Dokumen')
list_widget = QListWidget()
global input_cari_tterbit
input_cari_tterbit = QLineEdit()
layout_web = QHBoxLayout()
tombol_kembali_pemilihan = QPushButton("Kembali")
label_nama_dok = QLabel("Nama Dokumen :")
label_tterbit_dok = QLabel("Batas Minimum Tahun Terbit :")
label_background = QLabel(jendela_pemilihan)


Pixmap_Pencarian = QPixmap("Latar_polos.jpg")
skala_Pixmap= Pixmap_Pencarian.scaled(window_width,window_height)
label_background.setPixmap(skala_Pixmap)
label_background.setGeometry(0,0,window_width,window_height) 

layout.addWidget(label_nama_dok)
layout.addWidget(input_cari)
layout.addWidget(label_tterbit_dok)
layout.addWidget(input_cari_tterbit)
layout.addWidget(button_cari)
layout.addWidget(list_widget)
layout.addWidget(tombol_kembali_pemilihan)
# mulai_cek keberadaan dokumen di database
button_cari.clicked.connect(cari_dokumen)
# akhir_cek keberadaan dokumen di database
tombol_kembali_pemilihan.clicked.connect(tmbl_kembali_pemilihan)



# button_tampilkan.clicked.connect(tampilkan_pdf)



# ///////////////////////// Area jendela Pembayaran
jendela_pembayaran = QWidget()
jendela_pembayaran.setWindowTitle('ReadMe')
jendela_pembayaran.setGeometry(100, 30, 1200, 700)  # Atur ukuran awal jendela
jendela_pembayaran.setWindowIcon(icon)

window_width = jendela_pembayaran.frameGeometry().width()
window_height = jendela_pembayaran.frameGeometry().height()

# mulai_tampilan kode qris 
pixmap = QPixmap('Latar.jpg')  # Masukkan gambar latar belakan jendela login
scaled_pixmap = pixmap.scaled(window_width, window_height)  # Sesuaikan gambar dengan ukuran jendela
# akhir_tampilan kode qris 
Default_Font= QFont("TimesNewroman",14)

background_label = QLabel(jendela_pembayaran)
background_label.setPixmap(scaled_pixmap)
background_label.setGeometry(0, 0, window_width, window_height)  # Atur ukuran label sesuai dengan jendela

# status_label_login  = QLabel(jendela_pembayaran)
# status_label_login.setFont(Default_Font)
# status_label_login.move(350,100)
# status_label_login.setFixedWidth(1000)



bigucapan = QLabel(jendela_pembayaran)
bigucapan.setText("Pembayaran Dokumen")
Default_Font.setPointSize(40)
bigucapan.setFont(Default_Font)
bigucapan.move(280,10)
bigucapan.setFixedWidth(1000)
# mulai_print mohon untuk membayar
bigucapan_2 = QLabel(jendela_pembayaran)
bigucapan_2.setText("Mohon untul membayar")
Default_Font.setPointSize(30)
bigucapan_2.setFont(Default_Font)
bigucapan_2.move(330,100)
bigucapan_2.setFixedWidth(1000)
bigucapan_2.setStyleSheet('color: red;')

bigucapan_3 = QLabel(jendela_pembayaran)
bigucapan_3.setText("Apakah sudah membayar ?")
Default_Font.setPointSize(25)
bigucapan_3.setFont(Default_Font)
bigucapan_3.move(350,550)
bigucapan_3.setFixedWidth(1000)

# web_view = QWebEngineView()





sys.exit(app.exec_())


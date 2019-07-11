import  sys
import sqlite3
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):

    def __init__(self):    #pencere classı bir objeye atandığında ilk olarak bu fonksiyon çağrılır...

        super().__init__()

        self.baglantı_olustur()

        self.init_ui()

    def baglantı_olustur(self):

        baglantı=sqlite3.connect("database.db")

        self.cursor=baglantı.cursor()

        sorgu="create table If not exists uyeler(kullanıcı_adı TEXT,parola TEXT)"
        self.cursor.execute(sorgu)

        baglantı.commit()

    def init_ui(self):
        self.ad_bolumu=QtWidgets.QLabel("kullanıcı adı")
        self.parola_bolumu=QtWidgets.QLabel("parola")
        self.kullanıcı_adı=QtWidgets.QLineEdit() #input alma
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)   #yazıln parolanın görünmemesini sağlar
        self.giriş=QtWidgets.QPushButton("GİRİŞ YAP")
        self.kayıt=QtWidgets.QPushButton("KAYDET")
        self.yazı_alanı=QtWidgets.QLabel("")  #gereksiz olmuş bu satır
        self.setGeometry(100,100,500,500)


        v_box=QtWidgets.QVBoxLayout()

        v_box.addWidget(self.ad_bolumu)
        v_box.addWidget(self.kullanıcı_adı)
        v_box.addWidget(self.parola_bolumu)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()
        v_box.addWidget(self.giriş)
        v_box.addWidget(self.kayıt)

        h_box=QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi")
        self.giriş.clicked.connect(self.login)
        self.kayıt.clicked.connect(self.login)

        self.show()

    def login(self):
        adi=self.kullanıcı_adı.text()  #girilen inputu adi objesine aktarır
        par=self.parola.text()

        sender=self.sender()

        if(sender.text== "GİRİŞ YAP"):


            sorgu = "select * from uyeler where kullanıcı_adı=? and parola=? "
            self.cursor.execute(sorgu, (adi, par))
            data = self.cursor.fetchall()

            if (len(data) == 0):
                self.yazı_alanı.setText("lutfen bir daha deneyiniz...")
            else:
                self.yazı_alanı.setText("hosgeldiniz  " + adi)

        else:
            sorgu="insert into uyeler values(?,?)"
            self.cursor.execute(sorgu,(adi,par))
            self.baglantı.commit()
            self.yazı_alanı.setText("veri girişi başarılı")









app=QtWidgets.QApplication(sys.argv)

pencere=Pencere()

sys.exit(app.exec_())
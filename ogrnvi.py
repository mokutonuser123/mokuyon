from PySide2.QtWidgets import QApplication, QDialog , QMainWindow, QPushButton, QLabel, QCheckBox, QMessageBox, QButtonGroup, QHBoxLayout, QWidget, QVBoxLayout
from PySide2.QtGui import Qt,QIcon,QFont
from PySide2.QtCore import QDateTime,QTimer
from random import choice
from sys import argv,exit
import ctypes
from os import startfile
from psutil import process_iter
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
a=[]
def verial(s=""):
    if s!="":
       a.clear()
    with open("ogrenci.txt","r",encoding="utf8") as file:
        for satir in file :
            a.append(satir.strip("\n"))

verial()


class pencere(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ekran()
    def ekran(self):
        self.mylabel=QLabel(self)
        self.mylabel.resize(250,25)
        self.mylabel.move(0,20)
        self.mylabel.setAlignment(Qt.AlignCenter)
        self.font=self.mylabel.font()
        self.font.setPointSize(15)
        self.mylabel.setFont(self.font)
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle("Öğrenci Seç")
        self.setFixedSize(250,220)


        self.mybutton=QPushButton("Öğrenci seç",self)
        self.mybutton.move(80,43)
        self.mybutton.resize(80,30)
        self.mybutton.clicked.connect(self.sec)

        self.mylabel2=QLabel(self)
        self.font=self.mylabel2.font()
        self.font.setPointSize(15)
        self.mylabel2.setFont(self.font)
        self.mylabel2.move(110,70)

        self.chech1=QCheckBox("Listeden \n Silinme",self)
        self.chech1.move(150,100)
        self.chech2=QCheckBox("Listeden \n Sil",self)
        self.chech2.move(50,100)
        self.mybuttong=QButtonGroup()
        self.mybuttong.addButton(self.chech2)
        self.mybuttong.addButton(self.chech1)
        self.mybuttong.setExclusive(True)
        self.mybuttong.buttonClicked.connect(self.tik)

        self.epicen=QPushButton("EPİC \n PEN",self)
        self.epicen.clicked.connect(lambda :startfile("Epic Pen.lnk") if (len([i  for i in process_iter() if i.name().startswith("Epic") ] ) ==0) else None)

        self.font=self.epicen.font()
        self.font.setPointSize(10)
        self.epicen.setFont(self.font)
        self.epicen.resize(60,35)
        self.epicen.move(5,144)


        self.beyaz = QPushButton("BEYAZ \n EKRAN", self)
        self.beyaz.clicked.connect(self.beyaz_ekran)
        self.font = self.epicen.font()
        self.font.setPointSize(10)
        self.beyaz.setFont(self.font)
        self.beyaz.resize(60, 35)
        self.beyaz.move(65, 144)

        self.zaman = QPushButton("LGS \n ZAMAN", self)
        self.zaman.clicked.connect(self.lgs_zaman)
        self.font = self.epicen.font()
        self.font.setPointSize(10)
        self.zaman.setFont(self.font)
        self.zaman.resize(60, 35)
        self.zaman.move(125, 144)

        self.ozel = QPushButton("ÖZEL \n LİSTE", self)
        self.ozel.clicked.connect(self.ozel_liste)
        self.font = self.epicen.font()
        self.font.setPointSize(10)
        self.ozel.setFont(self.font)
        self.ozel.resize(60, 35)
        self.ozel.move(185, 144)

        self.b = QPushButton("İşlevsiz \n Buton", self)
        self.b.clicked.connect(self.beyaz_ekran)
        self.font = self.epicen.font()
        self.font.setPointSize(10)
        self.b.setFont(self.font)
        self.b.resize(60, 35)
        self.b.move(5, 184)

        self.b = QPushButton("İşlevsiz \n Buton", self)
        self.b.clicked.connect(self.beyaz_ekran)
        self.font = self.epicen.font()
        self.font.setPointSize(10)
        self.b.setFont(self.font)
        self.b.resize(60, 35)
        self.b.move(65, 184)

        self.b = QPushButton("İşlevsiz \n Buton", self)
        self.b.clicked.connect(self.beyaz_ekran)
        self.font = self.epicen.font()
        self.font.setPointSize(10)
        self.b.setFont(self.font)
        self.b.resize(60, 35)
        self.b.move(125, 184)

        self.b = QPushButton("İşlevsiz \n Buton", self)
        self.b.clicked.connect(self.beyaz_ekran)
        self.font = self.epicen.font()
        self.font.setPointSize(10)
        self.b.setFont(self.font)
        self.b.resize(60, 35)
        self.b.move(185, 184)




        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(self.windowFlags() &~Qt.WindowMinMaxButtonsHint)
    def ozel_liste(self):
        print("sa")
    def lgs_zaman(self):
        ts = QDialog()
        layout = QHBoxLayout()
        layout2 = QHBoxLayout()

        font = QFont('Arial', 80, QFont.Bold)


        self.gun = QLabel()
        self.gun.setAlignment(Qt.AlignCenter)
        self.gun.setFont(font)
        self.saat = QLabel()
        self.saat.setAlignment(Qt.AlignCenter)
        self.saat.setFont(font)
        self.dakika = QLabel()
        self.dakika.setAlignment(Qt.AlignCenter)
        self.dakika.setFont(font)
        self.saniye = QLabel()
        self.saniye.setAlignment(Qt.AlignCenter)
        self.saniye.setFont(font)

        # adding label to the layout
        layout.addWidget(self.gun)
        layout.addWidget(self.saat)
        layout2.addWidget(self.dakika)
        layout2.addWidget(self.saniye)

        layout3 = QVBoxLayout()
        layw = QWidget()
        layw.setLayout(layout)
        lay2w = QWidget()
        lay2w.setLayout(layout2)
        layout3.addWidget(layw)
        layout3.addWidget(lay2w)
        ts.setLayout(layout3)

        # creating a timer object
        timer = QTimer(self)
        # adding action to timer
        timer.timeout.connect(self.showDateTime)

        self.showDateTime()
        timer.start(1000)
        ts.setWindowFlags(Qt.WindowStaysOnTopHint)
        ts.exec_()

        timer.stop()
    def showDateTime(self):

        current_datetime = QDateTime.currentDateTime()
        end_datetime = QDateTime(2023, 6, 4, 9, 0, 0)
        remaining_time = current_datetime.secsTo(end_datetime)
        days, seconds = divmod(remaining_time, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        self.gun.setText(str(days)+"\n Gün")
        self.saat.setText(str(hours)+"\n Saat")
        self.dakika.setText(str(minutes)+"\n Dakika")
        self.saniye.setText(str(seconds)+"\n Saniye")
    def beyaz_ekran(self):
        beyaz_ekra = QDialog()
        beyaz_ekra.showMaximized()
        beyaz_ekra.setWindowTitle("Beyaz Ekran")
        beyaz_ekra.exec_()
    def tik(self):
        verial("a")
        self.mylabel2.setText("")
        self.mylabel.setText("")
    def sec(self):

        if self.chech2.isChecked():
            if len(a)==0:
                self.mylabel.setText("Liste bitti")
                verial()
            else:
                secil=choice(a)
                self.mylabel.setText(secil)
                a.remove(secil)
                self.mylabel2.setText(str(len(a)))

        elif self.chech1.isChecked():
            self.mylabel.setText(choice(a))
            self.mylabel2.setText("")
        else:
            msgbox=QMessageBox()
            msgbox.setIcon(QMessageBox.Critical)
            msgbox.setWindowTitle("HATA")
            msgbox.setText("Lütfen seçenek seçiniz")
            msgbox.setWindowFlags(Qt.WindowStaysOnTopHint)
            msgbox.exec_()
def start():
    app=QApplication(argv)
    ekran=pencere()
    ekran.show()
    exit(app.exec_())
start()
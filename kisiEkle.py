# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kisiEkleUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ogrenci_Kayit(object):
    def setupUi(self, Ogrenci_Kayit):
        Ogrenci_Kayit.setObjectName("Ogrenci_Kayit")
        Ogrenci_Kayit.resize(625, 788)
        Ogrenci_Kayit.setStyleSheet("background-color: rgb(226, 255, 253);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.centralwidget = QtWidgets.QWidget(Ogrenci_Kayit)
        self.centralwidget.setObjectName("centralwidget")
        self.lbKamera = QtWidgets.QLabel(self.centralwidget)
        self.lbKamera.setGeometry(QtCore.QRect(340, 400, 251, 211))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lbKamera.setFont(font)
        self.lbKamera.setStyleSheet("")
        self.lbKamera.setText("")
        self.lbKamera.setObjectName("lbKamera")
        self.btnKaydet = QtWidgets.QPushButton(self.centralwidget)
        self.btnKaydet.setGeometry(QtCore.QRect(10, 630, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.btnKaydet.setFont(font)
        self.btnKaydet.setObjectName("btnKaydet")
        self.btnTenmizle = QtWidgets.QPushButton(self.centralwidget)
        self.btnTenmizle.setGeometry(QtCore.QRect(170, 630, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.btnTenmizle.setFont(font)
        self.btnTenmizle.setObjectName("btnTenmizle")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 117, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 8, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 30, 461, 251))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtAd = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtAd.setFont(font)
        self.txtAd.setObjectName("txtAd")
        self.verticalLayout_2.addWidget(self.txtAd)
        self.txtSoyad = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtSoyad.setFont(font)
        self.txtSoyad.setObjectName("txtSoyad")
        self.verticalLayout_2.addWidget(self.txtSoyad)
        self.txtOgrNo = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtOgrNo.setFont(font)
        self.txtOgrNo.setObjectName("txtOgrNo")
        self.verticalLayout_2.addWidget(self.txtOgrNo)
        self.comboSinif = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.comboSinif.setFont(font)
        self.comboSinif.setObjectName("comboSinif")
        self.verticalLayout_2.addWidget(self.comboSinif)
        self.txtVeliTel = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtVeliTel.setFont(font)
        self.txtVeliTel.setObjectName("txtVeliTel")
        self.verticalLayout_2.addWidget(self.txtVeliTel)
        self.txtVeliMail = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtVeliMail.setFont(font)
        self.txtVeliMail.setObjectName("txtVeliMail")
        self.verticalLayout_2.addWidget(self.txtVeliMail)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_Erkek = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radio_Erkek.setFont(font)
        self.radio_Erkek.setObjectName("radio_Erkek")
        self.horizontalLayout.addWidget(self.radio_Erkek)
        self.radio_Kiz = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radio_Kiz.setFont(font)
        self.radio_Kiz.setObjectName("radio_Kiz")
        self.horizontalLayout.addWidget(self.radio_Kiz)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.btnFotoCek = QtWidgets.QPushButton(self.centralwidget)
        self.btnFotoCek.setGeometry(QtCore.QRect(340, 630, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.btnFotoCek.setFont(font)
        self.btnFotoCek.setObjectName("btnFotoCek")
        self.btnKameraAc = QtWidgets.QPushButton(self.centralwidget)
        self.btnKameraAc.setGeometry(QtCore.QRect(340, 340, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.btnKameraAc.setFont(font)
        self.btnKameraAc.setObjectName("btnKameraAc")
        self.fotoList = QtWidgets.QListWidget(self.centralwidget)
        self.fotoList.setGeometry(QtCore.QRect(10, 330, 301, 281))
        self.fotoList.setObjectName("fotoList")
        self.spinbox_fotosayisi = QtWidgets.QSpinBox(self.centralwidget)
        self.spinbox_fotosayisi.setGeometry(QtCore.QRect(140, 290, 31, 20))
        self.spinbox_fotosayisi.setObjectName("spinbox_fotosayisi")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 121, 16))
        self.label_9.setObjectName("label_9")
        Ogrenci_Kayit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ogrenci_Kayit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 21))
        self.menubar.setObjectName("menubar")
        Ogrenci_Kayit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ogrenci_Kayit)
        self.statusbar.setObjectName("statusbar")
        Ogrenci_Kayit.setStatusBar(self.statusbar)

        self.retranslateUi(Ogrenci_Kayit)
        QtCore.QMetaObject.connectSlotsByName(Ogrenci_Kayit)

    def retranslateUi(self, Ogrenci_Kayit):
        _translate = QtCore.QCoreApplication.translate
        Ogrenci_Kayit.setWindowTitle(_translate("Ogrenci_Kayit", "MainWindow"))
        self.btnKaydet.setText(_translate("Ogrenci_Kayit", "Kaydet"))
        self.btnTenmizle.setText(_translate("Ogrenci_Kayit", "Temizle"))
        self.label.setText(_translate("Ogrenci_Kayit", "Ad :"))
        self.label_2.setText(_translate("Ogrenci_Kayit", "Soyad :"))
        self.label_4.setText(_translate("Ogrenci_Kayit", "Öğr-No :"))
        self.label_3.setText(_translate("Ogrenci_Kayit", "Sınıf :"))
        self.label_6.setText(_translate("Ogrenci_Kayit", "Veli Telefon:"))
        self.label_7.setText(_translate("Ogrenci_Kayit", "Veli E-posta:"))
        self.label_5.setText(_translate("Ogrenci_Kayit", "Cinsiyet:"))
        self.label_8.setText(_translate("Ogrenci_Kayit", "Fotoğraf Sayısı:"))
        self.radio_Erkek.setText(_translate("Ogrenci_Kayit", "Erkek"))
        self.radio_Kiz.setText(_translate("Ogrenci_Kayit", "Kız"))
        self.btnFotoCek.setText(_translate("Ogrenci_Kayit", "Fotoğrafları Çek"))
        self.btnKameraAc.setText(_translate("Ogrenci_Kayit", "Kamerayı Aç"))
        self.label_9.setText(_translate("Ogrenci_Kayit", "@LegendMan46"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ogrenci_Kayit = QtWidgets.QMainWindow()
    ui = Ui_Ogrenci_Kayit()
    ui.setupUi(Ogrenci_Kayit)
    Ogrenci_Kayit.show()
    sys.exit(app.exec_())

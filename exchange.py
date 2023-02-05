import os
import sys
from bs4 import BeautifulSoup
import requests
from urllib.request import Request,urlopen

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer,QTime,QDateTime
from PyQt5.QtWidgets import QApplication,QDialog,QWidget,QStackedWidget,QFileDialog
from PyQt5.QtGui import QIcon

class exhange(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        loadUi(r"C:\Users\bugra\OneDrive\Masaüstü\döviz-program\döviz.ui",self)

        self.timer = QTimer(self)

        self.timer.timeout.connect(self.current)
        # 1 saniye 1000 milisaniye
        self.timer.start(1000)



    def current(self):
        self.kur()

        self.label_5.setText(self.dolar)
        self.label_6.setText(self.euro)
        self.label_7.setText(self.sterlin)

    def kur(self):
        url = "https://uzmanpara.milliyet.com.tr/doviz-kurlari/"
        response = requests.get(url)
        html = response.content

        soup = BeautifulSoup(html,"html.parser")

        self.c = soup.find_all("div",attrs={"class":"realTimeBoxL"})

        self.dolar = ""
        self.euro = ""
        self.sterlin = ""

        for i in self.c:
            if self.dolar == "":
                self.dolar = i.text[9:]
                continue

            if self.euro == "":
                self.euro = i.text[9:]
                continue

            if self.sterlin == "":
                self.sterlin = i.text[9:]
                continue

        print("dolar",self.dolar)
        print("euro", self.euro)
        print("sterlin", self.sterlin)



app = QApplication(sys.argv)
ana = exhange()
widget = QStackedWidget()
widget.addWidget(ana)
widget.setWindowTitle("anlık döviz")
widget.setWindowIcon(QIcon(r"C:\Users\bugra\OneDrive\Masaüstü\döviz-program\dolar.png"))
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("çıkılıyor")
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaSistema.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(729, 525)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelLink = QtWidgets.QLabel(self.centralwidget)
        self.labelLink.setGeometry(QtCore.QRect(20, 20, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelLink.setFont(font)
        self.labelLink.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.labelLink.setObjectName("labelLink")
        self.entradaLinkDeDownload = QtWidgets.QLineEdit(self.centralwidget)
        self.entradaLinkDeDownload.setGeometry(QtCore.QRect(230, 20, 391, 31))
        self.entradaLinkDeDownload.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-radius: 5px;")
        self.entradaLinkDeDownload.setObjectName("entradaLinkDeDownload")
        self.buttonBaixar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBaixar.setGeometry(QtCore.QRect(630, 20, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonBaixar.setFont(font)
        self.buttonBaixar.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: white;\n"
"border-radius: 5px;")
        self.buttonBaixar.setObjectName("buttonBaixar")
        self.buttonAbrirPastaDeDestino = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAbrirPastaDeDestino.setGeometry(QtCore.QRect(130, 490, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonAbrirPastaDeDestino.setFont(font)
        self.buttonAbrirPastaDeDestino.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: white;\n"
"border-radius: 5px;")
        self.buttonAbrirPastaDeDestino.setObjectName("buttonAbrirPastaDeDestino")
        self.frameListagemDeDownloads = QtWidgets.QFrame(self.centralwidget)
        self.frameListagemDeDownloads.setGeometry(QtCore.QRect(10, 220, 711, 261))
        self.frameListagemDeDownloads.setStyleSheet("background-color: rgb(61, 61, 61);")
        self.frameListagemDeDownloads.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameListagemDeDownloads.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameListagemDeDownloads.setObjectName("frameListagemDeDownloads")
        self.listagemDeDownloads = QtWidgets.QListWidget(self.frameListagemDeDownloads)
        self.listagemDeDownloads.setGeometry(QtCore.QRect(0, 0, 711, 261))
        self.listagemDeDownloads.setStyleSheet("color: white;\n"
"font-size: 17px;\n"
"font-weight: bold;")
        self.listagemDeDownloads.setObjectName("listagemDeDownloads")
        self.labelLink_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelLink_2.setGeometry(QtCore.QRect(270, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelLink_2.setFont(font)
        self.labelLink_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.labelLink_2.setObjectName("labelLink_2")
        self.progresso = QtWidgets.QProgressBar(self.centralwidget)
        self.progresso.setGeometry(QtCore.QRect(230, 140, 521, 31))
        self.progresso.setProperty("value", 0)
        self.progresso.setObjectName("progresso")
        self.buttonSalvarEm = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSalvarEm.setGeometry(QtCore.QRect(60, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonSalvarEm.setFont(font)
        self.buttonSalvarEm.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: white;\n"
"border-radius: 5px;")
        self.buttonSalvarEm.setObjectName("buttonSalvarEm")
        self.entradaDestino = QtWidgets.QLineEdit(self.centralwidget)
        self.entradaDestino.setGeometry(QtCore.QRect(230, 60, 391, 31))
        self.entradaDestino.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-radius: 5px;")
        self.entradaDestino.setObjectName("entradaDestino")
        self.labelErro = QtWidgets.QLabel(self.centralwidget)
        self.labelErro.setGeometry(QtCore.QRect(220, 100, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelErro.setFont(font)
        self.labelErro.setStyleSheet("color: rgb(255, 0, 0);")
        self.labelErro.setText("")
        self.labelErro.setObjectName("labelErro")
        self.buttonRemover = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRemover.setGeometry(QtCore.QRect(10, 490, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonRemover.setFont(font)
        self.buttonRemover.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: white;\n"
"border-radius: 5px;")
        self.buttonRemover.setObjectName("buttonRemover")
        self.labelLink_4 = QtWidgets.QLabel(self.centralwidget)
        self.labelLink_4.setGeometry(QtCore.QRect(30, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelLink_4.setFont(font)
        self.labelLink_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.labelLink_4.setObjectName("labelLink_4")
        self.labelLink.raise_()
        self.entradaLinkDeDownload.raise_()
        self.buttonBaixar.raise_()
        self.buttonAbrirPastaDeDestino.raise_()
        self.frameListagemDeDownloads.raise_()
        self.labelLink_2.raise_()
        self.buttonSalvarEm.raise_()
        self.entradaDestino.raise_()
        self.labelErro.raise_()
        self.buttonRemover.raise_()
        self.labelLink_4.raise_()
        self.progresso.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sertec Music  Downloader"))
        self.labelLink.setText(_translate("MainWindow", "LINK DA MUSICA NO YOUTUBE"))
        self.buttonBaixar.setText(_translate("MainWindow", "BAIXAR"))
        self.buttonAbrirPastaDeDestino.setText(_translate("MainWindow", "ABRIR PASTA DE DESTINO"))
        self.labelLink_2.setText(_translate("MainWindow", "DOWNLOADS"))
        self.buttonSalvarEm.setText(_translate("MainWindow", "Selecionar Destino"))
        self.buttonRemover.setText(_translate("MainWindow", "REMOVER"))
        self.labelLink_4.setText(_translate("MainWindow", "PROGRESSO DO DOWNLOAD"))

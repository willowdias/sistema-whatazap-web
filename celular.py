import sqlite3
from PyQt5 import uic, QtWidgets
import sqlite3
from PyQt5.QtGui import QPixmap,QIcon
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from contato import*
class sistema(QtWidgets.QDialog):
    def __init__(self):
        super(sistema, self).__init__()
        uic.loadUi('TELEFONE.ui', self)
        self.show()
        self.setWindowIcon(QIcon("iconescanner/inicial.ico"))
        self.pushButton.clicked.connect(self.telefone)
        self.pushButton_2.clicked.connect(self.cadastro)
        self.numeross()
  
    def cadastro(self):
        self.telefone=cadastro()
        self.telefone.show()
    def telefone(self):
      
    
        import pywhatkit
        import keyboard
        import time
        from datetime import datetime

        contatos = self.lineEdit.text()
        texto=self.texto.text()

        contatos2 = self.lineEdit_2.text()
        texto=self.texto.text()

        contatos3 = self.lineEdit_3.text()
        texto=self.texto.text()
        
        contatos4 = self.lineEdit_4.text()
        texto=self.texto.text()

        contatos5 = self.lineEdit_5.text()
        texto=self.texto.text()

        contatos6 = self.lineEdit_6.text()
        texto=self.texto.text()

        contatos7 = self.lineEdit_7.text()
        texto=self.texto.text()
        
        contatos8 = self.lineEdit_8.text()
        texto=self.texto.text()
    
        #while len(contatos) >=1:
        #pywhatkit.sendwhatmsg(contatos, texto, datetime.now().hour, datetime.now().minute + 2)
        pywhatkit.sendwhatmsg(contatos,texto,datetime.now().hour, datetime.now().minute + 1)
        time.sleep(5)
        keyboard.press_and_release('ctrl + w')
        pywhatkit.sendwhatmsg(contatos2,texto,datetime.now().hour, datetime.now().minute + 1)
             
        time.sleep(5)
        keyboard.press_and_release('ctrl + w')

        pywhatkit.sendwhatmsg(contatos3,texto,datetime.now().hour, datetime.now().minute + 1)
             
        time.sleep(5)
        keyboard.press_and_release('ctrl + w')

        pywhatkit.sendwhatmsg(contatos4,texto,datetime.now().hour, datetime.now().minute + 1)
             
        time.sleep(5)
        keyboard.press_and_release('ctrl + w')

        pywhatkit.sendwhatmsg(contatos5,texto,datetime.now().hour, datetime.now().minute + 1)
             
        time.sleep(5)
        keyboard.press_and_release('ctrl + w')

        pywhatkit.sendwhatmsg(contatos6,texto,datetime.now().hour, datetime.now().minute + 1)
             
        time.sleep(5)
        keyboard.press_and_release('ctrl + w')

        pywhatkit.sendwhatmsg(contatos7,texto,datetime.now().hour, datetime.now().minute + 1)
             
        time.sleep(5)
        keyboard.press_and_release('ctrl + w')

        pywhatkit.sendwhatmsg(contatos8,texto,datetime.now().hour, datetime.now().minute + 1)
             
        time.sleep(5)
        keyboard.press_and_release('ctrl + w')
        self.lineEdit.setText("+5569")
        self.lineEdit_2.setText("+5569")
        self.lineEdit_3.setText("+5569")
        self.lineEdit_4.setText("+5569")
        self.lineEdit_5.setText("+5569")
        self.lineEdit_6.setText("+5569")
        self.lineEdit_7.setText("+5569")
        self.lineEdit_8.setText("+5569")

    def numeross(self):
        lista=['+556992702408']
        self.comboBox.addItems(lista)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = sistema()
    sys.exit(app.exec_())
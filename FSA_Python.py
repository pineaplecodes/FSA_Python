from cgitb import text
from string import ascii_letters
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest

 
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(700, 550)
        Dialog.setStyleSheet("QWidget#Dialog{\n"
"background-color: qlineargradient(spread:pad, x1:0.660945, y1:0.909, x2:0, y2:0, stop:0 rgba(219, 251, 241, 255), stop:1 rgba(254, 203, 197, 255));}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 18pt \"Yu Gothic UI\";\n"
"") 
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(False)
        self.label.setIndent(0)
        self.label.setObjectName("label")
#input Nama :
        self.inputNama = QtWidgets.QLineEdit(Dialog)
        self.inputNama.setGeometry(QtCore.QRect(200, 140, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(9)
        self.inputNama.setFont(font)
        self.inputNama.setText("")
        self.inputNama.setReadOnly(False)
        self.inputNama.setObjectName("inputNama")
#Input Nim :
        self.inputNim = QtWidgets.QLineEdit(Dialog)
        self.inputNim.setGeometry(QtCore.QRect(200, 200, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(9)
        self.inputNim.setFont(font)
        self.inputNim.setStyleSheet("gridline-color: rgb(9, 9, 9);")
        self.inputNim.setText("")
        self.inputNim.setObjectName("inputNim")
#Tombol Mulai
        self.buttonStart = QtWidgets.QPushButton(Dialog)
        self.buttonStart.setGeometry(QtCore.QRect(300, 250, 93, 35))
        self.buttonStart.clicked.connect(self.clickStart)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buttonStart.setFont(font)
        self.buttonStart.setStyleSheet("font: 10pt \"Segoe UI Symbol\";\n""background-color: rgb(251, 207, 207);")
        self.buttonStart.setObjectName("buttonStart")
#Output Status Nama
        self.statusNama = QtWidgets.QLabel(Dialog)
        self.statusNama.setGeometry(QtCore.QRect(540, 330, 121, 20))
        self.statusNama.setStyleSheet("font: 9pt \"Segoe UI Symbol\";")
        self.statusNama.setText("")
        self.statusNama.setObjectName("statusNama")
#Ouput Status Nim
        self.statusNim = QtWidgets.QLabel(Dialog)
        self.statusNim.setGeometry(QtCore.QRect(540, 400, 131, 20))
        self.statusNim.setStyleSheet("font: 9pt \"Segoe UI Symbol\";")
        self.statusNim.setText("")
        self.statusNim.setObjectName("statusNim")
#Tombol Hapus
        self.buttonDelete = QtWidgets.QPushButton(Dialog)
        self.buttonDelete.setGeometry(QtCore.QRect(300, 460, 93, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buttonDelete.setFont(font)
        self.buttonDelete.setStyleSheet("font: 10pt \"Segoe UI Symbol\";\n"
"background-color: rgb(251, 207, 207);")
        self.buttonDelete.setObjectName("buttonDelete")
        self.buttonDelete.clicked.connect(self.clickDelete)
#Output Hasil Nama
        self.outputNama = QtWidgets.QLabel(Dialog)
        self.outputNama.setGeometry(QtCore.QRect(200, 320, 281, 31))
        self.outputNama.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.outputNama.setFrameShape(QtWidgets.QFrame.Box)
        self.outputNama.setText("")
        self.outputNama.setObjectName("outputNama")
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(9)
        self.outputNama.setFont(font)
#Ouput Hasil Nim
        self.outputNim = QtWidgets.QLabel(Dialog)
        self.outputNim.setGeometry(QtCore.QRect(200, 390, 281, 31))
        self.outputNim.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.outputNim.setFrameShape(QtWidgets.QFrame.Box)
        self.outputNim.setText("")
        self.outputNim.setObjectName("outputNim")
        font.setFamily("Noto Sans")
        font.setPointSize(9)
        self.outputNim.setFont(font)
#Tulisan Judul Nama
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(200, 120, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 10pt \"Segoe UI Symbol\";")
        self.label_8.setObjectName("label_8")
#Tulisan Judul Nim
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(200, 180, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 10pt \"Segoe UI Symbol\";")
        self.label_9.setObjectName("label_9")
 
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
#Tulisan-Text
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Project"))
        self.label.setText(_translate("Dialog", "Implementasi FSA Pada Pemrograman"))
        self.buttonStart.setText(_translate("Dialog", "Mulai"))
        # self.labelNama.setText(_translate("Dialog", "Karakter "))
        # self.labelNim.setText(_translate("Dialog", "Karakter "))
        self.buttonDelete.setText(_translate("Dialog", "Hapus"))
        self.label_8.setText(_translate("Dialog", "Nama "))
        self.label_9.setText(_translate("Dialog", "NIM"))
#Scan Karakter 
        self.scanNama = QtWidgets.QLabel(Dialog)
        self.scanNama.setGeometry(QtCore.QRect(500, 320, 31, 31))
        self.scanNama.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"Segoe UI Symbol\";")
        self.scanNama.setFrameShape(QtWidgets.QFrame.Box)
        self.scanNama.setText("")
        self.scanNama.setObjectName("scanNama")
        self.scanNama.setAlignment(QtCore.Qt.AlignCenter)
 
        self.scanNim = QtWidgets.QLabel(Dialog)
        self.scanNim.setGeometry(QtCore.QRect(500, 390, 31, 31))
        self.scanNim.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"Segoe UI Symbol\";")
        self.scanNim.setFrameShape(QtWidgets.QFrame.Box)
        self.scanNim.setText("")
        self.scanNim.setObjectName("scanNim")
        self.scanNim.setAlignment(QtCore.Qt.AlignCenter)
#Final State
        self.hasilNama = QtWidgets.QLabel(Dialog)
        self.hasilNama.setGeometry(QtCore.QRect(200, 350, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hasilNama.setFont(font)
        self.hasilNama.setText("")
        self.hasilNama.setObjectName("hasilNama")
        self.hasilNim = QtWidgets.QLabel(Dialog)
        self.hasilNim.setGeometry(QtCore.QRect(200, 420, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hasilNim.setFont(font)
        self.hasilNim.setText("")
        self.hasilNim.setObjectName("hasilNim")
#Process Setelah Menekan Tombol Mulai
    def clickStart(self,teks = None):
        #Deklarasi variabel yang dibutuhkan 
        nama = self.inputNama.text()
        textProcess = ''
        angka = self.inputNim.text()
        numProcess = " " 
        tambahNama =" "
        tambahNim = " "
        for x in range(len(nama)) : 
            textProcess = nama[x]
            for y in " " +ascii_letters : 
                # textProcess += nama[x]
                textProcess = textProcess.replace(textProcess[0:len(textProcess)],textProcess[0:len(textProcess)-1]+y) if x>0 else textProcess.replace(textProcess[0],y)
                self.scanNama.setText(textProcess)
                QtTest.QTest.qWait(200)
                if y == nama[x]: 
                        tambahNama += y
                        self.scanNama.clear()
                        self.statusNama.setText("Karakter Diterima")
                        QtTest.QTest.qWait(200)
                        break
                if y != nama[x]:
                        self.statusNama.setText("Karakter Ditolak")
                        QtTest.QTest.qWait(200)
                        self.statusNama.clear()
                        continue 
            self.outputNama.setText(tambahNama)
        self.hasilNama.setText("String dikenali")
                        

        for a in range(len(angka)) :
            numProcess = angka[a]
            for b in '1234567890' :
                numProcess = numProcess.replace(numProcess[0:len(numProcess)],numProcess[0:len(numProcess)-1]+b) if a > 0 else numProcess.replace(numProcess[0],b)
                self.scanNim.setText(numProcess)
                QtTest.QTest.qWait(200)
                if b == angka[a] :
                        tambahNim += b
                        self.scanNim.clear()
                        QtTest.QTest.qWait(200)
                        self.statusNim.setText("Karakter Diterima")
                        break
                if b != angka[a]:
                        self.statusNim.clear()
                        QtTest.QTest.qWait(200)
                        self.statusNim.setText("Karakter Ditolak")
                        continue
            self.outputNim.setText(tambahNim)
        self.hasilNim.setText("String dikenali")
   
#Proses setelah menekan tombol Hapus
    def clickDelete(self, text=None):
        self.inputNama.clear()
        self.inputNim.clear()
        self.outputNama.clear()
        self.outputNim.clear()
        self.statusNama.clear()
        self.statusNim.clear()
        self.hasilNama.clear()
        self.hasilNim.clear()
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())   
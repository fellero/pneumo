# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_v0.0.2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import random   


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(212, 214, 232);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 180))
        self.frame.setStyleSheet("background-color: rgb(236, 235, 244);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.unit_lablel_0 = QtWidgets.QTextBrowser(self.frame)
        self.unit_lablel_0.setGeometry(QtCore.QRect(100, 10, 120, 30))
        self.unit_lablel_0.setStyleSheet("background-color: rgb(255, 163, 72);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.unit_lablel_0.setFrameShape(QtWidgets.QFrame.Box)
        self.unit_lablel_0.setObjectName("unit_lablel_0")
        self.current_value_0 = QtWidgets.QTextBrowser(self.frame)
        self.current_value_0.setGeometry(QtCore.QRect(80, 50, 160, 60))
        self.current_value_0.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.current_value_0.setFrameShape(QtWidgets.QFrame.Box)
        self.current_value_0.setObjectName("current_value_0")
        self.target_value_0 = QtWidgets.QTextBrowser(self.frame)
        self.target_value_0.setGeometry(QtCore.QRect(90, 120, 141, 31))
        self.target_value_0.setStyleSheet("background-color: rgb(5, 13, 152);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.target_value_0.setFrameShape(QtWidgets.QFrame.Box)
        self.target_value_0.setObjectName("target_value_0")
        self.unit_label_1 = QtWidgets.QTextBrowser(self.frame)
        self.unit_label_1.setGeometry(QtCore.QRect(580, 10, 120, 30))
        self.unit_label_1.setStyleSheet("background-color: rgb(255, 163, 72);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.unit_label_1.setFrameShape(QtWidgets.QFrame.Box)
        self.unit_label_1.setObjectName("unit_label_1")
        self.current_value_1 = QtWidgets.QTextBrowser(self.frame)
        self.current_value_1.setGeometry(QtCore.QRect(560, 50, 160, 60))
        self.current_value_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.current_value_1.setFrameShape(QtWidgets.QFrame.Box)
        self.current_value_1.setObjectName("current_value_1")
        self.target_value_1 = QtWidgets.QTextBrowser(self.frame)
        self.target_value_1.setGeometry(QtCore.QRect(570, 120, 141, 31))
        self.target_value_1.setStyleSheet("background-color: rgb(5, 13, 152);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.target_value_1.setFrameShape(QtWidgets.QFrame.Box)
        self.target_value_1.setObjectName("target_value_1")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(350, 10, 118, 23))
        self.progressBar.setProperty("value", 99)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 10, 30, 30))
        self.pushButton.setStyleSheet("border-radius : 15; \n"
"  border : 2px solid black;\n"
"background-color: rgb(31, 39, 156);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 120, 30, 30))
        self.pushButton_2.setStyleSheet("border-radius : 15; \n"
"  border : 2px solid black;\n"
"background-color: rgb(31, 39, 156);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(740, 10, 30, 30))
        self.pushButton_5.setStyleSheet("border-radius : 15; \n"
"  border : 2px solid black;\n"
"background-color: rgb(31, 39, 156);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(740, 120, 30, 30))
        self.pushButton_7.setStyleSheet("border-radius : 15; \n"
"  border : 2px solid black;\n"
"background-color: rgb(31, 39, 156);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 180, 800, 180))
        self.frame_2.setStyleSheet("background-color: rgb(246, 245, 244);\n"
"background-color: rgb(153, 193, 241);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.unit_label_2 = QtWidgets.QTextBrowser(self.frame_2)
        self.unit_label_2.setGeometry(QtCore.QRect(100, 10, 120, 30))
        self.unit_label_2.setStyleSheet("background-color: rgb(255, 163, 72);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.unit_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.unit_label_2.setObjectName("unit_label_2")
        self.current_value_2 = QtWidgets.QTextBrowser(self.frame_2)
        self.current_value_2.setGeometry(QtCore.QRect(80, 50, 160, 60))
        self.current_value_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.current_value_2.setFrameShape(QtWidgets.QFrame.Box)
        self.current_value_2.setObjectName("current_value_2")
        self.target_value_2 = QtWidgets.QTextBrowser(self.frame_2)
        self.target_value_2.setGeometry(QtCore.QRect(90, 120, 141, 31))
        self.target_value_2.setStyleSheet("background-color: rgb(5, 13, 152);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.target_value_2.setFrameShape(QtWidgets.QFrame.Box)
        self.target_value_2.setObjectName("target_value_2")
        self.unit_label_3 = QtWidgets.QTextBrowser(self.frame_2)
        self.unit_label_3.setGeometry(QtCore.QRect(580, 10, 120, 30))
        self.unit_label_3.setStyleSheet("background-color: rgb(255, 163, 72);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.unit_label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.unit_label_3.setObjectName("unit_label_3")
        self.current_value_3 = QtWidgets.QTextBrowser(self.frame_2)
        self.current_value_3.setGeometry(QtCore.QRect(560, 50, 160, 60))
        self.current_value_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.current_value_3.setFrameShape(QtWidgets.QFrame.Box)
        self.current_value_3.setObjectName("current_value_3")
        self.target_value_3 = QtWidgets.QTextBrowser(self.frame_2)
        self.target_value_3.setGeometry(QtCore.QRect(570, 120, 141, 31))
        self.target_value_3.setStyleSheet("background-color: rgb(5, 13, 152);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.target_value_3.setFrameShape(QtWidgets.QFrame.Box)
        self.target_value_3.setObjectName("target_value_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 10, 30, 30))
        self.pushButton_3.setStyleSheet("border-radius : 15; \n"
"  border : 2px solid black;\n"
"background-color: rgb(31, 39, 156);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 120, 30, 30))
        self.pushButton_4.setStyleSheet("border-radius : 15; \n"
"  border : 2px solid black;\n"
"background-color: rgb(31, 39, 156);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(740, 10, 30, 30))
        self.pushButton_6.setStyleSheet("border-radius : 15; \n"
"  border : 2px solid black;\n"
"background-color: rgb(31, 39, 156);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(740, 120, 30, 30))
        self.pushButton_8.setStyleSheet("border-radius : 15; \n"
"  border : 2px solid black;\n"
"background-color: rgb(31, 39, 156);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.message_space = QtWidgets.QTextEdit(self.centralwidget)
        self.message_space.setGeometry(QtCore.QRect(260, 410, 270, 131))
        self.message_space.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.message_space.setFrameShape(QtWidgets.QFrame.Box)
        self.message_space.setObjectName("message_space")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 380, 270, 20))
        self.label.setStyleSheet("\n"
"font: 75 11pt \"Carlito\";\n"
"font-color:rgb(20, 20, 205)")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 360, 240, 90))
        self.frame_3.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.textBrowser_21 = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser_21.setGeometry(QtCore.QRect(50, 10, 131, 51))
        self.textBrowser_21.setStyleSheet("background-color: rgb(255, 163, 72);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.textBrowser_21.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_21.setObjectName("textBrowser_21")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(550, 360, 251, 90))
        self.frame_4.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.textBrowser_20 = QtWidgets.QTextBrowser(self.frame_4)
        self.textBrowser_20.setGeometry(QtCore.QRect(50, 10, 131, 51))
        self.textBrowser_20.setStyleSheet("background-color: rgb(255, 163, 72);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Carlito\";")
        self.textBrowser_20.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_20.setObjectName("textBrowser_20")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.start_selection()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Messages"))

    def start_selection(self):
        # Repeating timer, calls random_pick over and over.
        self.picktimer = QTimer()
        self.picktimer.setInterval(500)
        self.picktimer.timeout.connect(self.random_pick)
        self.picktimer.start()

    def random_pick(self):
        self.current_value_0.setText(str(random.randint(0, 10)))
        self.current_value_1.setText(str(random.randint(0, 10)))
        self.current_value_2.setText(str(random.randint(0, 10)))
        self.current_value_3.setText(str(random.randint(0, 10)))
        self.progressBar.setValue(random.randint(0, 100))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_5.setText(_translate("MainWindow", " 5"))
        self.pushButton_7.setText(_translate("MainWindow", "6"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.label.setText(_translate("MainWindow", "Messages"))

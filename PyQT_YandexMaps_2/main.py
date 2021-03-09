#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
import os
import requests
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 771, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 761, 441))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Координаты\n"
" через запятую:"))
        self.label_2.setText(_translate("MainWindow", "Масштаб\n"
                                        " через запятую:"))
        self.pushButton.setText(_translate("MainWindow", "Показать"))
        self.pushButton.clicked.connect(self.show_png)
        self.lineEdit_2.setText('0.002,0.002')
        self.start_m = 0
    
    def create_map(self, first, second, m):              # create_map function
        coords = f"{first},{second}"
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords}&spn={m}&l=map"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
            
        self.pixmap = QPixmap(self.map_file)
        self.label_3.setPixmap(self.pixmap)
        
        
    def show_png(self):
        coords = self.lineEdit.text()
        m = self.lineEdit_2.text()
        self.start_m = m
        f = coords.split(',')[1]
        s = coords.split(',')[0]
        self.create_map(f, s, m)

        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:                # W Key
            coords = self.lineEdit.text()
            m = self.lineEdit_2.text()
            if float(m.split(',')[0]) < float(self.start_m.split(',')[0]) + 0.5 and float(m.split(',')[1]) < float(self.start_m.split(',')[1]) + 0.5:
                m = f"{str(float(m.split(',')[0]))},{str(float(m.split(',')[1]) + float(m.split(',')[1]))}"
                self.lineEdit_2.setText(m)
                f = coords.split(',')[1]
                s = coords.split(',')[0]
                self.create_map(f, s, m)
                
        elif event.key() == Qt.Key_S:            # S Key
            coords = self.lineEdit.text()
            m = self.lineEdit_2.text()
            if m != self.start_m:    
                m = f"{str(float(m.split(',')[0]))},{str(float(m.split(',')[1]) - float(m.split(',')[1]) / 2)}"
                self.lineEdit_2.setText(m)
                f = coords.split(',')[1]
                s = coords.split(',')[0]
                self.create_map(f, s, m)

            
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())





# In[ ]:





# In[ ]:





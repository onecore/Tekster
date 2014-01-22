####################################################################################
##
## Copyright (C) 2011-2013 CoreSEC Software Development Group. All rights reserved.
##
##
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
##          http://www.hacore.sf.net/forum/license.html
## If you are unsure which license is appropriate for your use, please
## review the following information:
##
##
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
####################################################################################

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
import urllib

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(756, 781)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(756, 781))
        MainWindow.setMaximumSize(QtCore.QSize(756, 781))
        #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow{\n"
"background-image: url(TeskterImages/bgs.png);\n"
"}\n"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("background-image: url(TeskterImages/bgs.png);"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 70, 431, 141))
        self.plainTextEdit.setStyleSheet(_fromUtf8("background: #3498db;/*#5b6bab;*/\n"
"\n"
"\n"
"\n"
"border-radius: 21px 21px 14px 14px;\n"
"\n"
"border: 3px outset #f2f2f2;"))
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 100, 71, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: #ffffff;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 140, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: #ffffff;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(50, 220, 661, 501))
        self.plainTextEdit_2.setStyleSheet(_fromUtf8("background: #3498db;/*#5b6bab;*/\n"
"\n"
"\n"
"\n"
"border-radius: 21px 21px 54px 14px;\n"
"\n"
"border: 3px outset #f2f2f2;"))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.MessageBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.MessageBox.setGeometry(QtCore.QRect(100, 310, 381, 351))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.MessageBox.setFont(font)
        self.MessageBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MessageBox.setStyleSheet(_fromUtf8("background: #66696b;/*#5b6bab;*/\n"
"\n"
"color: #ffffff;\n"
"\n"
"border-radius: 32px 45px 54px 50px;\n"
"\n"
"border: 2px outset #f2f2f2;\n"
"\n"
"\n"
"  padding: 15px 10px 15px 10px;"))
        self.MessageBox.setLineWidth(10)
        self.MessageBox.setMidLineWidth(0)
        self.MessageBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MessageBox.setTabStopWidth(80)
        self.MessageBox.setMaximumBlockCount(0)
        self.MessageBox.setBackgroundVisible(False)
        self.MessageBox.setCenterOnScroll(True)
        self.MessageBox.setObjectName(_fromUtf8("MessageBox"))
        self.TeksterLogo = QtGui.QLabel(self.centralwidget)
        self.TeksterLogo.setGeometry(QtCore.QRect(480, 0, 201, 81))
        self.TeksterLogo.setStyleSheet(_fromUtf8("background: transparent;\n"
"image: url(:/newPrefix/Untitled-1.png);"))
        self.TeksterLogo.setText(_fromUtf8(""))
        self.TeksterLogo.setPixmap(QtGui.QPixmap(_fromUtf8("TeskterImages/Untitled-1.png")))
        self.TeksterLogo.setScaledContents(True)
        self.TeksterLogo.setObjectName(_fromUtf8("TeksterClose"))

        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 734, 190, 22))
        self.comboBox.setStyleSheet(_fromUtf8("QComboBox {\n"
"    border: 3px outset #f2f2f2;\n"
"    border-radius: 8px 8px 8px 8px;\n"

"    padding: 1px 1px 1px 1px;\n"
"    min-width: 6em;\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: #ffffff;\n"
"    margin: 0 0 0 0;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: rgb(80, 80, 80);\n"
"}\n"
"\n"
"QComboBox:!editable {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"}\n"
"\n"
"QComboBox::drop-down:editable {background: #ffffff\n"
"}\n"
"\n"
"QComboBox:!editable:on {\n"
"}\n"
"\n"
"QComboBox::drop-down:editable:on {\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 15px; \n"
"    right:3px;\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"    background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(TeskterImages/closetekster.png);\n"
"    height: 10px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QListView#comboListView {\n"
"    background: rgb(80, 80, 80);\n"
"    color: rgb(220, 220, 220);\n"
"    min-height: 90px;\n"
"    margin: 0 0 0 0;\n"
"}\n"
"\n"
"QListView#comboListView::item {\n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"QListView#comboListView::item:hover {\n"
"    background-color: rgb(95, 95, 95);\n"
"}"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))




        #self.TeksterClose.setGeometry(QtCore.QRect(50, 8, 48, 48))
        self.TeksterClose = QtGui.QPushButton(self.centralwidget)
        self.TeksterClose.setGeometry(QtCore.QRect(10, 10, 48, 48))
        self.TeksterClose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TeksterClose.setStyleSheet(_fromUtf8("QPushButton{ \n"
"border-image: url(TeskterImages/closetekster.png);}\n"
"QPushButton:hover {\n"
"border-image: url(TeskterImages/hover.png);}\n"))
        self.TeksterClose.setObjectName(_fromUtf8("TeksterClose"))


        self.TeksterMinimize = QtGui.QPushButton(self.centralwidget)
        self.TeksterMinimize.setGeometry(QtCore.QRect(60, 20, 26, 30))
        self.TeksterMinimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TeksterMinimize.setStyleSheet(_fromUtf8("QPushButton{ \n"
"border-image: url(TeskterImages/minimizetekster.png);}\n"
"QPushButton:hover {\n"
"border-image: url(TeskterImages/MinHoverTekster.png);}\n"))
        self.TeksterMinimize.setObjectName(_fromUtf8("TeksterMinimize"))



        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 600, 361, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet(_fromUtf8(" QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"background-image: -webkit-linear-gradient(top, #66696b, #353a3d);\n"
" background-image: -moz-linear-gradient(top, #66696b, #353a3d);\n"
" background-image: -ms-linear-gradient(top, #66696b, #353a3d);\n"
" background-image: -o-linear-gradient(top, #66696b, #353a3d);\n"
" background-image: linear-gradient(to bottom, #66696b, #353a3d);\n"
" -webkit-border-radius: 28;\n"
"-moz-border-radius: 28;\n"
"border-radius: 25px 25px 54px 14px;\n"
"  font-family: Arial;\n"
" color: #ffffff;\n"
"font-size: 18px;\n"
" padding: 5px 5px 5px 5px;\n"
"text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3cb0fd, stop: 1 #3498db);\n"
" background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
" background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
" background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
" background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"text-decoration: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #0d5ca6, stop: 1 #2198c0);\n"
"}\n"
"\n"
""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.NumberBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.NumberBox.setGeometry(QtCore.QRect(170, 270, 191, 21))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.NumberBox.setFont(font)
        self.NumberBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NumberBox.setStyleSheet(_fromUtf8("background: #66696b;/*#5b6bab;*/\n"
"\n"
"\n"
"color: #ffffff;\n"
"border-radius: 7px 7px 7px 30px;\n"
"\n"
"border: 1px outset #f2f2f2;"))
        self.NumberBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.NumberBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.NumberBox.setObjectName(_fromUtf8("NumberBox"))
        self.PasswordPlainTextEditBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.PasswordPlainTextEditBox.setGeometry(QtCore.QRect(180, 140, 261, 21))
        self.PasswordPlainTextEditBox.setStyleSheet(_fromUtf8("background: #66696b;/*#5b6bab;*/\n"
"\n"
"\n"
"color: #ffffff;\n"
"border-radius: 7px 7px 7px 30px;\n"
"\n"
"border: 1px outset #f2f2f2;"))
        self.PasswordPlainTextEditBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PasswordPlainTextEditBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PasswordPlainTextEditBox.setObjectName(_fromUtf8("PasswordPlainTextEditBox"))
        self.UsernamePlainTextEditBox = QtGui.QLineEdit(self.centralwidget)
        self.UsernamePlainTextEditBox.setGeometry(QtCore.QRect(180, 100, 261, 21))

        self.UsernamePlainTextEditBox.setStyleSheet(_fromUtf8("background: #66696b;/*#5b6bab;*/\n"
"\n"
"\n"
"color: #ffffff;\n"
"border-radius: 7px 7px 7px 30px;\n"
"\n"
"border: 1px outset #f2f2f2;"))
        #self.UsernamePlainTextEditBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.UsernamePlainTextEditBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.UsernamePlainTextEditBox.setObjectName(_fromUtf8("UsernamePlainTextEditBox"))
        self.OpenSaveUserButton = QtGui.QPushButton(self.centralwidget)
        self.OpenSaveUserButton.setGeometry(QtCore.QRect(277, 170, 81, 31))
        self.OpenSaveUserButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OpenSaveUserButton.setStyleSheet(_fromUtf8("QPushButton{ \n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b6f73, stop: 1 #4e5457);\n"
" background-image: -webkit-linear-gradient(top, #3498db, #2980b9);\n"
" background-image: -moz-linear-gradient(top, #3498db, #2980b9);\n"
" background-image: -ms-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3498db, #2980b9);\n"
" background-image: linear-gradient(to bottom, #3498db, #2980b9);\n"
" -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 11px;\n"
"  font-family: Arial;\n"
" color: #ffffff;\n"
"  font-size: 11px;\n"
" padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background: #3cb0fd;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"text-decoration: none;\n"
"}"))
        self.OpenSaveUserButton.setObjectName(_fromUtf8("OpenSaveUserButton"))





        self.SaveCurrentUserButton = QtGui.QPushButton(self.centralwidget)
        self.SaveCurrentUserButton.setGeometry(QtCore.QRect(360, 170, 81, 31))
        self.SaveCurrentUserButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveCurrentUserButton.setStyleSheet(_fromUtf8("QPushButton{ \n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b6f73, stop: 1 #4e5457);\n"
" background-image: -webkit-linear-gradient(top, #3498db, #2980b9);\n"
" background-image: -moz-linear-gradient(top, #3498db, #2980b9);\n"
" background-image: -ms-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3498db, #2980b9);\n"
" background-image: linear-gradient(to bottom, #3498db, #2980b9);\n"
" -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 11px;\n"
"  font-family: Arial;\n"
" color: #ffffff;\n"
"  font-size: 11px;\n"
" padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background: #3cb0fd;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"text-decoration: none;\n"
"}"))
        self.SaveCurrentUserButton.setObjectName(_fromUtf8("SaveCurrentUserButton"))






        self.ActivateBoxesButton = QtGui.QPushButton(self.centralwidget)
        self.ActivateBoxesButton.setGeometry(QtCore.QRect(180, 170, 94, 31))
        self.ActivateBoxesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ActivateBoxesButton.setStyleSheet(_fromUtf8("QPushButton{ \n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b6f73, stop: 1 #4e5457);\n"
" background-image: -webkit-linear-gradient(top, #3498db, #2980b9);\n"
" background-image: -moz-linear-gradient(top, #3498db, #2980b9);\n"
" background-image: -ms-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3498db, #2980b9);\n"
" background-image: linear-gradient(to bottom, #3498db, #2980b9);\n"
" -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 11px;\n"
"  font-family: Arial;\n"
" color: #ffffff;\n"
"  font-size: 11px;\n"
" padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background: #3cb0fd;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"text-decoration: none;\n"
"}"))
        self.ActivateBoxesButton.setObjectName(_fromUtf8("ActivateBoxesButton"))






        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 270, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: #ffffff;"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.plainTextEdit_5 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_5.setEnabled(False)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(490, 90, 221, 121))
        self.plainTextEdit_5.setStyleSheet(_fromUtf8("background: #3498db;/*#5b6bab;*/\n"
"\n"
"\n"
"\n"
"border-radius: 21px 21px 14px 14px;\n"
"\n"
"border: 3px outset #f2f2f2;"))
        self.plainTextEdit_5.setObjectName(_fromUtf8("plainTextEdit_5"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 110, 51, 51))
        self.label_4.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("TeskterImages/GMAIL ICON.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 120, 111, 31))
        self.label_5.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("TeskterImages/logo_mail.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(570, 130, 16, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: #ffffff;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.MoreInfoButton = QtGui.QPushButton(self.centralwidget)
        self.MoreInfoButton.setGeometry(QtCore.QRect(530, 170, 151, 31))
        self.MoreInfoButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #3cb0fd; /*#66696b;*/\n"
"  background-image: -webkit-linear-gradient(top, #66696b, #353a3d);\n"
"  background-image: -moz-linear-gradient(top, #66696b, #353a3d);\n"
"  background-image: -ms-linear-gradient(top, #66696b, #353a3d);\n"
"  background-image: -o-linear-gradient(top, #66696b, #353a3d);\n"
"  background-image: linear-gradient(to bottom, #66696b, #353a3d);\n"
"  -webkit-border-radius: 60;\n"
"  -moz-border-radius: 60;\n"
"  border-radius: 60px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 9px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66696b;/*#3cb0fd;*/\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}"))
        self.MoreInfoButton.setObjectName(_fromUtf8("MoreInfoButton"))
        self.AddtoContactsButton = QtGui.QPushButton(self.centralwidget)
        self.AddtoContactsButton.setGeometry(QtCore.QRect(370, 270, 91, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.AddtoContactsButton.setFont(font)
        self.AddtoContactsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AddtoContactsButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #3cb0fd; /*#66696b;*/\n"
"\n"
"  border-radius: 10px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 9px;\n"
"  padding: 5px 10px 5px 10px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66696b;/*#3cb0fd;*/\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}"))
        self.AddtoContactsButton.setObjectName(_fromUtf8("AddtoContactsButton"))
        self.CharactersCountfromMessageBox = QtGui.QSpinBox(self.centralwidget)
        self.CharactersCountfromMessageBox.setGeometry(QtCore.QRect(430, 570, 31, 22))
        self.CharactersCountfromMessageBox.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: #ffffff;"))
        self.CharactersCountfromMessageBox.setWrapping(False)
        self.CharactersCountfromMessageBox.setFrame(False)
        self.CharactersCountfromMessageBox.setReadOnly(True)
        self.CharactersCountfromMessageBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.CharactersCountfromMessageBox.setAccelerated(True)
        self.CharactersCountfromMessageBox.setPrefix(_fromUtf8(""))
        self.CharactersCountfromMessageBox.setMaximum(500)
        self.CharactersCountfromMessageBox.setObjectName(_fromUtf8("CharactersCountfromMessageBox"))
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        self.toolBox.setEnabled(True)
        self.toolBox.setGeometry(QtCore.QRect(500, 310, 201, 351))
        self.toolBox.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: #ffffff;"))


        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.StatusTab = QtGui.QWidget()
        self.StatusTab.setGeometry(QtCore.QRect(0, 0, 201, 279))
        self.StatusTab.setObjectName(_fromUtf8("StatusTab"))
        self.label_8 = QtGui.QLabel(self.StatusTab)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 161, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.StatusTab)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 171, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.StatusTab)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.LatestVersionLabel = QtGui.QLabel(self.StatusTab)
        self.LatestVersionLabel.setGeometry(QtCore.QRect(140, 70, 21, 20))
        self.LatestVersionLabel.setObjectName(_fromUtf8("LatestVersionLabel"))
        self.label_12 = QtGui.QLabel(self.StatusTab)
        self.label_12.setGeometry(QtCore.QRect(20, 90, 71, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.EmailServerLabel = QtGui.QLabel(self.StatusTab)
        self.EmailServerLabel.setGeometry(QtCore.QRect(110, 90, 71, 16))
        self.EmailServerLabel.setObjectName(_fromUtf8("EmailServerLabel"))
        self.label_14 = QtGui.QLabel(self.StatusTab)
        self.label_14.setGeometry(QtCore.QRect(20, 110, 41, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.ErrorBoxShow = QtGui.QPlainTextEdit(self.StatusTab)
        self.ErrorBoxShow.setGeometry(QtCore.QRect(20, 130, 151, 71))
        self.ErrorBoxShow.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: #ffffff;\n"
"border: transparent;"))
        self.ErrorBoxShow.setObjectName(_fromUtf8("ErrorBoxShow"))
        self.label_15 = QtGui.QLabel(self.StatusTab)
        self.label_15.setGeometry(QtCore.QRect(0, 240, 191, 41))
        self.label_15.setStyleSheet(_fromUtf8("font: 9px;"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.CheckForUpdate = QtGui.QPushButton(self.StatusTab)
        self.CheckForUpdate.setGeometry(QtCore.QRect(10, 212, 181, 21))
        self.CheckForUpdate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CheckForUpdate.setStyleSheet(_fromUtf8("QPushButton{ \n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b6f73, stop: 1 #4e5457);\n"
" background-image: -webkit-linear-gradient(top, #3498db, #2980b9);\n"
" background-image: -moz-linear-gradient(top, #3498db, #2980b9);\n"
" background-image: -ms-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3498db, #2980b9);\n"
" background-image: linear-gradient(to bottom, #3498db, #2980b9);\n"
" -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 6px;\n"
"  font-family: Arial;\n"
" color: #ffffff;\n"
"  font-size: 11px;\n"
" padding: 0px 0px 0px 0px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background: #3cb0fd;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"text-decoration: none;\n"
"}"))
        self.CheckForUpdate.setObjectName(_fromUtf8("CheckForUpdate"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("TeskterImages/button_delete_violet.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolBox.addItem(self.StatusTab, icon, _fromUtf8(""))
        self.ContactsTab = QtGui.QWidget()
        self.ContactsTab.setGeometry(QtCore.QRect(0, 0, 201, 279))
        self.ContactsTab.setObjectName(_fromUtf8("ContactsTab"))
        self.label_16 = QtGui.QLabel(self.ContactsTab)
        self.label_16.setGeometry(QtCore.QRect(70, 5, 71, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.ContactsTab)
        self.label_17.setGeometry(QtCore.QRect(10, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.ContactsTab)
        self.label_18.setGeometry(QtCore.QRect(0, 65, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.AddtoContactNameBOX = QtGui.QPlainTextEdit(self.ContactsTab)
        self.AddtoContactNameBOX.setGeometry(QtCore.QRect(50, 30, 141, 21))
        self.AddtoContactNameBOX.setStyleSheet(_fromUtf8("background: #ffffff;\n"
"color: #000000;  border-radius: 6px;"))
        self.AddtoContactNameBOX.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddtoContactNameBOX.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddtoContactNameBOX.setObjectName(_fromUtf8("AddtoContactNameBOX"))
        self.AddtoContactNumberBOX = QtGui.QPlainTextEdit(self.ContactsTab)
        self.AddtoContactNumberBOX.setGeometry(QtCore.QRect(50, 60, 141, 21))
        self.AddtoContactNumberBOX.setStyleSheet(_fromUtf8("background: #ffffff;\n"
"color: #000000;  border-radius: 6px;"))
        self.AddtoContactNumberBOX.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddtoContactNumberBOX.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddtoContactNumberBOX.setObjectName(_fromUtf8("AddtoContactNumberBOX"))
        self.ContactsListBOX = QtGui.QPlainTextEdit(self.ContactsTab)
        self.ContactsListBOX.setGeometry(QtCore.QRect(0, 130, 191, 121))
        self.ContactsListBOX.setStyleSheet(_fromUtf8("background: #ffffff;\n"
"color: #000000;  border-radius: 6px;"))
        self.ContactsListBOX.setReadOnly(True)
        self.ContactsListBOX.setPlainText(_fromUtf8(""))
        self.ContactsListBOX.setObjectName(_fromUtf8("ContactsListBOX"))
        self.label_19 = QtGui.QLabel(self.ContactsTab)
        self.label_19.setGeometry(QtCore.QRect(0, 110, 46, 13))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.AddtoContactBUTTON = QtGui.QPushButton(self.ContactsTab)
        self.AddtoContactBUTTON.setGeometry(QtCore.QRect(130, 90, 61, 21))
        self.AddtoContactBUTTON.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #66696b;\n"
"  background-image: -webkit-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3498db, #2980b9);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 5px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 11px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #3cb0fd;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}"))
        self.AddtoContactBUTTON.setObjectName(_fromUtf8("AddtoContactBUTTON"))
        self.ShowFullContacts = QtGui.QPushButton(self.ContactsTab)
        self.ShowFullContacts.setGeometry(QtCore.QRect(40, 254, 111, 21))
        self.ShowFullContacts.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #66696b;\n"
"  background-image: -webkit-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3498db, #2980b9);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 5px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 11px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #3cb0fd;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}"))
        self.ShowFullContacts.setObjectName(_fromUtf8("ShowFullContacts"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("TeskterImages/button_delete_violet.png")), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.toolBox.addItem(self.ContactsTab, icon1, _fromUtf8(""))
        self.SettingsTab = QtGui.QWidget()
        self.SettingsTab.setGeometry(QtCore.QRect(0, 0, 201, 279))
        self.SettingsTab.setObjectName(_fromUtf8("SettingsTab"))
        self.label_20 = QtGui.QLabel(self.SettingsTab)
        self.label_20.setGeometry(QtCore.QRect(50, 10, 121, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.ChangeSMSGateWayBox = QtGui.QPlainTextEdit(self.SettingsTab)
        self.ChangeSMSGateWayBox.setGeometry(QtCore.QRect(0, 30, 201, 21))
        font = QtGui.QFont()
        font.setKerning(False)
        self.ChangeSMSGateWayBox.setFont(font)
        self.ChangeSMSGateWayBox.setStyleSheet(_fromUtf8("background: #ffffff;\n"
"color: #000000;"))
        self.ChangeSMSGateWayBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ChangeSMSGateWayBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ChangeSMSGateWayBox.setPlainText(_fromUtf8(""))
        self.ChangeSMSGateWayBox.setObjectName(_fromUtf8("ChangeSMSGateWayBox"))
        self.label_21 = QtGui.QLabel(self.SettingsTab)
        self.label_21.setGeometry(QtCore.QRect(50, 60, 111, 21))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.textEdit = QtGui.QTextEdit(self.SettingsTab)
        self.textEdit.setGeometry(QtCore.QRect(10, 80, 181, 231))
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.toolBox.addItem(self.SettingsTab, icon1, _fromUtf8(""))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 730, 161, 16))
        font = QtGui.QFont()
        font.setKerning(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_3.setLineWidth(0)
        self.label_3.setText(_fromUtf8("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; color:#888888;\">Tekster  | Send Free SMS Application</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setObjectName(_fromUtf8("label_3"))




        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(330, 740, 261, 16))
        self.label_11.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_23 = QtGui.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(600, 730, 111, 31))
        self.label_23.setStyleSheet(_fromUtf8("background: transparent;\n"
"border-image: url(:/newPrefix/hacoresec.png);"))
        self.label_23.setText(_fromUtf8(""))
        self.label_23.setPixmap(QtGui.QPixmap(_fromUtf8("TeskterImages/hacoresec.png")))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.DecimalLabel = QtGui.QLabel(self.centralwidget)
        self.DecimalLabel.setGeometry(QtCore.QRect(480, 140, 21, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.DecimalLabel.setFont(font)
        self.DecimalLabel.setStyleSheet(_fromUtf8("color: #ffffff;\n"
"background: transparent;\n"
""))
        self.DecimalLabel.setObjectName(_fromUtf8("DecimalLabel"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 670, 21, 23))
        self.pushButton.setStyleSheet(_fromUtf8("border-image: url(TeskterImages/Grin.png);\n"
"\n"
"background: transparent;"))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.HeartEyeEmoticon = QtGui.QPushButton(self.centralwidget)
        self.HeartEyeEmoticon.setGeometry(QtCore.QRect(180, 670, 21, 23))
        self.HeartEyeEmoticon.setStyleSheet(_fromUtf8("border-image: url(TeskterImages/Heart.png);\n"
"background: transparent;"))
        self.HeartEyeEmoticon.setText(_fromUtf8(""))
        self.HeartEyeEmoticon.setObjectName(_fromUtf8("HeartEyeEmoticon"))
        self.LaughEmoticon = QtGui.QPushButton(self.centralwidget)
        self.LaughEmoticon.setGeometry(QtCore.QRect(120, 670, 21, 23))
        self.LaughEmoticon.setStyleSheet(_fromUtf8("border-image: url(TeskterImages/Laugh.png);\n"
"\n"
"background: transparent;"))
        self.LaughEmoticon.setText(_fromUtf8(""))
        self.LaughEmoticon.setObjectName(_fromUtf8("LaughEmoticon"))
        self.OhhNooEmoticon = QtGui.QPushButton(self.centralwidget)
        self.OhhNooEmoticon.setGeometry(QtCore.QRect(210, 670, 21, 23))
        self.OhhNooEmoticon.setStyleSheet(_fromUtf8("border-image: url(TeskterImages/ohnoes.png);\n"
"\n"
"background: transparent;"))
        self.OhhNooEmoticon.setText(_fromUtf8(""))
        self.OhhNooEmoticon.setObjectName(_fromUtf8("OhhNooEmoticon"))
        self.DisappointEmoticon = QtGui.QPushButton(self.centralwidget)
        self.DisappointEmoticon.setGeometry(QtCore.QRect(240, 670, 21, 23))
        self.DisappointEmoticon.setStyleSheet(_fromUtf8("border-image: url(TeskterImages/Ambivalent.png);\n"
"\n"
"background: transparent;"))
        self.DisappointEmoticon.setText(_fromUtf8(""))
        self.DisappointEmoticon.setObjectName(_fromUtf8("DisappointEmoticon"))
        self.ConfuseEmoticon = QtGui.QPushButton(self.centralwidget)
        self.ConfuseEmoticon.setGeometry(QtCore.QRect(270, 670, 21, 23))
        self.ConfuseEmoticon.setStyleSheet(_fromUtf8("border-image: url(TeskterImages/Confused.png);\n"
"\n"
"background: transparent;"))
        self.ConfuseEmoticon.setText(_fromUtf8(""))
        self.ConfuseEmoticon.setObjectName(_fromUtf8("ConfuseEmoticon"))
        self.GeniusEmoticon = QtGui.QPushButton(self.centralwidget)
        self.GeniusEmoticon.setGeometry(QtCore.QRect(300, 670, 21, 23))
        self.GeniusEmoticon.setStyleSheet(_fromUtf8("border-image: url(TeskterImages/Hot.png);\n"
"\n"
"background: transparent;"))
        self.GeniusEmoticon.setText(_fromUtf8(""))
        self.GeniusEmoticon.setObjectName(_fromUtf8("GeniusEmoticon"))
        self.AngryEmoticon = QtGui.QPushButton(self.centralwidget)
        self.AngryEmoticon.setGeometry(QtCore.QRect(330, 670, 21, 23))
        self.AngryEmoticon.setStyleSheet(_fromUtf8("border-image: url(TeskterImages/VeryAngry.png);\n"
"\n"
"background: transparent;"))
        self.AngryEmoticon.setText(_fromUtf8(""))
        self.AngryEmoticon.setObjectName(_fromUtf8("AngryEmoticon"))
        self.CryingEmoticon = QtGui.QPushButton(self.centralwidget)
        self.CryingEmoticon.setGeometry(QtCore.QRect(360, 670, 21, 23))
        self.CryingEmoticon.setStyleSheet(_fromUtf8("border-image: url(TeskterImages/Crying.png);\n"
"\n"
"background: transparent;"))
        self.CryingEmoticon.setText(_fromUtf8(""))
        self.CryingEmoticon.setObjectName(_fromUtf8("CryingEmoticon"))
        self.BleehEmoticon = QtGui.QPushButton(self.centralwidget)
        self.BleehEmoticon.setGeometry(QtCore.QRect(390, 670, 21, 23))
        self.BleehEmoticon.setStyleSheet(_fromUtf8("border-image: url(TeskterImages/Sticking Out Tongue.png);\n"
"\n"
"background: transparent;"))
        self.BleehEmoticon.setText(_fromUtf8(""))
        self.BleehEmoticon.setObjectName(_fromUtf8("BleehEmoticon"))
        self.WinkEmoticon = QtGui.QPushButton(self.centralwidget)
        self.WinkEmoticon.setGeometry(QtCore.QRect(420, 670, 21, 23))
        self.WinkEmoticon.setStyleSheet(_fromUtf8("border-image: url(TeskterImages/Wink.png);\n"
"\n"
"background: transparent;"))
        self.WinkEmoticon.setText(_fromUtf8(""))
        self.WinkEmoticon.setObjectName(_fromUtf8("WinkEmoticon"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 670, 21, 23))
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #3cb0fd; /*#66696b;*/\n"
"  background-image: -webkit-linear-gradient(top, #66696b, #353a3d);\n"
"  background-image: -moz-linear-gradient(top, #66696b, #353a3d);\n"
"  background-image: -ms-linear-gradient(top, #66696b, #353a3d);\n"
"  background-image: -o-linear-gradient(top, #66696b, #353a3d);\n"
"  background-image: linear-gradient(to bottom, #66696b, #353a3d);\n"
"  -webkit-border-radius: 60;\n"
"  -moz-border-radius: 60;\n"
"  border-radius: 60px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 9px;\n"
"  padding: 1px 2px 1px 2px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66696b;/*#3cb0fd;*/\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 670, 91, 21))
        self.pushButton_4.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #3cb0fd; /*#66696b;*/\n"
"\n"
"  border-radius: 10px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 9px;\n"
"  padding: 5px 10px 5px 10px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66696b;/*#3cb0fd;*/\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(600, 670, 101, 21))
        self.pushButton_5.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #3cb0fd; /*#66696b;*/\n"
"\n"
"  border-radius: 10px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 9px;\n"
"  padding: 5px 10px 5px 10px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66696b;/*#3cb0fd;*/\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(620, 240, 41, 19))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.horizontalSlider.setMouseTracking(False)
        self.horizontalSlider.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.horizontalSlider.setToolTip(_fromUtf8(""))
        self.horizontalSlider.setStatusTip(_fromUtf8(""))
        self.horizontalSlider.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: #ffffff;\n"
"border-color: #ffffff;"))
        self.horizontalSlider.setMaximum(1)
        self.horizontalSlider.setSingleStep(2)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.label_24 = QtGui.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(590, 240, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(_fromUtf8("background: transparent;\n"
"\n"
"color: #ffffff;"))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(670, 240, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(_fromUtf8("background: transparent;\n"
"\n"
"color: #ffffff;"))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        self.toolBox.layout().setSpacing(0)


        QtCore.QObject.connect(self.ActivateBoxesButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ActivateBoxesButtonFunction)
        QtCore.QObject.connect(self.TeksterMinimize, QtCore.SIGNAL(_fromUtf8("clicked()")), self.teksterMinimizeFunction)
        QtCore.QObject.connect(self.TeksterClose, QtCore.SIGNAL(_fromUtf8("clicked()")), self.teksterCloseFunction)
        QtCore.QObject.connect(self.MessageBox, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.CharactersCountfromMessageBox.stepUp)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.teksterSendFunction)
        QtCore.QObject.connect(self.MoreInfoButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.MoreInformationFunction)
        QtCore.QObject.connect(self.CheckForUpdate, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CheckForUpdatesFunction)
        QtCore.QObject.connect(self.SaveCurrentUserButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.SaveCredentialsFunction)
        QtCore.QObject.connect(self.OpenSaveUserButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenSaveCredentialsFunction)
        QtCore.QObject.connect(self.AddtoContactsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.AddToContactsFunction)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ContactUsFunction)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.SentMessagesFunction)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ShowFullSmileysListFunction)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.UpupEmoticonFunction)
        QtCore.QObject.connect(self.LaughEmoticon, QtCore.SIGNAL(_fromUtf8("clicked()")), self.LaughEmoticonFunction)
        QtCore.QObject.connect(self.HeartEyeEmoticon, QtCore.SIGNAL(_fromUtf8("clicked()")), self.HeartEyesEmoticonFunction)
        QtCore.QObject.connect(self.OhhNooEmoticon, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ConfusedEmoticonFunction)
        QtCore.QObject.connect(self.DisappointEmoticon, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.MadEmoticonFunction)
        QtCore.QObject.connect(self.ConfuseEmoticon, QtCore.SIGNAL(_fromUtf8("clicked()")), self.TwirlEmoticonFunction)
        QtCore.QObject.connect(self.GeniusEmoticon, QtCore.SIGNAL(_fromUtf8("clicked()")), self.GeniusEmoticonFunction)
        QtCore.QObject.connect(self.AngryEmoticon, QtCore.SIGNAL(_fromUtf8("clicked()")), self.AngryEmoticonFunction)
        QtCore.QObject.connect(self.CryingEmoticon, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CriedEmoticonFunction)
        QtCore.QObject.connect(self.BleehEmoticon, QtCore.SIGNAL(_fromUtf8("clicked()")), self.BlehhEmoticonFunction)
        QtCore.QObject.connect(self.WinkEmoticon, QtCore.SIGNAL(_fromUtf8("clicked()")), self.WinkEmoticonFunction)
        QtCore.QObject.connect(self.AddtoContactBUTTON, QtCore.SIGNAL(_fromUtf8("clicked()")), self.AddNameAndNumbertoContactsFuntion)
        QtCore.QObject.connect(self.ShowFullContacts, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showFullContactsFunction)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Tekster | Freedom as in Free Open-Source ", None))
        ################ PROVIDERS LIST / MSHIELAMA ####################

        self.comboBox.setItemText(0, _translate("MainWindow", "Verizon PCS - 203", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Nextel - 214", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Alltel PCS - 36", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Cingular Wireless - 69", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "SunCom - 178", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "T-Mobile / Voicestream - 182", None))
        self.comboBox.setItemText(6, _translate("MainWindow", "Sprint PCS - 176", None))
        self.comboBox.setItemText(7, _translate("MainWindow", "AT&T PCS - 41", None))
        self.comboBox.setItemText(8, _translate("MainWindow", "MTS (Russia) - 1", None))
        self.comboBox.setItemText(9, _translate("MainWindow", "PGSM (Hungary) - 2", None))
        self.comboBox.setItemText(10, _translate("MainWindow", "Telecom Italia Mobile (Italy) - 3", None))
        self.comboBox.setItemText(11, _translate("MainWindow", "Vodafone Omnitel (Italy) - 4", None))
        self.comboBox.setItemText(12, _translate("MainWindow", "Max.Mobil (Austria) - 5", None))
        self.comboBox.setItemText(13, _translate("MainWindow", "Orange (United Kingdom) - 6", None))
        self.comboBox.setItemText(14, _translate("MainWindow", "Tele Danmark Mobil (Denmark) - 7", None))
        self.comboBox.setItemText(15, _translate("MainWindow", "Sonofon (Denmark) - 8", None))
        self.comboBox.setItemText(16, _translate("MainWindow", "Telia Mobitel (Sweden) - 9", None))
        self.comboBox.setItemText(17, _translate("MainWindow", "Comviq GSM (Sweden) - 10", None))
        self.comboBox.setItemText(18, _translate("MainWindow", "Europolitan (Sweden) - 11", None))
        self.comboBox.setItemText(19, _translate("MainWindow", "Telenor Mobil (Norway) - 12", None))
        self.comboBox.setItemText(20, _translate("MainWindow", "Netcom GSM (Norway) - 13", None))
        self.comboBox.setItemText(21, _translate("MainWindow", "Plus GSM (Poland)< - 14", None))
        self.comboBox.setItemText(22, _translate("MainWindow", "D1 De TeMobil (Germany) - 15", None))
        self.comboBox.setItemText(23, _translate("MainWindow", "D2 Mannesmann Mobilefunk (Germany) - 16", None))
        self.comboBox.setItemText(24, _translate("MainWindow", "E-Plus (Germany) - 17", None))
        self.comboBox.setItemText(25, _translate("MainWindow", "Celcom (Malaysia) - 18", None))
        self.comboBox.setItemText(26, _translate("MainWindow", "Mobitel (Tanzania) - 19", None))
        self.comboBox.setItemText(27, _translate("MainWindow", "Telecel (Portugal) - 20", None))
        self.comboBox.setItemText(28, _translate("MainWindow", "Optimus (Portugal) - 21", None))
        self.comboBox.setItemText(29, _translate("MainWindow", "TMN (Portugal) - 22", None))
        self.comboBox.setItemText(30, _translate("MainWindow", "LMT (Latvia) - 23", None))
        self.comboBox.setItemText(31, _translate("MainWindow", "UMC GSM (Ukraine) - 24", None))
        self.comboBox.setItemText(32, _translate("MainWindow", "Kyivstar GSM (Ukraine) - 25", None))
        self.comboBox.setItemText(33, _translate("MainWindow", "Si.Mobil (Slovenia) - 26", None))
        self.comboBox.setItemText(34, _translate("MainWindow", "Mobitel (Slovenia) - 27", None))
        self.comboBox.setItemText(35, _translate("MainWindow", "Eurotel (Czech Republic) - 28", None))
        self.comboBox.setItemText(36, _translate("MainWindow", "Cellis & LibanCell (Lebanon) - 29", None))
        self.comboBox.setItemText(37, _translate("MainWindow", "River Wireless - 30", None))
        self.comboBox.setItemText(38, _translate("MainWindow", "ACS Wireless - 31", None))
        self.comboBox.setItemText(39, _translate("MainWindow", "Advantage Communications - 32", None))
        self.comboBox.setItemText(40, _translate("MainWindow", "Airtouch Pagers - 33", None))
        self.comboBox.setItemText(41, _translate("MainWindow", "AlphaNow - 34", None))
        self.comboBox.setItemText(42, _translate("MainWindow", "Alltel - 35", None))
        self.comboBox.setItemText(43, _translate("MainWindow", "Alltel PCS - 36", None))
        self.comboBox.setItemText(44, _translate("MainWindow", "Ameritech Paging - 37", None))
        self.comboBox.setItemText(45, _translate("MainWindow", "Ameritech Clearpath - 38", None))
        self.comboBox.setItemText(46, _translate("MainWindow", "Andhra Pradesh Airtel - 39", None))
        self.comboBox.setItemText(47, _translate("MainWindow", "Arch Pagers (PageNet) - 40", None))
        self.comboBox.setItemText(48, _translate("MainWindow", "AT&T PCS - 41", None))
        self.comboBox.setItemText(49, _translate("MainWindow", "AT&T Pocketnet PCS - 42", None))
        self.comboBox.setItemText(50, _translate("MainWindow", "Beepwear - 43", None))
        self.comboBox.setItemText(51, _translate("MainWindow", "BeeLine GSM - 44", None))
        self.comboBox.setItemText(52, _translate("MainWindow", "Bell Atlantic - 45", None))
        self.comboBox.setItemText(53, _translate("MainWindow", "Bell Canada - 46", None))
        self.comboBox.setItemText(54, _translate("MainWindow", "Bell Mobility (Canada) - 47", None))
        self.comboBox.setItemText(55, _translate("MainWindow", "Bell Mobility - 48", None))
        self.comboBox.setItemText(56, _translate("MainWindow", "Bell South (Blackberry) - 49", None))
        self.comboBox.setItemText(57, _translate("MainWindow", "Bell South - 50", None))
        self.comboBox.setItemText(58, _translate("MainWindow", "Bell South Mobility - 51", None))
        self.comboBox.setItemText(59, _translate("MainWindow", "Blue Sky Frog< - 52", None))
        self.comboBox.setItemText(60, _translate("MainWindow", "Bluegrass Cellular - 53", None))
        self.comboBox.setItemText(61, _translate("MainWindow", "Boost - 54", None))
        self.comboBox.setItemText(62, _translate("MainWindow", "BPL mobile - 55", None))
        self.comboBox.setItemText(63, _translate("MainWindow", "Carolina Mobile Communications - 56", None))
        self.comboBox.setItemText(64, _translate("MainWindow", "Carolina West - 223", None))
        self.comboBox.setItemText(65, _translate("MainWindow", "Cellular One East Coast - 57", None))
        self.comboBox.setItemText(66, _translate("MainWindow", "Cellular One South West - 58", None))
        self.comboBox.setItemText(67, _translate("MainWindow", "Cellular One PCS - 59", None))
        self.comboBox.setItemText(68, _translate("MainWindow", "Cellular One - 60", None))
        self.comboBox.setItemText(69, _translate("MainWindow", "Cellular One West - 61", None))
        self.comboBox.setItemText(70, _translate("MainWindow", "Cellular South - 62", None))
        self.comboBox.setItemText(71, _translate("MainWindow", "Central Vermont Communications - 63", None))
        self.comboBox.setItemText(72, _translate("MainWindow", "CenturyTel - 64", None))
        self.comboBox.setItemText(73, _translate("MainWindow", "Chennai RPG Cellular - 65", None))
        self.comboBox.setItemText(74, _translate("MainWindow", "Chennai Skycell / Airtel - 66", None))
        self.comboBox.setItemText(75, _translate("MainWindow", "Cincinnati Bell - 67", None))
        self.comboBox.setItemText(76, _translate("MainWindow", "Cingular - 68", None))
        self.comboBox.setItemText(77, _translate("MainWindow", "Cingular Wireless - 69", None))
        self.comboBox.setItemText(78, _translate("MainWindow", "Clearnet - 70", None))
        self.comboBox.setItemText(79, _translate("MainWindow", "Comcast - 71", None))
        self.comboBox.setItemText(80, _translate("MainWindow", "Communication Specialists - 72", None))
        self.comboBox.setItemText(81, _translate("MainWindow", "Comviq - 73", None))
        self.comboBox.setItemText(82, _translate("MainWindow", "Cook Paging - 74", None))
        self.comboBox.setItemText(83, _translate("MainWindow", "Corr Wireless Communications - 75", None))
        self.comboBox.setItemText(84, _translate("MainWindow", "Cricket Wireless - 215", None))
        self.comboBox.setItemText(85, _translate("MainWindow", "Delhi Aritel - 76", None))
        self.comboBox.setItemText(86, _translate("MainWindow", "Digi-Page / Page Kansas - 77", None))
        self.comboBox.setItemText(87, _translate("MainWindow", "Dobson Cellular Systems - 78", None))
        self.comboBox.setItemText(88, _translate("MainWindow", "Dobson-Alex Wireless / Dobson-Cellular One - 89", None))
        self.comboBox.setItemText(89, _translate("MainWindow", "DT T-Mobile - 80", None))
        self.comboBox.setItemText(90, _translate("MainWindow", "Dutchtone / Orange-NL - 81", None))
        self.comboBox.setItemText(91, _translate("MainWindow", "Edge Wireless - 82", None))
        self.comboBox.setItemText(92, _translate("MainWindow", "EMT - 83", None))
        self.comboBox.setItemText(93, _translate("MainWindow", "Escotel - 84", None))
        self.comboBox.setItemText(94, _translate("MainWindow", "Fido - 85", None))
        self.comboBox.setItemText(95, _translate("MainWindow", "Galaxy Corporation - 86", None))
        self.comboBox.setItemText(96, _translate("MainWindow", "GCS Paging - 87", None))
        self.comboBox.setItemText(97, _translate("MainWindow", "Goa BPLMobil - 88", None))
        self.comboBox.setItemText(98, _translate("MainWindow", "Golden Telecom - 89", None))
        self.comboBox.setItemText(99, _translate("MainWindow", "GrayLink / Porta-Phone - 90", None))
        self.comboBox.setItemText(101, _translate("MainWindow", "GTE - 91", None))
        self.comboBox.setItemText(102, _translate("MainWindow", "Gujarat Celforce - 92", None))
        self.comboBox.setItemText(103, _translate("MainWindow", "Houston Cellular - 93", None))
        self.comboBox.setItemText(104, _translate("MainWindow", "Infopage Systems - 94", None))
        self.comboBox.setItemText(105, _translate("MainWindow", "Inland Cellular Telephone - 95", None))
        self.comboBox.setItemText(106, _translate("MainWindow", "JSM Tele-Page - 96", None))
        self.comboBox.setItemText(107, _translate("MainWindow", "Kerala Escotel - 97", None))
        self.comboBox.setItemText(108, _translate("MainWindow", "Kolkata Airtel - 98", None))
        self.comboBox.setItemText(109, _translate("MainWindow", "Kyivstar - 99", None))
        self.comboBox.setItemText(110, _translate("MainWindow", "Lauttamus Communication - 100", None))
        self.comboBox.setItemText(111, _translate("MainWindow", "LMT - 101", None))
        self.comboBox.setItemText(112, _translate("MainWindow", "Maharashtra BPL Mobile - 102", None))
        self.comboBox.setItemText(113, _translate("MainWindow", "Maharashtra Idea Cellular - 103", None))
        self.comboBox.setItemText(114, _translate("MainWindow", "Manitoba Telecom Systems - 104", None))
        self.comboBox.setItemText(115, _translate("MainWindow", "MCI Phone - 105", None))
        self.comboBox.setItemText(116, _translate("MainWindow", "MCI Page - 106", None))
        self.comboBox.setItemText(117, _translate("MainWindow", "Meteor - 107", None))
        self.comboBox.setItemText(118, _translate("MainWindow", "Metrocall - 108", None))
        self.comboBox.setItemText(119, _translate("MainWindow", "Metrocall 2-way - 109", None))
        self.comboBox.setItemText(120, _translate("MainWindow", "Metro PCS - 110", None))
        self.comboBox.setItemText(121, _translate("MainWindow", "Microcell - 111", None))
        self.comboBox.setItemText(122, _translate("MainWindow", "Midwest Wireless - 112", None))
        self.comboBox.setItemText(123, _translate("MainWindow", "MiWorld - 113", None))
        self.comboBox.setItemText(124, _translate("MainWindow", "Mobilecom PA - 114", None))
        self.comboBox.setItemText(125, _translate("MainWindow", "Mobilecomm - 115", None))
        self.comboBox.setItemText(126, _translate("MainWindow", "Mobileone - 116", None))
        self.comboBox.setItemText(127, _translate("MainWindow", "Mobilfone - 117", None))
        self.comboBox.setItemText(128, _translate("MainWindow", "Mobility Bermuda - 118", None))
        self.comboBox.setItemText(129, _translate("MainWindow", "Mobistar Belgium - 119", None))
        self.comboBox.setItemText(130, _translate("MainWindow", "Mobitel Tanzania - 120", None))
        self.comboBox.setItemText(131, _translate("MainWindow", "Mobtel Srbija - 121", None))
        self.comboBox.setItemText(132, _translate("MainWindow", "Morris Wireless - 122", None))
        self.comboBox.setItemText(133, _translate("MainWindow", "Motient - 123", None))
        self.comboBox.setItemText(134, _translate("MainWindow", "Movistar - 124", None))
        self.comboBox.setItemText(135, _translate("MainWindow", "Mumbai BPL Mobile - 125", None))
        self.comboBox.setItemText(136, _translate("MainWindow", "Mumbai Orange - 126", None))
        self.comboBox.setItemText(137, _translate("MainWindow", "NBTel - 127", None))
        self.comboBox.setItemText(138, _translate("MainWindow", "Netcom - 128", None))
        self.comboBox.setItemText(139, _translate("MainWindow", "NPI Wireless - 129", None))
        self.comboBox.setItemText(140, _translate("MainWindow", "Ntelos - 130", None))
        self.comboBox.setItemText(141, _translate("MainWindow", "O2 - 131", None))
        self.comboBox.setItemText(142, _translate("MainWindow", "O2 (M-mail) - 132", None))
        self.comboBox.setItemText(143, _translate("MainWindow", "Omnipoint - 133", None))
        self.comboBox.setItemText(144, _translate("MainWindow", "One Connect Austria - 134", None))
        self.comboBox.setItemText(145, _translate("MainWindow", "OnlineBeep - 135", None))
        self.comboBox.setItemText(146, _translate("MainWindow", "Optus Mobile - 136", None))
        self.comboBox.setItemText(147, _translate("MainWindow", "Orange - 137", None))
        self.comboBox.setItemText(148, _translate("MainWindow", "Orange Mumbai - 138", None))
        self.comboBox.setItemText(149, _translate("MainWindow", "Orange - NL / Dutchtone - 139", None))
        self.comboBox.setItemText(150, _translate("MainWindow", "Oskar - 140", None))
        self.comboBox.setItemText(151, _translate("MainWindow", "P&T Luxembourg - 141", None))
        self.comboBox.setItemText(152, _translate("MainWindow", "Pacific Bell - 142", None))
        self.comboBox.setItemText(153, _translate("MainWindow", "PageMart - 143", None))
        self.comboBox.setItemText(154, _translate("MainWindow", "PageMart Advanced /2way - 144", None))
        self.comboBox.setItemText(155, _translate("MainWindow", "PageMart Canada - 145", None))
        self.comboBox.setItemText(156, _translate("MainWindow", "PageNet Canada< - 146", None))
        self.comboBox.setItemText(157, _translate("MainWindow", "PageOne NorthWest - 147", None))
        self.comboBox.setItemText(158, _translate("MainWindow", "PCS One - 148", None))
        self.comboBox.setItemText(159, _translate("MainWindow", "Personal Communication - 149", None))
        self.comboBox.setItemText(160, _translate("MainWindow", "Pioneer / Enid Cellular - 150", None))
        self.comboBox.setItemText(161, _translate("MainWindow", "PlusGSM - 151", None))
        self.comboBox.setItemText(162, _translate("MainWindow", "Pondicherry BPL Mobile - 152", None))
        self.comboBox.setItemText(163, _translate("MainWindow", "Powertel - 153", None))
        self.comboBox.setItemText(164, _translate("MainWindow", "Price Communications - 154", None))
        self.comboBox.setItemText(165, _translate("MainWindow", "Primco - 155", None))
        self.comboBox.setItemText(166, _translate("MainWindow", "Primtel - 156", None))
        self.comboBox.setItemText(167, _translate("MainWindow", "ProPage - 157", None))
        self.comboBox.setItemText(168, _translate("MainWindow", "Public Service Cellular - 158", None))
        self.comboBox.setItemText(169, _translate("MainWindow", "Qualcomm - 159", None))
        self.comboBox.setItemText(170, _translate("MainWindow", "Qwest - 160", None))
        self.comboBox.setItemText(171, _translate("MainWindow", "RAM Page - 161", None))
        self.comboBox.setItemText(172, _translate("MainWindow", "Rogers AT&T Wireless - 162", None))
        self.comboBox.setItemText(173, _translate("MainWindow", "Rogers Canada - 163", None))
        self.comboBox.setItemText(174, _translate("MainWindow", "Safaricom - 164", None))
        self.comboBox.setItemText(175, _translate("MainWindow", "Satelindo GSM - 165", None))
        self.comboBox.setItemText(176, _translate("MainWindow", "Satellink - 166", None))
        self.comboBox.setItemText(177, _translate("MainWindow", "SBC Ameritech Paging - 167", None))
        self.comboBox.setItemText(178, _translate("MainWindow", "SCS-900 - 168", None))
        self.comboBox.setItemText(179, _translate("MainWindow", "SFR France - 169", None))
        self.comboBox.setItemText(180, _translate("MainWindow", "Skytel Pagers - 170", None))
        self.comboBox.setItemText(181, _translate("MainWindow", "Simple Freedom - 171", None))
        self.comboBox.setItemText(182, _translate("MainWindow", "Smart Telecom - 172", None))
        self.comboBox.setItemText(183, _translate("MainWindow", "Southern LINC - 173", None))
        self.comboBox.setItemText(184, _translate("MainWindow", "Southwestern Bell - 174", None))
        self.comboBox.setItemText(185, _translate("MainWindow", "Sprint - 175", None))
        self.comboBox.setItemText(186, _translate("MainWindow", "Sprint PCS - 176", None))
        self.comboBox.setItemText(187, _translate("MainWindow", "ST Paging - 177", None))
        self.comboBox.setItemText(188, _translate("MainWindow", "SunCom - 178", None))
        self.comboBox.setItemText(189, _translate("MainWindow", "Sunrise Mobile - 179", None))
        self.comboBox.setItemText(190, _translate("MainWindow", "Surewest Communicaitons - 180", None))
        self.comboBox.setItemText(191, _translate("MainWindow", "Swisscom - 181", None))
        self.comboBox.setItemText(192, _translate("MainWindow", "T-Mobile / Voicestream - 182", None))
        self.comboBox.setItemText(193, _translate("MainWindow", "T-Mobile Austria - 183", None))
        self.comboBox.setItemText(194, _translate("MainWindow", "T-Mobile Germany - 184", None))
        self.comboBox.setItemText(195, _translate("MainWindow", "T-Mobile UK - 185", None))
        self.comboBox.setItemText(196, _translate("MainWindow", "Tamil Nadu BPL Mobile - 186", None))
        self.comboBox.setItemText(197, _translate("MainWindow", "Tele2 Latvia - 187", None))
        self.comboBox.setItemText(198, _translate("MainWindow", "Telefonica Movistar - 188", None))
        self.comboBox.setItemText(199, _translate("MainWindow", "Telenor - 189", None))
        self.comboBox.setItemText(200, _translate("MainWindow", "Teletouch - 190", None))
        self.comboBox.setItemText(201, _translate("MainWindow", "Telia Denmark - 191", None))
        self.comboBox.setItemText(202, _translate("MainWindow", "Telus - 192", None))
        self.comboBox.setItemText(203, _translate("MainWindow", "TIM - 193", None))
        self.comboBox.setItemText(204, _translate("MainWindow", "Triton - 194", None))
        self.comboBox.setItemText(205, _translate("MainWindow", "TSR Wireless - 195", None))
        self.comboBox.setItemText(206, _translate("MainWindow", "UMC - 196", None))
        self.comboBox.setItemText(207, _translate("MainWindow", "Unicel - 197", None))
        self.comboBox.setItemText(208, _translate("MainWindow", "Uraltel - 198", None))
        self.comboBox.setItemText(209, _translate("MainWindow", "US Cellular - 199", None))
        self.comboBox.setItemText(210, _translate("MainWindow", "US West - 200", None))
        self.comboBox.setItemText(211, _translate("MainWindow", "Uttar Pradesh Escotel - 201", None))
        self.comboBox.setItemText(212, _translate("MainWindow", "Verizon Pagers - 202", None))
        self.comboBox.setItemText(213, _translate("MainWindow", "Verizon PCS - 203", None))
        self.comboBox.setItemText(214, _translate("MainWindow", "Vessotel - 204", None))
        self.comboBox.setItemText(215, _translate("MainWindow", "Virgin Mobile - 205", None))
        self.comboBox.setItemText(216, _translate("MainWindow", "Vodafone Italy - 206", None))
        self.comboBox.setItemText(217, _translate("MainWindow", "Vodafone Japan - 207", None))
        self.comboBox.setItemText(218, _translate("MainWindow", "Vodafone Spain - 208", None))
        self.comboBox.setItemText(219, _translate("MainWindow", "Vodafone UK - 209", None))
        self.comboBox.setItemText(220, _translate("MainWindow", "WebLink Wireless - 210", None))
        self.comboBox.setItemText(221, _translate("MainWindow", "West Central Wireless - 211", None))
        self.comboBox.setItemText(222, _translate("MainWindow", "Western Wireless - 212", None))
        self.comboBox.setItemText(223, _translate("MainWindow", "Wyndtell - 213", None))
        self.comboBox.setItemText(224, _translate("MainWindow", "Nextel - 214", None))
        self.comboBox.setItemText(-0, _translate("MainWindow", "                Select a Network", None))


        self.UsernamePlainTextEditBox.setPlaceholderText(_translate("MainWindow", "Email as Text Message Sender!", None))
        self.label.setText(_translate("MainWindow", "Email", None))
        self.TeksterClose.setText(_translate("MainWindow", "X", None))
        PassVar = 'None'
        self.label_2.setText(_translate("MainWindow", PassVar, None))
        self.pushButton_2.setText(_translate("MainWindow", "Send", None))
        self.OpenSaveUserButton.setText(_translate("MainWindow", "Open", None))
        self.ActivateBoxesButton.setText(_translate("MainWindow", "Email Mode", None))
        self.SaveCurrentUserButton.setText(_translate("MainWindow", "Save", None))
        self.label_7.setText(_translate("MainWindow", "Send to", None))
        self.label_6.setText(_translate("MainWindow", "OR", None))
        self.MoreInfoButton.setText(_translate("MainWindow", "More Information", None))
        self.AddtoContactsButton.setText(_translate("MainWindow", "Add to Contacts", None))
        self.label_8.setText(_translate("MainWindow", "Connection:                     Online", None))
        self.label_9.setText(_translate("MainWindow", "Version:                            4.0", None))
        self.label_10.setText(_translate("MainWindow", "Latest Version:", None))
        self.LatestVersionLabel.setText(_translate("MainWindow", "4.0", None))
        self.label_12.setText(_translate("MainWindow", "Email Server:", None))
        self.EmailServerLabel.setText(_translate("MainWindow", "None", None))
        self.label_14.setText(_translate("MainWindow", "Error:", None))
        self.ErrorBoxShow.setPlainText(_translate("MainWindow", "None", None))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Please Visit: <span style=\" font-style:italic;\">http://www.tekster.sf.net/ </span></p><p align=\"center\">for more information</p></body></html>", None))
        self.CheckForUpdate.setText(_translate("MainWindow", "Check for Updates", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.StatusTab), _translate("MainWindow", "Status", None))
        self.toolBox.setItemToolTip(self.toolBox.indexOf(self.StatusTab), _translate("MainWindow", "<html><head/><body><p><span style=\" color:#00aaff;\">Tekster Status</span></p></body></html>", None))
        self.label_16.setText(_translate("MainWindow", "Add Contact", None))
        self.label_17.setText(_translate("MainWindow", "Name", None))
        self.label_18.setText(_translate("MainWindow", "Number", None))
        self.label_19.setText(_translate("MainWindow", "Contacts", None))
        self.AddtoContactBUTTON.setText(_translate("MainWindow", "Add", None))
        self.ShowFullContacts.setText(_translate("MainWindow", "Show Contacts", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.ContactsTab), _translate("MainWindow", "Contacts", None))
        self.toolBox.setItemToolTip(self.toolBox.indexOf(self.ContactsTab), _translate("MainWindow", "<html><head/><body><p>Add or Check your Contacts</p></body></html>", None))
        self.label_20.setText(_translate("MainWindow", "Custom SMS Gateway", None))
        self.label_21.setText(_translate("MainWindow", "Other Gateways List", None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"

"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">3 River Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@sms.3rivers.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">ACS Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@paging.acswireless.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Alltel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@message.alltel.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">AT&amp;T</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@txt.att.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Bell Canada</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@txt.bellmobility.ca</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Bell Canada</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@bellmobility.ca</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Bell Mobility (Canada)</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@txt.bell.ca</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Bell Mobility</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@txt.bellmobility.ca</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Blue Sky Frog</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@blueskyfrog.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Bluegrass Cellular</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@sms.bluecell.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Boost Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@myboostmobile.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">BPL Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@bplmobile.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Carolina West Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digit10digitnumber@cwwsms.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Cellular One</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@mobile.celloneusa.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Cellular South</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@csouth1.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Centennial Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@cwemail.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">CenturyTel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@messaging.centurytel.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Cingular (Now AT&amp;T)</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@txt.att.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Clearnet</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@msg.clearnet.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Comcast</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@comcastpcs.textmsg.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Corr Wireless Communications</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@corrwireless.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Dobson</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@mobile.dobson.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Edge Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@sms.edgewireless.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Fido</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@fido.ca</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Golden Telecom</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@sms.goldentele.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Helio</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@messaging.sprintpcs.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Houston Cellular</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@text.houstoncellular.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Idea Cellular</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@ideacellular.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Illinois Valley Cellular</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@ivctext.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Inland Cellular Telephone</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@inlandlink.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">MCI</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@pagemci.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Metrocall</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@page.metrocall.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Metrocall 2-way</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@my2way.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Metro PCS</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@mymetropcs.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Microcell</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@fido.ca</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Midwest Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@clearlydigital.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Mobilcomm</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@mobilecomm.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">MTS</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@text.mtsmobility.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Nextel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@messaging.nextel.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">OnlineBeep</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@onlinebeep.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">PCS One</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@pcsone.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">President\'s Choice</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@txt.bell.ca</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Public Service Cellular</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@sms.pscel.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Qwest</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@qwestmp.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Rogers AT&amp;T Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@pcs.rogers.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Rogers Canada</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@pcs.rogers.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Satellink</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber.pageme@satellink.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Southwestern Bell</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@email.swbw.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Sprint</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@messaging.sprintpcs.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Sumcom</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@tms.suncom.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Surewest Communicaitons</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@mobile.surewest.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">T-Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@tmomail.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Telus</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@msg.telus.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Tracfone</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@txt.att.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Triton</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@tms.suncom.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Unicel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@utext.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">US Cellular</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@email.uscc.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Solo Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@txt.bell.ca</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Sprint</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@messaging.sprintpcs.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Sumcom</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@tms.suncom.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Surewest Communicaitons</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@mobile.surewest.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">T-Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@tmomail.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Telus</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@msg.telus.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Triton</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@tms.suncom.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Unicel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@utext.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">US Cellular</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@email.uscc.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">US West</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@uswestdatamail.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Verizon</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@vtext.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Virgin Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@vmobl.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Virgin Mobile Canada</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@vmobile.ca</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">West Central Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@sms.wcc.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Western Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@cellularonewest.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#cc0000; background-color:#ffffff;\">International Carriers</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Chennai RPG Cellular</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@rpgmail.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Chennai Skycell / Airtel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@airtelchennai.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Comviq</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">number@sms.comviq.se</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Delhi Aritel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@airtelmail.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Delhi Hutch</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@delhi.hutch.co.in</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">DT T-Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@t-mobile-sms.de</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Dutchtone / Orange-NL</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@sms.orange.nl</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">EMT</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@sms.emt.ee</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Escotel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@escotelmobile.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">German T-Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">number@t-mobile-sms.de</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Goa BPLMobil</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@bplmobile.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Golden Telecom</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@sms.goldentele.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Gujarat Celforce</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@celforce.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">JSM Tele-Page</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">pinnumber@jsmtel.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Kerala Escotel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@escotelmobile.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Kolkata Airtel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@airtelkol.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Kyivstar</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">number@smsmail.lmt.lv</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Lauttamus Communication</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">pagernumber@e-page.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">LMT</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@smsmail.lmt.lv</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Maharashtra BPL Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@bplmobile.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Maharashtra Idea Cellular</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@ideacellular.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Manitoba Telecom Systems</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@text.mtsmobility.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Meteor</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@mymeteor.ie</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">MiWorld</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@m1.com.sg</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Mobileone</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@m1.com.sg</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Mobilfone</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@page.mobilfone.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Mobility Bermuda</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@ml.bm</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Mobistar Belgium</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@mobistar.be</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Mobitel Tanzania</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@sms.co.tz</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Mobtel Srbija</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@mobtel.co.yu</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Movistar</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">number@correo.movistar.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Mumbai BPL Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@bplmobile.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Netcom</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@sms.netcom.no</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Ntelos</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">number@pcs.ntelos.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">O2</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">name@o2.co.uk</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">O2</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">number@o2imail.co.uk</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">O2 (M-mail)</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">number@mmail.co.uk</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">One Connect Austria</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@onemail.at</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">OnlineBeep</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@onlinebeep.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Optus Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@optusmobile.com.au</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Orange</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@orange.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Orange Mumbai</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@orangemail.co.in</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Orange NL / Dutchtone</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@sms.orange.nl</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Oskar</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@mujoskar.cz</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">P&amp;T Luxembourg</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@sms.luxgsm.lu</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Personal Communication</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">sms@pcom.ru (put the number in the subject line)</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Pondicherry BPL Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@bplmobile.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Primtel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@sms.primtel.ru</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Safaricom</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@safaricomsms.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Satelindo GSM</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@satelindogsm.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">SCS-900</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@scs-900.ru</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">SFR France</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@sfr.fr</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Simple Freedom</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@text.simplefreedom.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Smart Telecom</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@mysmart.mymobile.ph</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Southern LINC</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@page.southernlinc.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Sunrise Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@mysunrise.ch</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Sunrise Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@swmsg.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Surewest Communications</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@freesurf.ch</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Swisscom</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@bluewin.ch</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">T-Mobile Austria</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@sms.t-mobile.at</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">T-Mobile Germany</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@t-d1-sms.de</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">T-Mobile UK</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@t-mobile.uk.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Tamil Nadu BPL Mobile</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@bplmobile.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Tele2 Latvia</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@sms.tele2.lv</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Telefonica Movistar</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@movistar.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Telenor</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@mobilpost.no</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Teletouch</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@pageme.teletouch.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Telia Denmark</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@gsm1800.telia.dk</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">TIM</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@timnet.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">TSR Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">pagernumber@alphame.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">UMC</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@sms.umc.com.ua</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Uraltel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@sms.uraltel.ru</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Uttar Pradesh Escotel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@escotelmobile.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Vessotel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@pager.irkutsk.ru</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Vodafone Italy</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">number@sms.vodafone.it</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Vodafone Japan</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@c.vodafone.ne.jp</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Vodafone Japan</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@h.vodafone.ne.jp</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Vodafone Japan</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@t.vodafone.ne.jp</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Vodafone UK</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">phonenumber@vodafone.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Wyndtell</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">number@wyndtell.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#cc0000; background-color:#ffffff;\">Old US &amp; Canadian Carriers (Most Not In Use)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Advantage Communications</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@advantagepaging.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Airtouch Pagers</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@myairmail.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">AlphaNow</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">pin@alphanow.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Ameritech Paging</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@paging.acswireless.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">American Messaging</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@page.americanmessaging.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Ameritech Clearpath</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@clearpath.acswireless.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Arch Pagers (PageNet)</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@archwireless.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">AT&amp;T</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@mobile.att.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">AT&amp;T Free2Go</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@mmode.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">AT&amp;T PCS</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@mobile.att.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">AT&amp;T Pocketnet PCS</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@dpcs.mobile.att.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Beepwear</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@beepwear.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Bell Atlantic</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@message.bam.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Bell South</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@wireless.bellsouth.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Bell South (Blackberry)</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@bellsouthtips.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Bell South Mobility</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@blsdcs.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Cellular One (East Coast)</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@phone.cellone.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Cellular One (South West)</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@swmsg.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Cellular One</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@cellularone.txtmsg.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Cellular One</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@cellularone.textmsg.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Cellular One</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@cell1.textmsg.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Cellular One</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@sbcemail.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Cellular One (West)</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@mycellone.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Central Vermont Communications</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@cvcpaging.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Cingular</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@cingularme.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Communication Specialists</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">7digitpin@pageme.comspeco.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Cook Paging</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@cookmail.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Corr Wireless Communications</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@corrwireless.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Digi-Page / Page Kansas</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@page.hit.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Galaxy Corporation</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber.epage@sendabeep.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">GCS Paging</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@webpager.us</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">GrayLink / Porta-Phone</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@epage.porta-phone.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">GTE</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@airmessage.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">GTE</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@gte.pagegate.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">GTE</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@messagealert.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Infopage Systems</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">pinnumber@page.infopagesystems.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Indiana Paging Co</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@inlandlink.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">MCI</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@pagemci.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Metrocall</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@page.metrocall.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Mobilecom PA</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@page.mobilcom.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Morris Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@beepone.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Motient</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@isp.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Nextel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@page.nextel.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Omnipoint</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@omnipointpcs.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Pacific Bell</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@pacbellpcs.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">PageMart</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">7digitpinnumber@pagemart.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">PageMart Canada</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@pmcl.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">PageNet Canada</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@pagegate.pagenet.ca</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">PageOne Northwest</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@page1nw.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">PCS One</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@pcsone.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Powertel</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@voicestream.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Price Communications</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@mobilecell1se.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Primeco</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@email.uscc.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">ProPage</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">7digitpagernumber@page.propage.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Qualcomm</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">name@pager.qualcomm.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">RAM Page</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">number@ram-page.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">SBC Ameritech Paging</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@paging.acswireless.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Skytel Pagers</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@email.skytel.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">ST Paging</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">pin@page.stpaging.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Verizon Pagers</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitpagernumber@myairmail.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">Verizon PCS</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@myvzw.com</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">VoiceStream</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@voicestream.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">WebLink Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@@airmessage.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">WebLink Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@pagemart.net</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#333333; background-color:#ffffff;\">West Central Wireless</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Trebuchet MS,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:29px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">10digitphonenumber@sms.wcc.net</span></li></ul></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.SettingsTab), _translate("MainWindow", "Settings", None))
        self.toolBox.setItemToolTip(self.toolBox.indexOf(self.SettingsTab), _translate("MainWindow", "Tekster Settings", None))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt; color:#888888;\">CoreSEC Software Development | Geek Talks | Sourceforge</span></p></body></html>", None))
        self.DecimalLabel.setText(_translate("MainWindow", "-", None))
        self.pushButton_3.setText(_translate("MainWindow", ">>", None))
        self.pushButton_4.setText(_translate("MainWindow", "Sent Messages", None))
        self.pushButton_5.setText(_translate("MainWindow", "Contact Us", None))
        self.label_24.setText(_translate("MainWindow", "SMS", None))
        self.label_25.setText(_translate("MainWindow", "Email", None))
        usernameD = self.UsernamePlainTextEditBox
        passwordD = self.PasswordPlainTextEditBox
        passwordD.setDisabled(1)  #Disabled PBox




    def teksterMinimizeFunction(self):
        MainWindow.showMinimized()


    def teksterCloseFunction(self):
        MainWindow.close()

    def MoreInformationFunction(self):
        teksterBox = self.MessageBox

        teksterBox.clear(), teksterBox.appendHtml("<b>TEKSTER</b> Email as SMS Sender Are Important and you could also set it to  tekster@hacore.sf.net (other than leaving it blank), Enable to Send EMAIL, Tekster needs your Username/Password Credentials as Tekster Uses SMTP (Send Mail Transfer Protocol)<br/>"
                                                  "Which is the best and easiest function for us to process your Message Directly through the<br/>"
                                                  "Live,Gmail,Outlook,Hotmail SMTP Servers (you prefer)<br/>"
                                                  "<br/>"
                                                  "We Store all of the Encrypted characters directly to your Storage disk, Also the History or Sent Messages,<br/>"
                                                  "We Do not Store or have an access to any of the Sensitive informations which is/was stored on your"
                                                  "<br/>Tekster Software Folder."
                                                    "Sent Messages will be store on your Email Provider under as well as SMS/EMAIL Function, \"Sent Messages\" of the mentioned Email Server."
                                                    "<br/><br/><br/>For more informations please consult at: <a>http://hacore.sourceforge.net/forum/viewtopic.php?id=6<a/><br/>"
                                                    "This Software is Licensed under the General Public Licence v2, and Software Provided by: CoreSEC Software Development Group"
                                                    "<br/><br/>Developers: http://www.tekster.sf.net/developers.html<br/>"
                                                    )


    def CheckForUpdatesFunction(self):
        """ CHECK FOR UPDATES FUNCTION """
        import urllib
        teksterCount = self.CharactersCountfromMessageBox
        teksterCount.setValue(0)
        teksterBox = self.MessageBox
        Labelversion = self.LatestVersionLabel
        teksterBox.clear(), teksterBox.appendHtml("<html><span style=\"color:#ffd700;\">Checking for Updates....<br/>Please Wait...</span></html>")
        teksterLVersion = urllib.urlopen('http://tekster.sourceforge.net/latestversion.txt')
        Read = teksterLVersion.read()
        if Read != '4.0':   ### NEED TO UPDATE
            teksterBox.clear(), teksterBox.appendPlainText('Your Tekster Software is Out of Date, New Version is '+ str(Read)
                                                                  +'\n\nPlease Download the New Version at \nhttp://sourceforge.net/projects/tekster/')
            teksterLabel = Labelversion
            vfileOpen = open('teksterFiles/Version', 'w+')
            vfileRead = vfileOpen.read()
            vfileWrite = vfileOpen.write(Read)
            vfileOpen.close()
        elif Read == '4.0':  ### UPDATED
            teksterBox.clear(), teksterBox.appendHtml("<html><span style=\"color:#ffd700;\">You are already have the Latest Tekster version! 4.0</span></html>")
            teksterLabel = Labelversion
            vfileOpen = open('teksterFiles/Version', 'w+')
            vfileRead = vfileOpen.read()
            vfileWrite = vfileOpen.write(Read)
            vfileOpen.close()
        else:
            return True
        # End of Check Function





    def ActivateBoxesButtonFunction(self):
        uBox = self.UsernamePlainTextEditBox
        pBox = self.PasswordPlainTextEditBox
        pBoxLabel = self.label_2
        pBoxLabelU = self.label
        Slider = self.horizontalSlider
        Slider.setValue(1)
        uBox.setEnabled(1)
        pBox.setEnabled(1)
        pBoxLabel.setText('Password')
        pBoxLabelU.setText('Username')
        uBox.setPlaceholderText('You Email (Gmail, Live, Hotmail or Outlook!)')








    def SaveCredentialsFunction(self):
        teksfileU = open('teksterFiles/SavedCredentialsUsername', 'w+')
        teksfileP = open('teksterFiles/SavedCredentialsPassword', 'w+')
        username = self.UsernamePlainTextEditBox.text()
        password = self.PasswordPlainTextEditBox
        Strusername = str(username)
        Strpassword = password.toPlainText()

        teksfileU.write(str(Strusername))
        teksfileP.write(str(Strpassword))
        box = self.MessageBox
        box.clear(), box.insertPlainText('Saved...')


    def OpenSaveCredentialsFunction(self):
        teksfileU = open('teksterFiles/SavedCredentialsUsername', 'r+')
        teksfileP = open('teksterFiles/SavedCredentialsPassword', 'r+')
        username = self.UsernamePlainTextEditBox
        password = self.PasswordPlainTextEditBox
        box = self.MessageBox
        boxLenght = self.MessageBox.toPlainText()
        username.clear()
        password.clear()


        ReadU = teksfileU.read()
        ReadP = teksfileP.read()

        username.insert(str(ReadU))
        password.insertPlainText(str(ReadP))
        box.clear(), box.insertPlainText('Saved File Username and Password Opened!\n Username: '+str(ReadU)+'\n Password: (Encrypted)')



    def AddToContactsFunction(self):
        number = self.NumberBox.toPlainText()
        Strnumber = str(number)
        Box = self.MessageBox
        Rbox = Box.toPlainText()
        ContactOpens = open('teksterFiles/Contacts', 'r+')
        ContactReads = ContactOpens.read()

        if len(str(number)) <= 4:
            Box.clear(), Box.appendHtml('Please Make sure your number is greater than four characters! ')
            return False
        if str(number) in ContactReads:
            Box.clear(), Box.appendHtml('<b>Ooops! Number/Email Already Exists!<br/>name: '+str(number)+ '</b>')
            return False
        if str(number) not in ContactReads:

            ContactOpen = open('teksterFiles/Contacts', 'a')
            ContactWrite = ContactOpen.write('Name: <b> No Name</b><br/>Number: <b>' + str(Strnumber) + "</b><br/><br/>")
            ContactOpen.close()
            Box.clear()
            Box.appendHtml('Added to your Contact\'s List!')
            ContactOpen.close()
            return False
        else:
            Box.appendPlainText('Number Already Exists! Check your Contacts List!')

    def ContactUsFunction(self):
        Box = self.MessageBox
        Box.clear(), Box.appendHtml("""<b>For Questions related with this software please

                                    <br/>Navigate and Discuss about it at:  http://www.hacore.sf.net/forum/  <br/>(On Tekster Section)

                                   <br/><br/>and for offers,request or donation, Please send an email to  onecore@me.com  or onecore@live.com</b>""")

    def SentMessagesFunction(self):
        Box = self.MessageBox
        sentMessagesFile = open('teksterFiles/TeksterSentMessages','r+')
        readSents = sentMessagesFile.read()
        Box.insertPlainText(readSents)

############     Smilies    ############
    def ShowFullSmileysListFunction(self):
        teksterBox = self.MessageBox
        teksterBox.clear()
        teksterBox = self.MessageBox

        teksterBox.appendHtml("This Smileys should be right this characters, as some Phones could't read the graphics properly.<br/>"
        "<br/>"
        "<b>:)</b> - Smile<br/>"
        "<b>:D</b> - Laugh<br/>"
        "<b>:\")</b> - Blush<br/>"
        "<b>8)</b> - Genius<br/>"
        "<b>^_^</b> - Nice<br/>"
        "<b>:@</b> - Mad<br/>"
        "<b>-_-\"</b> - Confused<br/>"
        "<b>:(</b> - Sad<br/>"
        "<b>;)</b> - Wink<br/>"
        "<b>:P</b> - Blehh<br/>"
        "<b>T_T</b> - Crying<br/>"
        "<b>o_O</b> - Unconvinced</b><br/><br/>"
        "For More informations related with Emoticons<br/>"
        "Please visit: http://hacore.sourceforge.net/forum/viewtopic.php?id=6")




    def UpupEmoticonFunction(self):
        teksterBox = self.MessageBox
        teksterBox.insertPlainText('^_^')

    def LaughEmoticonFunction(self):
        teksterBox = self.MessageBox
        teksterBox.insertPlainText(':D')

    def HeartEyesEmoticonFunction(self):
        teksterBox = self.MessageBox
        teksterBox.insertPlainText('<3_<3')

    def ConfusedEmoticonFunction(self):
        teksterBox = self.MessageBox
        teksterBox.insertPlainText('-_-\"')


    def MadEmoticonFunction(self):
        teksterBox = self.MessageBox
        teksterBox.sinsertPlainText('-_-')

    def TwirlEmoticonFunction(self):
        teksterBox = self.MessageBox
        teksterBox.insertPlainText('~_~')

    def GeniusEmoticonFunction(self):
        teksterBox = self.MessageBox
        teksterBox.insertPlainText('0-0')

    def AngryEmoticonFunction(self):
        teksterBox = self.MessageBox
        teksterBox.insertPlainText('@_@')

    def CriedEmoticonFunction(self):
        teksterBox = self.MessageBox
        teksterBox.insertPlainText('T_T')

    def BlehhEmoticonFunction(self):
        teksterBox = self.MessageBox
        teksterBox.insertPlainText(':P')

    def WinkEmoticonFunction(self):
        teksterBox = self.MessageBox
        teksterBox.insertPlainText('^_-')






    def AddNameAndNumbertoContactsFuntion(self):
        """ CONTACTS FUNCTIONS"""
        import Contacts as Con
        Name = self.AddtoContactNameBOX
        Number = self.AddtoContactNumberBOX
        FinalName = Name.toPlainText()
        FinalNumber = Number.toPlainText()
        Box = self.MessageBox
        Finds = open('teksterFiles/Contacts', 'r+')
        FindRead = Finds.read()

        if len(FinalName) <= 3:
            Box.clear(), Box.appendHtml('<b>Ooops! Insufficient Name Characters!</b>')
            return False
        if len(FinalNumber) <= 3:
            Box.clear(), Box.appendHtml('<b>Ooops! Insufficient Number Characters!</b>')
            return False
        if str(FinalName) in FindRead:
            Box.clear(), Box.appendHtml('<b>Ooops! Name Already Exists!<br/>name: '+str(FinalName)+ '</b>')
            return False


        ContactOpen = open('Contacts', 'a')
        ContactWrite = ContactOpen.write('Name: <b>'+str(FinalName)+'</b><br/>Number: <b>' + str(FinalNumber) + "</b><br/><br/>")
        ContactOpen.close()


        #show on Lists



    def showFullContactsFunction(self):
        ShowOnLists = self.ContactsListBOX
        StrBox = str(ShowOnLists)
        FileOpen = open('teksterFiles/Contacts', 'r+')
        FileOpenRead = FileOpen.read()
        return ShowOnLists.clear(), ShowOnLists.appendHtml(FileOpenRead)


        FileOpen.close()

        #show on Lists


    def teksterSendFunction(self):
        import urllib
        import urllib2
        import smtplib
        import time





        Username = self.UsernamePlainTextEditBox.text()
        Password = self.PasswordPlainTextEditBox.toPlainText()
        Message = self.MessageBox.toPlainText()
        Number = self.NumberBox.toPlainText()
        StringUsername = str(Username)
        StringPassword = str(Password)
        StringMessage = str(Message)
        StringNumber = str(Number)

        SetEmailLabel = self.EmailServerLabel

        gateway = self.ChangeSMSGateWayBox
        getgateway = gateway.toPlainText()
        errorbox = self.ErrorBoxShow
        box = self.MessageBox

        ########### CHECK EVERYTHING BEFORE WE GO ON ################



        ########## IF PASSED MESSAGE WILL START TO PROCESS ON THEIR PROVIDERS ##############

        ######### Open Check Provider ##########
        lookUrl = 'http://www.txt2day.com/lookup.php'

        RequestsString = {'action' : 'lookup',
                           'pre' : Number[0:3],
                           'ex' : Number[3:6],
                           'myButton' : 'Find Provider'}
        ProvCheck = urllib.urlencode(RequestsString)  ##provider checker
        req2 = urllib2.Request(lookUrl, ProvCheck)
        Lookupresponse = urllib2.urlopen(req2)
        Tekster = Lookupresponse.read()
        Chosen = None
        UsernameString = str(Username)



        ###############EMAIL FUNCTION / NOT SMS :)
        slider = self.horizontalSlider
        vslider = slider.value()
        cU = self.UsernamePlainTextEditBox
        cP = self.UsernamePlainTextEditBox
        def Enabled(U,P):
            U.setEnabled(1)
            P.setEnabled(1)
            P.text()
        Enabled(cU,cP)
        SentMessagesFile = open('teksterFiles/TeksterSentMessages','a')
        if vslider == 1:
            #Numbers = str(Number) + str(TeksterCanada.canada4)
            header = 'To: ' + StringNumber +'\n' + 'From: ' + StringUsername + '\n' + 'Subject: Sent Using Tekster \n' + StringMessage

            if StringUsername[-10:] == '@gmail.com': ##GMAIL
                try:
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(StringUsername,StringPassword)
                    server.sendmail(StringUsername, StringNumber, header)
                    box.appendHtml('<span style="font-family:arial,helvetica,sans-serif; color:#33cc66;">Message Sent!</span>')
                    server.quit()

                    SentMessagesFile.write('To: '+ StringNumber + '\nMessage: ' + StringMessage + ' on ' + time.ctime() +'\n\n')
                    SentMessagesFile.close()

                    return False
                except:
                    box.appendHtml('<span style="font-family:arial,helvetica,sans-serif; color:#ff6600;">Error! Please re-check your Email/Password!</span>')

            elif StringUsername[-9:] == '@live.com':     ## LIVE/Hotmal/OutLook

                try:
                    server = smtplib.SMTP('smtp.live.com',587)
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(StringUsername,StringPassword)
                    server.sendmail(StringUsername, StringNumber, header)
                    box.appendHtml('<span style="font-family:arial,helvetica,sans-serif; color:#ff6600;">Message Sent!</span>')
                    server.quit()

                    SentMessagesFile.write('To: '+ StringNumber + '\nMessage: ' + StringMessage + ' on ' + time.ctime() +'\n\n')
                    SentMessagesFile.close()
                    return False
                except:
                    box.appendHtml('<span style="font-family:arial,helvetica,sans-serif; color:#ff6600;">Error! Please re-check your Email/Password!</span>')


        if vslider == 0:
            pass
        ################## EMAIL FUNCTION END #####################



        ############## IF Username sliced and has GMAIL.COM Run Below ###############################
        if len(StringNumber) <= 5:
            box.appendHtml('<span style="font-family:arial,helvetica,sans-serif; color:#ff6600; font-size: 13px;">Error! Please re-check your Recipients Number!</span>')
            return False
        if len(StringMessage) <= 5:
            box.appendHtml('<span style="font-family:arial,helvetica,sans-serif; color:#ff6600;font-size: 13px;">Error! Please re-check your Message! (Atleast 5 or and not greater than 100 Characters!</span>')
            return False
        if len(StringMessage) >= 120:
            box.appendHtml('<span style="font-family:arial,helvetica,sans-serif; color:#ff6600;font-size: 13px;">Ooops! Your Message is too long!</span>')
            return False



        SMSSend = True
        if SMSSend == True:
            teksterNetworks = self.comboBox
            notSelectedNet = teksterNetworks.currentText()
            if 'Select' in notSelectedNet:
                box.appendHtml('<span style="font-family:arial,helvetica,sans-serif; color:#ff6600;font-size: 13px;">Make sure to Select a Network first.</span>')
                return False
            else:
                pass
            teksterNetwork = self.comboBox
            currentTeksterNetworks = teksterNetwork.currentText()
            slicecurrentNet = currentTeksterNetworks[-3:]
            finalTeksterNetwork = eval(str(slicecurrentNet))

            lookUrl = 'http://www.onlinetextmessage.com/send.php'
            Numberx = StringNumber
            Email = StringUsername
            Subject = 'None'
            Quicktext = ''
            Messager = str(Message) + "  -Sent Using Teskter and"
            RequestsString = {
                                'code' : '2B83C2',
                                'number' : Numberx,
                                'from' : Email,
                                'remember' : 'y',
                                'subject' : Subject,
                                'carrier' : finalTeksterNetwork,
                                'quicktext' : '',
                                'message' : Messager,
                                'name' : "Send Message",
                            }
            ProvCheck = urllib.urlencode(RequestsString)
            req2 = urllib2.Request(lookUrl, ProvCheck)
            Lookupresponse = urllib2.urlopen(req2)

            box.appendHtml('<br/><br/><span style="font-size:11px; color:#00ff66;">Message Sent!</span>')
            SentMessagesFile.write('To: '+ StringNumber + '\nMessage: ' + StringMessage + ' on ' + time.ctime() +'\n\n')
            SentMessagesFile.close()
            return False






















if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    Tekster = Ui_MainWindow()
    Tekster.setupUi(MainWindow)
    MainWindow.setWindowFlags(QtCore.Qt.CustomizeWindowHint)  #Border Less
    #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)   # Tekster Frameless
    MainWindow.show()
    sys.exit(app.exec_())


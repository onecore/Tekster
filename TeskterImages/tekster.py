# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tekster.ui'
#
# Created: Tue Oct 29 17:14:08 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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
        MainWindow.resize(753, 915)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(753, 915))
        MainWindow.setMaximumSize(QtCore.QSize(753, 915))
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(_fromUtf8("background-image: url(linen_bg_tile.jpg);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(_fromUtf8("background-image: url(linen_bg_tile.jpg);"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 100, 431, 171))
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
        self.label.setGeometry(QtCore.QRect(100, 160, 71, 16))
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
        self.label_2.setGeometry(QtCore.QRect(100, 200, 71, 16))
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
        self.plainTextEdit_2.setGeometry(QtCore.QRect(50, 280, 661, 541))
        self.plainTextEdit_2.setStyleSheet(_fromUtf8("background: #3498db;/*#5b6bab;*/\n"
"\n"
"\n"
"\n"
"border-radius: 21px 21px 54px 14px;\n"
"\n"
"border: 3px outset #f2f2f2;"))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.MessageBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.MessageBox.setGeometry(QtCore.QRect(100, 370, 381, 391))
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
        self.TeksterLogo.setGeometry(QtCore.QRect(480, 10, 241, 111))
        self.TeksterLogo.setStyleSheet(_fromUtf8("background: transparent;"))
        self.TeksterLogo.setText(_fromUtf8(""))
        self.TeksterLogo.setPixmap(QtGui.QPixmap(_fromUtf8("Untitled-1.png")))
        self.TeksterLogo.setScaledContents(True)
        self.TeksterLogo.setObjectName(_fromUtf8("TeksterLogo"))
        self.SendButton = QtGui.QPushButton(self.centralwidget)
        self.SendButton.setGeometry(QtCore.QRect(110, 700, 361, 51))
        self.SendButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.SendButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"  background-image: -webkit-linear-gradient(top, #66696b, #353a3d);\n"
"  background-image: -moz-linear-gradient(top, #66696b, #353a3d);\n"
"  background-image: -ms-linear-gradient(top, #66696b, #353a3d);\n"
"  background-image: -o-linear-gradient(top, #66696b, #353a3d);\n"
"  background-image: linear-gradient(to bottom, #66696b, #353a3d);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"border-radius: 25px 25px 54px 14px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 18px;\n"
"  padding: 5px 5px 5px 5px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3cb0fd, stop: 1 #3498db);\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #0d5ca6, stop: 1 #2198c0);\n"
"}"))
        self.SendButton.setCheckable(False)
        self.SendButton.setObjectName(_fromUtf8("SendButton"))
        self.NumberBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.NumberBox.setGeometry(QtCore.QRect(170, 330, 191, 21))
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
        self.PasswordPlainTextEditBox.setGeometry(QtCore.QRect(180, 200, 261, 21))
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
        self.UsernamePlainTextEditBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.UsernamePlainTextEditBox.setGeometry(QtCore.QRect(180, 160, 261, 21))
        self.UsernamePlainTextEditBox.setStyleSheet(_fromUtf8("background: #66696b;/*#5b6bab;*/\n"
"\n"
"\n"
"color: #ffffff;\n"
"border-radius: 7px 7px 7px 30px;\n"
"\n"
"border: 1px outset #f2f2f2;"))
        self.UsernamePlainTextEditBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.UsernamePlainTextEditBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.UsernamePlainTextEditBox.setObjectName(_fromUtf8("UsernamePlainTextEditBox"))
        self.OpenSaveUserButton = QtGui.QPushButton(self.centralwidget)
        self.OpenSaveUserButton.setGeometry(QtCore.QRect(270, 230, 81, 31))
        self.OpenSaveUserButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OpenSaveUserButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b6f73, stop: 1 #4e5457);\n"
"  background-image: -webkit-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3498db, #2980b9);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 11px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 11px;\n"
"  padding: 10px 20px 10px 20px;\n"
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
        self.OpenSaveUserButton.setObjectName(_fromUtf8("OpenSaveUserButton"))
        self.SaveCurrentUserButton = QtGui.QPushButton(self.centralwidget)
        self.SaveCurrentUserButton.setGeometry(QtCore.QRect(360, 230, 81, 31))
        self.SaveCurrentUserButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveCurrentUserButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b6f73, stop: 1 #4e5457);\n"
"  background-image: -webkit-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3498db, #2980b9);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 11px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 11px;\n"
"  padding: 10px 20px 10px 20px;\n"
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
        self.SaveCurrentUserButton.setObjectName(_fromUtf8("SaveCurrentUserButton"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 330, 61, 16))
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
        self.plainTextEdit_5.setGeometry(QtCore.QRect(490, 130, 221, 121))
        self.plainTextEdit_5.setStyleSheet(_fromUtf8("background: #3498db;/*#5b6bab;*/\n"
"\n"
"\n"
"\n"
"border-radius: 21px 21px 14px 14px;\n"
"\n"
"border: 3px outset #f2f2f2;"))
        self.plainTextEdit_5.setObjectName(_fromUtf8("plainTextEdit_5"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 150, 51, 51))
        self.label_4.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("GMAIL ICON.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 160, 111, 31))
        self.label_5.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("logo_mail.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(570, 170, 16, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: #ffffff;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.MoreInfoButton = QtGui.QPushButton(self.centralwidget)
        self.MoreInfoButton.setGeometry(QtCore.QRect(530, 210, 151, 31))
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
        self.AddtoContactsButton.setGeometry(QtCore.QRect(370, 330, 91, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.AddtoContactsButton.setFont(font)
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
        self.CharactersCountfromMessageBox.setGeometry(QtCore.QRect(440, 670, 31, 22))
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
        self.toolBox.setGeometry(QtCore.QRect(500, 370, 201, 391))
        self.toolBox.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: #ffffff;"))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.StatusTab = QtGui.QWidget()
        self.StatusTab.setGeometry(QtCore.QRect(0, 0, 201, 319))
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
        self.CheckForUpdate.setGeometry(QtCore.QRect(10, 210, 181, 23))
        self.CheckForUpdate.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #66696b;\n"
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
"  background: #3cb0fd;/*#3cb0fd;*/\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}"))
        self.CheckForUpdate.setObjectName(_fromUtf8("CheckForUpdate"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../Python/button_delete_violet.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolBox.addItem(self.StatusTab, icon, _fromUtf8(""))
        self.ContactsTab = QtGui.QWidget()
        self.ContactsTab.setGeometry(QtCore.QRect(0, 0, 201, 319))
        self.ContactsTab.setObjectName(_fromUtf8("ContactsTab"))
        self.label_16 = QtGui.QLabel(self.ContactsTab)
        self.label_16.setGeometry(QtCore.QRect(70, 0, 71, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.ContactsTab)
        self.label_17.setGeometry(QtCore.QRect(10, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.ContactsTab)
        self.label_18.setGeometry(QtCore.QRect(0, 60, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.AddtoContactNameBOX = QtGui.QPlainTextEdit(self.ContactsTab)
        self.AddtoContactNameBOX.setGeometry(QtCore.QRect(50, 30, 141, 21))
        self.AddtoContactNameBOX.setStyleSheet(_fromUtf8("background: #ffffff;\n"
"color: #000000;"))
        self.AddtoContactNameBOX.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddtoContactNameBOX.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddtoContactNameBOX.setObjectName(_fromUtf8("AddtoContactNameBOX"))
        self.AddtoContactNumberBOX = QtGui.QPlainTextEdit(self.ContactsTab)
        self.AddtoContactNumberBOX.setGeometry(QtCore.QRect(50, 60, 141, 21))
        self.AddtoContactNumberBOX.setStyleSheet(_fromUtf8("background: #ffffff;\n"
"color: #000000;"))
        self.AddtoContactNumberBOX.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddtoContactNumberBOX.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AddtoContactNumberBOX.setObjectName(_fromUtf8("AddtoContactNumberBOX"))
        self.ContactsListBOX = QtGui.QPlainTextEdit(self.ContactsTab)
        self.ContactsListBOX.setGeometry(QtCore.QRect(0, 130, 191, 131))
        self.ContactsListBOX.setStyleSheet(_fromUtf8("background: #ffffff;\n"
"color: #000000;"))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../Python/button_delete_violet.png")), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.toolBox.addItem(self.ContactsTab, icon1, _fromUtf8(""))
        self.SettingsTab = QtGui.QWidget()
        self.SettingsTab.setGeometry(QtCore.QRect(0, 0, 201, 319))
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
        self.label_3.setGeometry(QtCore.QRect(540, 840, 161, 16))
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
        self.label_11.setGeometry(QtCore.QRect(440, 850, 261, 16))
        self.label_11.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(390, 860, 311, 20))
        self.label_13.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_22 = QtGui.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(450, 880, 251, 16))
        self.label_22.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(50, 860, 111, 31))
        self.label_23.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_23.setText(_fromUtf8(""))
        self.label_23.setPixmap(QtGui.QPixmap(_fromUtf8("hacoresec.png")))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.DecimalLabel = QtGui.QLabel(self.centralwidget)
        self.DecimalLabel.setGeometry(QtCore.QRect(480, 160, 16, 61))
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
        self.pushButton.setGeometry(QtCore.QRect(140, 780, 21, 23))
        self.pushButton.setStyleSheet(_fromUtf8("border-image: url(Grin.png);\n"
"\n"
"background: transparent;"))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.HeartEyeEmoticon = QtGui.QPushButton(self.centralwidget)
        self.HeartEyeEmoticon.setGeometry(QtCore.QRect(170, 780, 21, 23))
        self.HeartEyeEmoticon.setStyleSheet(_fromUtf8("border-image: url(Heart.png);\n"
"background: transparent;"))
        self.HeartEyeEmoticon.setText(_fromUtf8(""))
        self.HeartEyeEmoticon.setObjectName(_fromUtf8("HeartEyeEmoticon"))
        self.LaughEmoticon = QtGui.QPushButton(self.centralwidget)
        self.LaughEmoticon.setGeometry(QtCore.QRect(110, 780, 21, 23))
        self.LaughEmoticon.setStyleSheet(_fromUtf8("border-image: url(Laugh.png);\n"
"\n"
"background: transparent;"))
        self.LaughEmoticon.setText(_fromUtf8(""))
        self.LaughEmoticon.setObjectName(_fromUtf8("LaughEmoticon"))
        self.OhhNooEmoticon = QtGui.QPushButton(self.centralwidget)
        self.OhhNooEmoticon.setGeometry(QtCore.QRect(200, 780, 21, 23))
        self.OhhNooEmoticon.setStyleSheet(_fromUtf8("border-image: url(ohnoes.png);\n"
"\n"
"background: transparent;"))
        self.OhhNooEmoticon.setText(_fromUtf8(""))
        self.OhhNooEmoticon.setObjectName(_fromUtf8("OhhNooEmoticon"))
        self.DisappointEmoticon = QtGui.QPushButton(self.centralwidget)
        self.DisappointEmoticon.setGeometry(QtCore.QRect(230, 780, 21, 23))
        self.DisappointEmoticon.setStyleSheet(_fromUtf8("border-image: url(Ambivalent.png);\n"
"\n"
"background: transparent;"))
        self.DisappointEmoticon.setText(_fromUtf8(""))
        self.DisappointEmoticon.setObjectName(_fromUtf8("DisappointEmoticon"))
        self.ConfuseEmoticon = QtGui.QPushButton(self.centralwidget)
        self.ConfuseEmoticon.setGeometry(QtCore.QRect(260, 780, 21, 23))
        self.ConfuseEmoticon.setStyleSheet(_fromUtf8("border-image: url(Confused.png);\n"
"\n"
"background: transparent;"))
        self.ConfuseEmoticon.setText(_fromUtf8(""))
        self.ConfuseEmoticon.setObjectName(_fromUtf8("ConfuseEmoticon"))
        self.GeniusEmoticon = QtGui.QPushButton(self.centralwidget)
        self.GeniusEmoticon.setGeometry(QtCore.QRect(290, 780, 21, 23))
        self.GeniusEmoticon.setStyleSheet(_fromUtf8("border-image: url(Hot.png);\n"
"\n"
"background: transparent;"))
        self.GeniusEmoticon.setText(_fromUtf8(""))
        self.GeniusEmoticon.setObjectName(_fromUtf8("GeniusEmoticon"))
        self.AngryEmoticon = QtGui.QPushButton(self.centralwidget)
        self.AngryEmoticon.setGeometry(QtCore.QRect(320, 780, 21, 23))
        self.AngryEmoticon.setStyleSheet(_fromUtf8("border-image: url(VeryAngry.png);\n"
"\n"
"background: transparent;"))
        self.AngryEmoticon.setText(_fromUtf8(""))
        self.AngryEmoticon.setObjectName(_fromUtf8("AngryEmoticon"))
        self.CryingEmoticon = QtGui.QPushButton(self.centralwidget)
        self.CryingEmoticon.setGeometry(QtCore.QRect(350, 780, 21, 23))
        self.CryingEmoticon.setStyleSheet(_fromUtf8("border-image: url(Crying.png);\n"
"\n"
"background: transparent;"))
        self.CryingEmoticon.setText(_fromUtf8(""))
        self.CryingEmoticon.setObjectName(_fromUtf8("CryingEmoticon"))
        self.BleehEmoticon = QtGui.QPushButton(self.centralwidget)
        self.BleehEmoticon.setGeometry(QtCore.QRect(380, 780, 21, 23))
        self.BleehEmoticon.setStyleSheet(_fromUtf8("border-image: url(Sticking Out Tongue.png);\n"
"\n"
"background: transparent;"))
        self.BleehEmoticon.setText(_fromUtf8(""))
        self.BleehEmoticon.setObjectName(_fromUtf8("BleehEmoticon"))
        self.WinkEmoticon = QtGui.QPushButton(self.centralwidget)
        self.WinkEmoticon.setGeometry(QtCore.QRect(410, 780, 21, 23))
        self.WinkEmoticon.setStyleSheet(_fromUtf8("border-image: url(Wink.png);\n"
"\n"
"background: transparent;"))
        self.WinkEmoticon.setText(_fromUtf8(""))
        self.WinkEmoticon.setObjectName(_fromUtf8("WinkEmoticon"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 780, 21, 23))
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
        self.pushButton_4.setGeometry(QtCore.QRect(500, 780, 91, 21))
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
        self.pushButton_5.setGeometry(QtCore.QRect(600, 780, 91, 21))
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
        self.horizontalSlider.setGeometry(QtCore.QRect(620, 300, 41, 19))
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
        self.label_24.setGeometry(QtCore.QRect(590, 300, 21, 16))
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
        self.label_25.setGeometry(QtCore.QRect(670, 300, 31, 16))
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
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(0)
        QtCore.QObject.connect(self.MessageBox, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.CharactersCountfromMessageBox.stepUp)
        QtCore.QObject.connect(self.SendButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.teksterSendFunction)
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Tekster | Freedom as in Free Open-Source ", None))
        self.label.setText(_translate("MainWindow", "Username", None))
        self.label_2.setText(_translate("MainWindow", "Password", None))
        self.SendButton.setText(_translate("MainWindow", "Send", None))
        self.OpenSaveUserButton.setText(_translate("MainWindow", "Open", None))
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
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt; color:#888888;\">Written in Python by Mark A. Pequeras | Open-Source / GPL V2 Licence</span></p></body></html>", None))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt; color:#888888;\">For Help Please Inquire at http://www.hacore.sf.net/forum</span></p></body></html>", None))
        self.DecimalLabel.setText(_translate("MainWindow", "-", None))
        self.pushButton_3.setText(_translate("MainWindow", "<<", None))
        self.pushButton_4.setText(_translate("MainWindow", "Sent Messages", None))
        self.pushButton_5.setText(_translate("MainWindow", "Contact Us", None))
        self.label_24.setText(_translate("MainWindow", "SMS", None))
        self.label_25.setText(_translate("MainWindow", "Email", None))



    def MoreInformationFunction(self):
        pass

    def CheckForUpdatesFunction(self):
        import urllib

        teksterCount = self.CharactersCountfromMessageBox

        teksterCount.setValue(0)

        teksterBox = self.MessageBox

        def UpdateVersion(object):
            """ INNER FUNCTION FOR CHECKING AND UPDATING VERSION  """
            import urllib
            tfile = open('Version')
            readTfile = tfile.read()
            teksterLVersion = urllib.urlopen('http://tekster.sourceforge.net/latestversion.txt')
            Read = teksterLVersion.read()
            label = self.LatestVersionLabel
            if Read != '4.0':
                return labelappend


        UpdateVersion(object)


        teksterBox.clear(), teksterBox.appendHtml("<html><span style=\"color:#ffd700;\">Checking for Updates....<br/>Please Wait...</span></html>")
        teksterLVersion = urllib.urlopen('http://tekster.sourceforge.net/latestversion.txt')
        Read = teksterLVersion.read()


        if Read != '4.0':   ### NEED TO UPDATE
            return teksterBox.clear(), teksterBox.appendPlainText('Your Tekster Software is Out of Date, New Version is '+ str(Read) +'\n\nPlease Download the New Version at \nhttp://sourceforge.net/projects/tekster/')

        elif Read == '4.0':  ### UPDATED
            teksterBox.clear(), teksterBox.appendHtml("<html><span style=\"color:#ffd700;\">You are already have the Latest Tekster version! 4.0</span></html>")

        else:
            print "none"

    def SaveCredentialsFunction(self):
        pass

    def OpenSaveCredentialsFunction(self):
        pass

    def AddToContactsFunction(self):
        pass

    def ContactUsFunction(self):
        pass

    def SentMessagesFunction(self):
        pass

############     Smilies    ############
    def ShowFullSmileysListFunction(self):
        teksterBox = self.MessageBox
        teksterBox.clear()


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




    def teksterSendFunction(self):
        TeksterHash =   {
                        "a" : "aZ23",
                        "b" : "@31sc",
                        "c" : "@D@dh",
                        "d" : "@daH",
                        }
        Username = self.MessageBox.toPlainText()
        Password = self.MessageBox.toPlainText()
        Message = self.MessageBox.toPlainText()
        Number = self.NumberBox.toPlainText()
        SetEmailLabel = self.EmailServerLabel
        print Username
        print Password
        print Number
######## end  ##########
    def AddNameAndNumbertoContactsFuntion(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


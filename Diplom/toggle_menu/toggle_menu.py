# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\ui\toggle_menu.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 586)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMinimumSize(QtCore.QSize(0, 40))
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_toggle.sizePolicy().hasHeightForWidth())
        self.frame_toggle.setSizePolicy(sizePolicy)
        self.frame_toggle.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame_toggle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_toggle.setStyleSheet("background-color: rgb(255, 100, 255);\n"
"")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_toggle)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setStyleSheet("QPushButton\n"
"{\n"
"    color: rgb(255,255,255);\n"
"    border: 0px sold;\n"
"    text-align: center;\n"
"}\n"
"")
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.horizontalLayout_3.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_2 = QtWidgets.QFrame(self.Top_Bar)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_line = QtWidgets.QFrame(self.frame_2)
        self.frame_line.setMinimumSize(QtCore.QSize(800, 0))
        self.frame_line.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_line.setObjectName("frame_line")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_line)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_line)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.horizontalLayout_4.addWidget(self.frame_line)
        self.frame_btn_find = QtWidgets.QFrame(self.frame_2)
        self.frame_btn_find.setMinimumSize(QtCore.QSize(20, 0))
        self.frame_btn_find.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_btn_find.setStyleSheet("background-color: rgb(52, 113, 255);")
        self.frame_btn_find.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btn_find.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btn_find.setObjectName("frame_btn_find")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_btn_find)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnFind = QtWidgets.QPushButton(self.frame_btn_find)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFind.sizePolicy().hasHeightForWidth())
        self.btnFind.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.btnFind.setFont(font)
        self.btnFind.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:  rgb(85, 170, 255);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 0, 0);\n"
"    padding-top: 5px;\n"
"}")
        self.btnFind.setObjectName("btnFind")
        self.horizontalLayout_5.addWidget(self.btnFind)
        self.horizontalLayout_4.addWidget(self.frame_btn_find)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Btn_page_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_page_1.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_page_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_page_1.setObjectName("Btn_page_1")
        self.verticalLayout_4.addWidget(self.Btn_page_1)
        self.Btn_page_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_page_2.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_page_2.setAutoFillBackground(False)
        self.Btn_page_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    text-overflow: clip;\n"
"    white-space: pre-line\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"    text-overflow: clip;\n"
"}")
        self.Btn_page_2.setAutoDefault(False)
        self.Btn_page_2.setFlat(False)
        self.Btn_page_2.setObjectName("Btn_page_2")
        self.verticalLayout_4.addWidget(self.Btn_page_2)
        self.Btn_page_3 = QtWidgets.QPushButton(self.frame_top_menus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_page_3.sizePolicy().hasHeightForWidth())
        self.Btn_page_3.setSizePolicy(sizePolicy)
        self.Btn_page_3.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_page_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Btn_page_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_page_3.setCheckable(False)
        self.Btn_page_3.setObjectName("Btn_page_3")
        self.verticalLayout_4.addWidget(self.Btn_page_3)
        self.Btn_page_4 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_page_4.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_page_4.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_page_4.setObjectName("Btn_page_4")
        self.verticalLayout_4.addWidget(self.Btn_page_4)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.label_forecast = QtWidgets.QLabel(self.frame_left_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_forecast.sizePolicy().hasHeightForWidth())
        self.label_forecast.setSizePolicy(sizePolicy)
        self.label_forecast.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_forecast.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_forecast.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_forecast.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_forecast.setObjectName("label_forecast")
        self.verticalLayout_3.addWidget(self.label_forecast)
        self.spinBox_fbprophet = QtWidgets.QSpinBox(self.frame_left_menu)
        self.spinBox_fbprophet.setStyleSheet("QSpinBox{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.spinBox_fbprophet.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_fbprophet.setMaximum(1000)
        self.spinBox_fbprophet.setProperty("value", 180)
        self.spinBox_fbprophet.setObjectName("spinBox_fbprophet")
        self.verticalLayout_3.addWidget(self.spinBox_fbprophet)
        self.button_fb = QtWidgets.QPushButton(self.frame_left_menu)
        self.button_fb.setMinimumSize(QtCore.QSize(0, 30))
        self.button_fb.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:  rgb(85, 170, 255);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.button_fb.setObjectName("button_fb")
        self.verticalLayout_3.addWidget(self.button_fb)
        self.lineEdit_long = QtWidgets.QLineEdit(self.frame_left_menu)
        self.lineEdit_long.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.lineEdit_long.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_long.setReadOnly(True)
        self.lineEdit_long.setObjectName("lineEdit_long")
        self.verticalLayout_3.addWidget(self.lineEdit_long)
        self.spinBox_long = QtWidgets.QSpinBox(self.frame_left_menu)
        self.spinBox_long.setStyleSheet("QSpinBox{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.spinBox_long.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_long.setMinimum(40)
        self.spinBox_long.setMaximum(250)
        self.spinBox_long.setProperty("value", 100)
        self.spinBox_long.setObjectName("spinBox_long")
        self.verticalLayout_3.addWidget(self.spinBox_long)
        self.horizontalSlider_long = QtWidgets.QSlider(self.frame_left_menu)
        self.horizontalSlider_long.setMinimum(40)
        self.horizontalSlider_long.setMaximum(250)
        self.horizontalSlider_long.setSingleStep(1)
        self.horizontalSlider_long.setProperty("value", 100)
        self.horizontalSlider_long.setSliderPosition(100)
        self.horizontalSlider_long.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_long.setObjectName("horizontalSlider_long")
        self.verticalLayout_3.addWidget(self.horizontalSlider_long)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.lineEdit_short = QtWidgets.QLineEdit(self.frame_left_menu)
        self.lineEdit_short.setStyleSheet("QLineEdit {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.lineEdit_short.setInputMask("")
        self.lineEdit_short.setFrame(True)
        self.lineEdit_short.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_short.setDragEnabled(False)
        self.lineEdit_short.setReadOnly(True)
        self.lineEdit_short.setObjectName("lineEdit_short")
        self.verticalLayout_3.addWidget(self.lineEdit_short)
        self.spinBox_short = QtWidgets.QSpinBox(self.frame_left_menu)
        self.spinBox_short.setStyleSheet("QSpinBox {\n"
"    background-color: white;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.spinBox_short.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_short.setMinimum(10)
        self.spinBox_short.setMaximum(40)
        self.spinBox_short.setProperty("value", 40)
        self.spinBox_short.setDisplayIntegerBase(10)
        self.spinBox_short.setObjectName("spinBox_short")
        self.verticalLayout_3.addWidget(self.spinBox_short)
        self.horizontalSlider_short = QtWidgets.QSlider(self.frame_left_menu)
        self.horizontalSlider_short.setMinimum(10)
        self.horizontalSlider_short.setMaximum(40)
        self.horizontalSlider_short.setProperty("value", 40)
        self.horizontalSlider_short.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_short.setObjectName("horizontalSlider_short")
        self.verticalLayout_3.addWidget(self.horizontalSlider_short)
        self.label_volatility = QtWidgets.QLabel(self.frame_left_menu)
        self.label_volatility.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_volatility.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_volatility.setFrameShape(QtWidgets.QFrame.Box)
        self.label_volatility.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_volatility.setObjectName("label_volatility")
        self.verticalLayout_3.addWidget(self.label_volatility)
        self.comboBox = QtWidgets.QComboBox(self.frame_left_menu)
        self.comboBox.setStyleSheet("/* The container must be positioned relative: */\n"
"QComboBox {\n"
"  position: relative;\n"
"  font-family: Arial;\n"
"  background-color: white;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QComboBox select {\n"
"  display: none; /*hide original SELECT element: */\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
".select-selected {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Style the arrow inside the select element: */\n"
".select-selected:after {\n"
"  position: absolute;\n"
"  content: \"\";\n"
"  top: 14px;\n"
"  right: 10px;\n"
"  width: 0;\n"
"  height: 0;\n"
"  border: 6px solid transparent;\n"
"  border-color: #fff transparent transparent transparent;\n"
"\n"
"  background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Point the arrow upwards when the select box is open (active): */\n"
".select-selected.select-arrow-active:after {\n"
"  border-color: transparent transparent #fff transparent;\n"
"  top: 7px;\n"
"  background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* style the items (options), including the selected item: */\n"
".select-items div,.select-selected {\n"
"  color: #ffffff;\n"
"  padding: 8px 16px;\n"
"  border: 1px solid transparent;\n"
"  border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;\n"
"  cursor: pointer;\n"
"  background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Style items (options): */\n"
".select-items {\n"
"  position: absolute;\n"
"  background-color: DodgerBlue;\n"
"  top: 100%;\n"
"  left: 0;\n"
"  right: 0;\n"
"  z-index: 99;\n"
"  background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Hide the items when the select box is closed: */\n"
".select-hide {\n"
"  display: none;\n"
"  background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
".select-items div:hover, .same-as-selected {\n"
"  background-color: rgba(0, 0, 0, 0.1);\n"
"  background-color: rgb(255, 255, 255);\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.btn_back = QtWidgets.QPushButton(self.frame_left_menu)
        self.btn_back.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_back.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    color: #FFF;\n"
"    background-color: rgb(62, 180, 158);\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid rgb(48, 50, 62);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(162, 180, 158);\n"
"    padding-top: 5px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setObjectName("btn_back")
        self.verticalLayout_3.addWidget(self.btn_back)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_Toggle.setText(_translate("MainWindow", "Акции"))
        self.btnFind.setText(_translate("MainWindow", "Найти"))
        self.Btn_page_1.setText(_translate("MainWindow", "График"))
        self.Btn_page_2.setText(_translate("MainWindow", "Вола\n"
"тильность"))
        self.Btn_page_3.setText(_translate("MainWindow", "Простая \n"
"стратегия"))
        self.Btn_page_4.setText(_translate("MainWindow", "Прогноз"))
        self.label_forecast.setText(_translate("MainWindow", "Дней"))
        self.button_fb.setText(_translate("MainWindow", "OK"))
        self.lineEdit_long.setText(_translate("MainWindow", "Long"))
        self.lineEdit_short.setText(_translate("MainWindow", "Short"))
        self.label_volatility.setText(_translate("MainWindow", "Месяцев"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "3"))
        self.comboBox.setItemText(2, _translate("MainWindow", "6"))
        self.comboBox.setItemText(3, _translate("MainWindow", "12"))
        self.btn_back.setText(_translate("MainWindow", "Вернуться"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

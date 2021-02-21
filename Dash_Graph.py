# -*- coding: utf-8 -*-


import seaborn as sns
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd
import xlsxwriter
from PyQt5 import QtCore, QtGui, QtWidgets
from Pandas_to_QT import pandasModel
import numpy as np
from Checkablecombobox import CheckableComboBox
import matplotlib.pyplot as plt
import qdarkstyle
import math
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QPushButton, QGridLayout)

"""

This program allows you to filter group and present data.
In addition, you save the filtered/grouped data as CSV/XLSX

Contact me for more info

Author: Ron Elias
Linkedin: www.linkedin.com/in/ronelias7

"""


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowTitle("Dashgraph")
        self.setupUi(self)

    def setupUi(self, MainWindow):
        ###
        # Setting up the Window and Layout
        ###
        # creating a demo dataframe

        self.data = pd.DataFrame(np.random.randint(0,100,size=(100, 8)), columns=list('ABCDEFGH'))
        self.data2 = self.data.copy()

        # window setup
        MainWindow.setObjectName("Dashgraph")
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))
        MainWindow.resize(1800, 900)
        model = pandasModel(self.data)
        view = QTableView()
        view.setModel(model)

        # setting up the central widget layer
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # setting up the table and declaring all the widgets inside the central widget
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setModel(model)
        self.table.setObjectName("TABLE")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 600, 360, 221))
        self.label.hide()
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("Xaxis")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setObjectName("Yaxis")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setObjectName("filter")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setObjectName("groupby")
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setObjectName("slidervalue")
        self.label7 = QtWidgets.QLabel(self.centralwidget)
        self.label7.setObjectName("operator")
        self.label8 = QtWidgets.QLabel(self.centralwidget)
        self.label8.setObjectName("DataFiltering")
        self.label9 = QtWidgets.QLabel(self.centralwidget)
        self.label9.setObjectName("Plotting")
        self.label10 = QtWidgets.QLabel(self.centralwidget)
        self.label10.setObjectName("Descriptive Analysis")
        self.label11 = QtWidgets.QLabel(self.centralwidget)
        self.label11.setObjectName("Meas.Type")
        self.label12 = QtWidgets.QLabel(self.centralwidget)
        self.label12.setObjectName("Select col for boxplot")
        self.label13 = QtWidgets.QLabel(self.centralwidget)
        self.label13.setObjectName("scatter")
        self.combobox1 = QtWidgets.QComboBox(self.centralwidget)
        self.combobox2 = QtWidgets.QComboBox(self.centralwidget)
        self.combobox3 = QtWidgets.QComboBox(self.centralwidget)
        self.combobox4 = QtWidgets.QComboBox(self.centralwidget)
        self.combobox5 = QtWidgets.QComboBox(self.centralwidget)
        self.combobox6 = QtWidgets.QComboBox(self.centralwidget)
        self.combobox7 = CheckableComboBox()
        self.combobox8 = QtWidgets.QComboBox(self.centralwidget)
        self.combobox9 = QtWidgets.QComboBox(self.centralwidget)
        font3 = QtGui.QFont()
        font3.setPointSize(10)
        self.combobox1.setFont(font3)
        self.combobox2.setFont(font3)
        self.combobox3.setFont(font3)
        self.combobox4.setFont(font3)
        self.combobox5.setFont(font3)
        self.combobox6.setFont(font3)
        self.combobox7.setFont(font3)
        self.combobox8.setFont(font3)
        self.combobox9.setFont(font3)
        self.slider = QtWidgets.QSlider(orientation=0x1, parent=self.centralwidget)
        self.slider.setObjectName("filter slider")

        # inserting data to combobox's
        self.combobox4.addItem("Bigger than")
        self.combobox4.addItem("Smaller than")
        self.combobox4.addItem("Equals to")
        self.combobox6.addItem("Mean lvl")
        self.combobox6.addItem("Maximum Value")
        self.combobox6.addItem("Minimum Value")
        for i in self.data.columns:
            self.combobox1.addItem(i)
            self.combobox2.addItem(i)
            self.combobox5.addItem(i)
            if (np.issubdtype(self.data[i].dtype, np.number)):
                self.combobox3.addItem(i)
                self.combobox7.addItem(i)
                self.combobox8.addItem(i)
                self.combobox9.addItem(i)

        # inserting data to slider
        if (np.issubdtype(self.data[self.combobox3.currentText()].dtype, np.number)):
            self.slider.setMaximum(int(self.data[self.combobox3.currentText()].max()))
            self.slider.setMinimum(int(self.data[self.combobox3.currentText()].min()))

        # label font setup
        font = QtGui.QFont()
        font.setPointSize(36)
        font2 = QtGui.QFont()
        font2.setPointSize(12)
        font4 = QtGui.QFont("Times", 14, QtGui.QFont.Bold)
        self.label2.setFont(font2)
        self.label3.setFont(font2)
        self.label4.setFont(font2)
        self.label5.setFont(font2)
        self.label6.setFont(font2)
        self.label7.setFont(font2)
        self.label8.setFont(font4)
        self.label9.setFont(font4)
        self.label10.setFont(font4)
        self.label11.setFont(font2)
        self.label12.setFont(font2)
        self.label13.setFont(font2)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # Menubar setup
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport_Data = QtWidgets.QMenu(self.menubar)
        self.menuExport_Data.setObjectName("menuExport_Data")
        self.menuEdit_View = QtWidgets.QMenu(self.menubar)
        self.menuEdit_View.setObjectName("menuEdit_View")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # buttons setup
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setFixedHeight(60)
        self.Button1.setObjectName("Plot Graph")
        self.Button1.setFont(font2)
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setFont(font2)
        self.Button2.setObjectName("Manipulate rows")
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setObjectName("ExecuteFilter")
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button4.setObjectName("Groupby")
        self.Button5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button5.setObjectName("Plotbox")
        self.Button5.setFixedHeight(60)
        self.Button6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button6.setObjectName("ResetData")
        self.Button7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button7.setObjectName("Plotlinegraph")
        self.Button7.setFixedHeight(60)
        self.Button8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button8.setObjectName("Plotscatter")
        self.Button8.setFixedHeight(60)

        # icons setup
        icon1 = QIcon("barplot")
        icon2 = QIcon("graphplot")
        icon3 = QIcon("filter")
        icon4 = QIcon("launch")
        icon5 = QIcon("groupby")
        icon6 = QIcon("reset")
        icon7 = QIcon("scatter")
        icon8 = QIcon("exit")
        icon9 = QIcon("load")
        icon10 = QIcon("daymode")
        icon11 = QIcon("darkmode")
        icon12 = QIcon("csv")
        icon13 = QIcon("xlsx")

        self.Button1.setIcon(icon1)
        self.Button7.setIcon(icon2)
        self.Button2.setIcon(icon3)
        self.Button3.setIcon(icon3)
        self.Button5.setIcon(icon4)
        self.Button4.setIcon(icon5)
        self.Button6.setIcon(icon6)
        self.Button8.setIcon(icon7)

        size = QSize(40, 40)
        size2 = QSize(30, 30)
        self.Button1.setIconSize(size)
        self.Button7.setIconSize(size)
        self.Button2.setIconSize(size2)
        self.Button3.setIconSize(size2)
        self.Button5.setIconSize(size)
        self.Button4.setIconSize(size2)
        self.Button6.setIconSize(size2)
        self.Button8.setIconSize(size)

        self.Button5.setFont(font2)
        self.Button3.setFont(font2)
        self.Button4.setFont(font2)
        self.Button6.setFont(font2)
        self.Button7.setFont(font2)
        self.Button8.setFont(font2)

        # grid setup
        layout = QGridLayout()
        self.label6.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.table, 0, 0, 19, 1)
        layout.addWidget(self.label8, 0, 1, 1, 1)
        layout.addWidget(self.label4, 1, 1)
        layout.addWidget(self.combobox3, 1, 2)
        layout.addWidget(self.label7, 2, 1)
        layout.addWidget(self.combobox4, 2, 2)
        layout.addWidget(self.slider, 4, 1, 1, 2)
        layout.addWidget(self.label6, 5, 1, 1, 2)
        layout.addWidget(self.Button3, 6, 1, 1, 1)
        layout.addWidget(self.label10, 7, 1)
        layout.addWidget(self.label5, 8, 1)
        layout.addWidget(self.combobox5, 8, 2)
        layout.addWidget(self.label11, 9, 1)
        layout.addWidget(self.combobox6, 9, 2)
        layout.addWidget(self.Button4, 10, 1)
        layout.addWidget(self.Button6, 10, 2)
        layout.addWidget(self.label9, 11, 1)
        layout.addWidget(self.label2, 12, 1)
        layout.addWidget(self.label3, 12, 2)
        layout.addWidget(self.combobox1, 13, 1)
        layout.addWidget(self.combobox2, 13, 2)
        layout.addWidget(self.Button1, 14, 1, 1, 1)
        layout.addWidget(self.Button7, 14, 2, 1, 1)
        layout.addWidget(self.Button2, 5, 2, 3, 1)
        layout.addWidget(self.Button5, 18, 1, 1, 1)
        layout.addWidget(self.label12, 15, 1, 1, 1)
        layout.addWidget(self.label13, 15, 2, 1, 1)
        layout.addWidget(self.combobox7, 16, 1, 2, 1)
        layout.addWidget(self.Button8, 18, 2, 1, 1)
        layout.addWidget(self.combobox8, 16, 2, 1, 1)
        layout.addWidget(self.combobox9, 17, 2, 1, 1)
        # Set the layout on the application's window
        self.centralwidget.setLayout(layout)

        # set actions
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExport_Data = QtWidgets.QAction(MainWindow)
        self.actionExport_Data.setObjectName("actionExport_Data")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionRefresh_Data = QtWidgets.QAction(MainWindow)
        self.actionRefresh_Data.setObjectName("actionRefresh_Data")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.actionDay = QtWidgets.QAction(MainWindow)
        self.actionDay.setObjectName("actionDay")
        self.actionExportToCSV = QtWidgets.QAction(MainWindow)
        self.actionExportToCSV.setObjectName("actionExportToCSV")
        self.actionExportToXLSX = QtWidgets.QAction(MainWindow)
        self.actionExportToXLSX.setObjectName("actionExportToXLSX")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionRefresh_Data)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit_View.addAction(self.actionDay)
        self.menuEdit_View.addAction(self.actionDark)
        self.menuExport_Data.addAction(self.actionExportToCSV)
        self.menuExport_Data.addAction(self.actionExportToXLSX)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExport_Data.menuAction())
        self.menubar.addAction(self.menuEdit_View.menuAction())

        # menu icon setup
        self.actionRefresh_Data.setIcon(icon6)
        self.actionExit.setIcon(icon8)
        self.actionLoad.setIcon(icon9)
        self.actionDay.setIcon(icon10)
        self.actionDark.setIcon(icon11)
        self.actionExportToCSV.setIcon(icon12)
        self.actionExportToXLSX.setIcon(icon13)

        # words to present
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # actions and functions calling
        self.actionLoad.triggered.connect(lambda: self.loaddata())
        self.actionExit.triggered.connect(lambda: self.exit())
        self.actionDay.triggered.connect(lambda: self.daymode())
        self.actionDark.triggered.connect(lambda: self.darkmode())
        self.actionRefresh_Data.triggered.connect(lambda: self.Resetdata())
        self.actionExportToCSV.triggered.connect(lambda: self.savefile())
        self.actionExportToXLSX.triggered.connect(lambda: self.savefile2())
        self.Button2.clicked.connect(lambda: self.manipulate_table())
        self.Button1.clicked.connect(lambda: self.show_bar_graph())
        self.Button3.clicked.connect(lambda: self.executefilter())
        self.Button4.clicked.connect(lambda: self.groupby())
        self.Button5.clicked.connect(lambda: self.show_boxplot())
        self.Button6.clicked.connect(lambda: self.Resetdata())
        self.Button7.clicked.connect(lambda: self.show_line_graph())
        self.Button8.clicked.connect(lambda: self.show_scatter())
        self.slider.valueChanged.connect(lambda: self.label6.setText("Value = " + str(self.slider.value())))
        self.combobox3.currentTextChanged.connect(self.on_combobox_changed)

    ###
    # Functions:
    ###

    ##UI:
    def daymode(self):
        # change to day mode
        app.setStyleSheet("")

    def darkmode(self):
        # change to dark mode
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

    def retranslateUi(self, MainWindow):
        # specifying the content to show to user
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dash Graph"))
        self.label.setText(_translate("MainWindow", "Draft"))
        self.label2.setText(_translate("MainWindow", "Graphs \nColumn for the X axis:"))
        self.label3.setText(_translate("MainWindow", "\nColumn for the Y axis:"))
        self.label4.setText(_translate("MainWindow", "Filter by(choose column):"))
        self.label5.setText(_translate("MainWindow", "Group by(choose column):"))
        self.label6.setText(_translate("MainWindow", "Value = 0"))
        self.label7.setText(_translate("MainWindow", "Choose operator:"))
        self.label8.setText(_translate("MainWindow", "Data Filtering:"))
        self.label9.setText(_translate("MainWindow", "Plotting:"))
        self.label10.setText(_translate("MainWindow", "Descriptive Analysis:"))
        self.label11.setText(_translate("MainWindow", "Meas. Type:"))
        self.label12.setText(_translate("MainWindow", "Box Plot \nselect Columns:"))
        self.label13.setText(_translate("MainWindow", "Scatter and Density Plot\nselect Columns:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport_Data.setTitle(_translate("MainWindow", "Export Data"))
        self.menuEdit_View.setTitle(_translate("MainWindow", "View"))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionExport_Data.setText(_translate("MainWindow", "Export Data"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionDark.setText(_translate("MainWindow", "Dark Mode"))
        self.actionDark.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionDay.setText(_translate("MainWindow", "Day Mode"))
        self.actionDay.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionExportToCSV.setText(_translate("MainWindow", "Save As .CSV"))
        self.actionExportToXLSX.setText(_translate("MainWindow", "Save As .XLSX"))
        self.actionRefresh_Data.setText(_translate("MainWindow", "Reset Data"))
        self.actionRefresh_Data.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.Button1.setText(_translate("MainWindow", "Plot Bar Graph"))
        self.Button2.setText(_translate("MainWindow", "Manual Row Filtering"))
        self.Button3.setText(_translate("MainWindow", "Execute Data Filtering"))
        self.Button4.setText(_translate("MainWindow", "Execute Group by"))
        self.Button5.setText(_translate("MainWindow", "Launch Box Plot"))
        self.Button6.setText(_translate("MainWindow", "Reset Data"))
        self.Button7.setText(_translate("MainWindow", "Plot Line Graph"))
        self.Button8.setText(_translate("MainWindow", "Plot Scatter and Density"))

    ## Exit on demand

    def exit(self):
        # exit application on exit request
        sys.exit(app.exec_())

    ## IO Handeling: Reset, load, and save

    def Resetdata(self):
        # Reset to data2(the backup data)
        self.data = self.data2
        model2 = pandasModel(self.data)
        self.table.setModel(model2)
        self.comboboxdata()

    def loaddata(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file',
                                                 'c:\\', "table (*.csv *.xls)")
        if self.fname != ("", ""):
            self.data = self.csv_opener(self.fname[0])
            self.data2 = self.data.copy()
        model2 = pandasModel(self.data)
        self.table.setModel(model2)
        self.comboboxdata()

    def csv_opener(self, filename):
        try:
            # opening loading and dropping na's from the table
            df = pd.read_csv(filename)
            df = df.dropna()
            return df
        except:
            self.General_error(str(sys.exc_info()[0].__name__))

    def savefile(self):
        try:
            # get a file name and save the data to that dir as CSV
            filename = QFileDialog.getSaveFileName(self, "Save to CSV", "table.csv",
                                                   "Comma Separated Values Spreadsheet (*.csv);;"
                                                   "All Files (*)")[0]
            if filename:
                self.data.to_csv(filename)
        except:
            self.General_error(str(sys.exc_info()[0].__name__))

    def savefile2(self):
        # get a file name and save the data to that dir as XLSX
        filename = QFileDialog.getSaveFileName(self, "Save to xlsx", "table.xlsx",
                                               "Excel Workbook (*.xlsx);;"
                                               "All Files (*)")[0]
        try:
            writer = pd.ExcelWriter(filename, engine='xlsxwriter')
            self.data.to_excel(writer, sheet_name='Sheet1')
            writer.save()
        except:
            self.General_error(str(sys.exc_info()[0].__name__))  # This shouldn't occur, this is a safety measurement.

    ##
    ##Data Filtering and organizing
    ##

    def groupby(self):
        # divide data into groups
        if self.data.empty:
            self.emptydataalert()
            return
        if self.combobox6.currentText() == "Mean lvl":
            self.data = self.data.groupby([self.combobox5.currentText()], as_index=False).mean()
        if self.combobox6.currentText() == "Maximum Value":
            self.data = self.data.groupby([self.combobox5.currentText()], as_index=False).max()
        if self.combobox6.currentText() == "Minimum Value":
            self.data = self.data.groupby([self.combobox5.currentText()], as_index=False).min()
        model2 = pandasModel(self.data)
        self.table.setModel(model2)
        self.comboboxdata()

    def executefilter(self):
        # Execute filter chosen(Column filtering)
        if self.data.empty:
            self.emptydataalert()
            return
        if self.slider.value() == None:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Choose a Value to filter using the slider!')
        col = self.combobox3.currentText()
        model2 = None
        operator = self.combobox4.currentText()
        value = self.slider.value()
        if operator == "Bigger than":
            model2 = pandasModel(self.data[self.data[col] > value])
            self.data = self.data[self.data[col] > value]
        if operator == "Smaller than":
            model2 = pandasModel(self.data[self.data[col] < value])
            self.data = self.data[self.data[col] < value]
        if operator == "Equals to":
            model2 = pandasModel(self.data[self.data[col] == value])
            self.data = self.data[self.data[col] == value]
        if self.table != None:
            self.table.setModel(model2)
        try:
            if not math.isnan(self.data[self.combobox3.currentText()].max()):
                self.slider.setMaximum(int(self.data[self.combobox3.currentText()].max()))
                self.slider.setMinimum(int(self.data[self.combobox3.currentText()].min()))

        except:
            self.General_error(str(sys.exc_info()[0].__name__))  # shouldn't appear, this is a safety meas.

    def manipulate_table(self):
        # Execute filter chosen(Row manual filtering)
        if self.data.empty:
            self.emptydataalert()
            return
        rows = sorted(set(index.row() for index in
                          self.table.selectedIndexes()))
        if rows == []:
            model2 = pandasModel(self.data2)
            self.data = self.data2.copy()
        else:
            model2 = pandasModel(self.data.iloc[rows, :])
            self.data = self.data.iloc[rows, :]

        self.slider.setMaximum(int(self.data[self.combobox3.currentText()].max()))
        self.slider.setMinimum(int(self.data[self.combobox3.currentText()].min()))
        self.table.setModel(model2)

    ##
    ## Handeling data changed(Combobox and slider updating)
    ##
    def comboboxdata(self):
        # update the combobox's data
        self.combobox1.clear()
        self.combobox2.clear()
        self.combobox3.clear()
        self.combobox5.clear()
        self.combobox7.clear()
        self.combobox8.clear()
        self.combobox9.clear()
        for i in self.data.columns:
            self.combobox1.addItem(i)
            self.combobox2.addItem(i)
            self.combobox5.addItem(i)
            if (np.issubdtype(self.data[i].dtype, np.number)):
                self.combobox3.addItem(i)
                self.combobox7.addItem(i)
                self.combobox8.addItem(i)
                self.combobox9.addItem(i)

    def on_combobox_changed(self):
        # updating the slider when user changes the meas.
        if self.combobox3.currentText() != "":
            if (np.issubdtype(self.data[self.combobox3.currentText()].dtype, np.number)):
                self.slider.setMaximum(int(self.data[self.combobox3.currentText()].max()))
                self.slider.setMinimum(int(self.data[self.combobox3.currentText()].min()))

    ##
    ## Data ERROR Handeling
    ##
    def emptydataalert(self):
        # alert if action is being tried when data frame is empty
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("A Data Error occurred!")
        msg.setInformativeText('Data Set is empty.\nPlease load a new data set or hit the "Reset Data" Button')
        msg.setWindowTitle("Error: 112")
        msg.exec_()

    def General_error(self, err):

        error_dialog = QtWidgets.QErrorMessage(self)
        error_dialog.setWindowModality(QtCore.Qt.WindowModal)
        error_dialog.setWindowTitle("General_Error: 113")
        error_dialog.showMessage("Oops! an '" + str(err) + "' error occurred. Please reset dataframe and try again.")

    ##
    ## Plotting:
    ##
    def show_line_graph(self):
        # Plotting a line graph
        if self.data.empty:
            self.emptydataalert()
            return
        plt.clf()
        selectedcombobox1 = self.combobox1.currentText()
        selectedcombobox2 = self.combobox2.currentText()
        plt.title('The Line Graph', fontsize=20)
        plt.xlabel(selectedcombobox1, fontsize=16)
        plt.ylabel(selectedcombobox2, fontsize=16)
        x = self.data[selectedcombobox1]
        y = self.data[selectedcombobox2]
        plt.plot(x, y)
        plt.tight_layout()
        plt.show()

    def show_bar_graph(self):
        # Plot a bar graph
        if self.data.empty:
            self.emptydataalert()
            return
        plt.clf()
        selectedcombobox1 = self.combobox1.currentText()
        selectedcombobox2 = self.combobox2.currentText()

        plt.title('The Bar Graph', fontsize=20)
        plt.xlabel(selectedcombobox1, fontsize=16)
        plt.ylabel(selectedcombobox2, fontsize=16)

        x = self.data[selectedcombobox1]
        y = self.data[selectedcombobox2]

        plt.bar(x, y)
        plt.tight_layout()
        plt.show()

    def show_scatter(self):
        # Plot a scatter graph
        try:
            if self.data.empty:
                self.emptydataalert()
                return
            selectedcombobox1 = self.combobox8.currentText()
            selectedcombobox2 = self.combobox9.currentText()
            if selectedcombobox1 != selectedcombobox2:
                ax = sns.lmplot(x=selectedcombobox1, y=selectedcombobox2, data=self.data, fit_reg=False, height=7)
                sns.kdeplot(data=self.data, x=selectedcombobox1, y=selectedcombobox2, ax=ax)
                plt.show()
        except:
            self.General_error(str(sys.exc_info()[0].__name__))

    def show_boxplot(self):
        # Plot a boxplot
        if self.data.empty:
            self.emptydataalert()
            return
        plt.clf()
        lst = []
        lst2 = []
        adc = []
        for i in self.data.columns:
            if (np.issubdtype(self.data[i].dtype, np.number)):
                lst.append(i)
        # Using the Checkablecombobox lib, I used slicing to find the category chosen
        try:
            adc = str(self.combobox7.currentText()).split("- selected index: ")[1].split(",")
            for i in range(len(adc)):
                adc[i] = int(adc[i])
            # print(adc)

            for i in adc:
                lst2.append(lst[i])
            boxplot = self.data.loc[:, lst2].boxplot()
            plt.title('Statistics Boxplot', fontsize=20)
            plt.xlabel('Category', fontsize=16)
            plt.ylabel('Result', fontsize=16)

            plt.xticks(range(1, len(adc) + 1), lst2, rotation=60)
            plt.tick_params(labelsize=11)
            plt.tight_layout()
            plt.show()
        except:  # In case user didn't choose columns to present
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowModality(QtCore.Qt.WindowModal)
            error_dialog.setWindowTitle("Boxplot plot Error: 113")
            error_dialog.showMessage(
                'In order to present the data in a form of a boxplot, please choose the columns that you would like to plot.')


if __name__ == "__main__":
    import sys

    # showing the window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

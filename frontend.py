from PyQt5 import QtCore, QtGui, QtWidgets
from converter import Conversion


class Ui_MainWindow(object):    # Created using Qt Designer
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_3.addWidget(self.titleLabel)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputLine = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(15)
        self.inputLine.setFont(font)
        self.inputLine.setAlignment(QtCore.Qt.AlignCenter)
        self.inputLine.setObjectName("inputLine")
        self.verticalLayout.addWidget(self.inputLine)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 40, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainButton.sizePolicy().hasHeightForWidth())
        self.mainButton.setSizePolicy(sizePolicy)
        self.mainButton.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.mainButton.setFont(font)
        self.mainButton.setObjectName("mainButton")
        self.verticalLayout_2.addWidget(self.mainButton, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setPointSize(15)
        self.outputLabel.setFont(font)
        self.outputLabel.setText("")
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.verticalLayout_4.addWidget(self.outputLabel)
        self.gridLayout.addLayout(self.verticalLayout_4, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.mainButton.clicked.connect(self.clicked)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Numeral Converter"))
        self.titleLabel.setText(_translate("MainWindow", "Numeral Converter"))
        self.inputLine.setText(_translate("MainWindow", ""))
        self.mainButton.setText(_translate("MainWindow", "Convert"))

    def clicked(self):
        number = self.inputLine.text()
        result = Conversion(number).evaluate()

        if result == "Invalid":
            self.outputLabel.setText(f"Invalid Input")
        else:
            self.outputLabel.setText(f"Converted {number} to {result}")


if __name__ =='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


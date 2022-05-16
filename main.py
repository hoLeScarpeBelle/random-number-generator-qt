import sys
import random as rng
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui


#functions
def generate_number(max,min):
    try:
        min = int(min)
        max = int(max)

        randValue = rng.randint(min,max)
        if randValue < 0 and randValue > -10: 
            numberLabel.setText("-0" + str(abs(randValue)))
        elif randValue < 10 and randValue >= 0:
            numberLabel.setText("0"+str(randValue))
        else:
            numberLabel.setText(str(randValue))
    except Exception as e:
        print("error:" + str(e))
    
#------------------------------------------------

app = QtWidgets.QApplication(sys.argv)

#window conf
win = QtWidgets.QWidget()
win.setWindowTitle('random number generator')
win.setGeometry(0,0,300,300)

#layout
layout = QtWidgets.QGridLayout()
layout.setColumnStretch(2,1)
#layout.setRowStretch(1,2)

#top bar
#--min
layout.addWidget(QtWidgets.QLabel('min'),0,0)
minEntry = QtWidgets.QLineEdit()
minEntry.setText("0")
layout.addWidget(minEntry,0,1)


#--max
layout.addWidget(QtWidgets.QLabel('max'),0,3)
maxEntry = QtWidgets.QLineEdit()
maxEntry.setText("10")
layout.addWidget(maxEntry,0,4)

#central label
numberLabel = QtWidgets.QLabel('00')
numberLabel.setAlignment(QtCore.Qt.AlignCenter)
numberLabel.setStyleSheet("background-color:pink;color:black;font-size: 60px")
layout.addWidget(numberLabel,1,0,4,5)#fromrow;fromcolumn;rowSpan;columnSpan;

#bottom button

sendButton = QtWidgets.QPushButton('go')
sendButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
sendButton.clicked.connect(lambda : generate_number(maxEntry.text(),minEntry.text()))

layout.addWidget(sendButton,5,0,2,5)

win.setLayout(layout)

#show window 
win.show()
sys.exit(app.exec())
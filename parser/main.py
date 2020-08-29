'''
Translate Text to JSON
For use SQL > extract Excel > copy to Text > JSON
to analyze data.

@author Bunedin
@version 1.0
'''

import sys, json
import json_parser
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QLineEdit, QLabel, QPushButton, QVBoxLayout, qApp
from PyQt5.QtGui import QIcon

class GuiMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #Label
        self.lbFileName = QLabel(self)
        self.lbFileName.setText('Please input the file link from [File>Open]')
        self.lbFileName.resize(500, 50)
        self.lbFileName.move(50, 40)

        #StatusBar
        self.statusBar()

        #Button
        self.btnSend = QPushButton('&Send', self)
        self.btnSend.setShortcut('Ctrl+S')
        self.btnSend.move(550, 50)
        self.btnSend.clicked.connect(lambda : self.sendFile(self.lbFileName.text()))

        #openAction on Menubar
        openFile = QAction(QIcon('open.png'), '&Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        closeWindow = QAction(QIcon('exit.png'), '&Quit', self)
        closeWindow.setShortcut('Ctrl+Q')
        closeWindow.setStatusTip('Quit')
        closeWindow.triggered.connect(qApp.quit)

        #menuBar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(closeWindow)

        self.setWindowTitle('File Loader')
        self.setGeometry(300, 300, 700, 120)
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', './')

        if fname[0]:
            f = open(fname[0], 'r')
            self.lbFileName.setText(fname[0])

    def sendFile(self, text_link):
        if text_link == '' or text_link == 'Please input the file link from [File>Open]':
            pass
        else:
            return_dic = json_parser.trans_to_json(text_link)
            self.dialog = JsonViewer()
            self.dialog.textEdit.setText(json.dumps(return_dic, ensure_ascii=False, indent='\t'))
            #self.dialog.exec_()


class JsonViewer(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #textEditor
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        #statusBar
        self.statusBar()

        #text Save
        saveFile = QAction(QIcon('save.png'), '&Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.showDialog)

        #close Window
        closeWindow = QAction(QIcon('exit.png'), '&Quit', self)
        closeWindow.setShortcut('Ctrl+Q')
        closeWindow.setStatusTip('Quit')
        closeWindow.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(saveFile)
        fileMenu.addAction(closeWindow)

        self.setWindowTitle('JSON')
        self.setGeometry(300, 300, 600, 400)
        self.show()

    def showDialog(self):
        fname = QFileDialog.getSaveFileName(self, 'Save File', './')
        f = open(fname[0], 'w')
        text = self.textEdit.toPlainText()
        f.write(text)
        f.close()

def main():
    app = QApplication(sys.argv)
    main = GuiMain()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
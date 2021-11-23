from MiniDBsetup import MiniDB
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from Time import Time


class MainWindow(QMainWindow, Time, MiniDB):
    def __init__(self):
        super().__init__()

        self.clearDB()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Time Counter 3.0')
        self.setFixedSize(500, 500)

        push_btn1 = QPushButton('Start', self)
        push_btn1.setFixedSize(200, 30)
        push_btn1.move(150, 200)
        push_btn2 = QPushButton('End', self)
        push_btn2.setFixedSize(200, 30)
        push_btn2.move(150, 250)
        push_btn3 = QPushButton('Show 3 latest sessions', self)
        push_btn3.setFixedSize(200, 30)
        push_btn3.move(150, 300)
        push_btn4 = QPushButton('Show total time', self)
        push_btn4.setFixedSize(200, 30)
        push_btn4.move(150, 350)

        push_btn1.clicked.connect(self.start_btn)
        push_btn2.clicked.connect(self.end_btn)
        push_btn3.clicked.connect(self.show_sessions)
        push_btn4.clicked.connect(self.show_total)

        self.show()

    def start_btn(self):
        msg = QMessageBox()
        msg.setWindowTitle(' ')
        msg.setText(Time.start(self))
        msg.exec()

    def end_btn(self):
        msg = QMessageBox()
        msg.setWindowTitle(' ')
        msg.setText(Time.end(self))
        msg.exec()

    def show_sessions(self):
        msg = QMessageBox()
        msg.setWindowTitle(' ')
        msg.setText(Time.show3lastSessions(self))
        msg.exec()

    def show_total(self):
        msg = QMessageBox()
        msg.setWindowTitle(' ')
        msg.setText(Time.showTotalTime(self))
        msg.exec()


if __name__ == '__main__':
    app = QApplication()
    win = MainWindow()

    sys.exit(app.exec())

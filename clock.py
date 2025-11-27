import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer,QTime


class digitalclock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 200, 100)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 120px;" "color: blue;")
        self.setStyleSheet("background-color: black;")
        self.timer.timeout.connect(self.upddate_time)
        self.timer.start(1000)
        self.upddate_time()

    def upddate_time(self):
        cuurent_time= QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(cuurent_time)
        






def main():
    app = QApplication(sys.argv)
    window = digitalclock()
    window.show()
    sys.exit(app.exec_())
    app = QApplication(sys.argv)
    
    window.show()
    sys.exit(app.exec_())
   
   




if __name__ == "__main__":
    main()
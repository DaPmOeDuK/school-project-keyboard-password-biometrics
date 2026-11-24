from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ведите пароль")
        self.setGeometry(750, 400, 500, 150)

        # self.lbl = QLabel()

        self.line = QLineEdit(self)
        self.line.setPlaceholderText("Пример: password#1234")
        self.line.setFixedSize(460, 35)
        self.line.move(20,10)

        self.ready_btn = QPushButton(self)
        self.ready_btn.setText("Готово")
        self.ready_btn.clicked.connect(self.check)
        self.ready_btn.setFixedSize(150, 25)
        self.ready_btn.move(175,50)

        def check(self):
            pass #here would be retranslating to the server part




def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
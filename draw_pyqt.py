# ************************** man hinh loai 2 *************************
import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        canvas = QtGui.QPixmap(500, 400)
        canvas.fill(QtGui.QColor('white'))
        self.uic.label.setPixmap(canvas)
        self.draw_something()

    def draw_something(self):
        painter = QtGui.QPainter(self.uic.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)

        # all. Filled rectangles
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("#FFD141"))
        # brush.setStyle(Qt.Dense1Pattern)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)

        # 1. draw line
        # painter.drawLine(10, 20, 100, 120)
        # 2. draw point
        # painter.drawPoint(200, 150)
        # 3. draw point random
        # for n in range(10):
        #     painter.drawPoint(
        #         200 + randint(-100, 100),  # x
        #         150 + randint(-100, 100)  # y
        #     )
        # 4. draw rectangle
        painter.drawRect(50, 50, 100, 100)
        painter.drawRect(100, 60, 150, 100)
        # 5. draw Rounded_rectangle
        # painter.drawRoundedRect(40, 40, 100, 100, 10, 10)
        # painter.drawRoundedRect(60, 60, 150, 200, 40, 40)
        # 6. draw Ellipse
        # painter.drawEllipse(10, 10, 100, 100)
        # painter.drawEllipse(40, 20, 100, 200)
        # 7. draw text
        # font = QtGui.QFont()
        # font.setFamily('Times')
        # font.setBold(True)
        # font.setPointSize(20)
        # painter.setFont(font)
        # painter.drawText(10, 50, 'Hello, world!')
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
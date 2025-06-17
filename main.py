import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Pet(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()

        # 加载 GIF 表情
        self.movie = QtGui.QMovie("momocat.gif")  # 换成你的GIF路径
        self.setMovie(self.movie)
        self.movie.start()

        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint  # 无边框
            | QtCore.Qt.WindowStaysOnTopHint  # 总在最前
            | QtCore.Qt.Tool  # 任务栏不显示
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 透明背景

        self.resize(128, 128)

        # 设置初始位置在右下角
        screen = QtWidgets.QApplication.desktop().screenGeometry()
        self.move(screen.width() - self.width(), screen.height() - self.height())

        self.show()

        # 定时移动
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.move_pet)
        self.timer.start(100)  # 每100ms移动一次

        # 用于记录鼠标拖动
        self.dragging = False
        self.offset = QtCore.QPoint()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = False

    def move_pet(self):
        if not self.dragging:  # 只在不拖拽时随机移动
            x = self.x() + random.choice([-1, 1, 0])
            y = self.y() + random.choice([-1, 1, 0])
            screen = QtWidgets.QApplication.desktop().screenGeometry()
            # 防止超出屏幕边界
            x = max(0, min(x, screen.width() - self.width()))
            y = max(0, min(y, screen.height() - self.height()))
            self.move(x, y)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pet = Pet()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(500, 350)
        self.center() # 창이 화면 가운데 위치하게하는 함수 실행
        self.show()

    # 화면 가운데 위치하게하는 함수
    def center(self):
        qr = self.frameGeometry() # 창의 위치와 크기 정보를 가져온다.
        cp = QDesktopWidget().availableGeometry().center() # 사용하는 모니터 화면의 가운데 위치 파악
        qr.moveCenter(cp) # 직사각형 위치를 중심위치로 이동
        self.move(qr.topLeft()) # 창 이동


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
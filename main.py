import sys
from PyQt5.QtWidgets import QApplication
from MyMnistWindow import MyMnistWindow
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mymnist = MyMnistWindow()
    mymnist.show()
    app.exec_()

import getpass
import os
import sys
import random

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import subprocess
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Ёбнуть свой комп нахуй!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        self.destroy(True,True)
        os.system('taskkill /f /im explorer.exe')
        user = getpass.getuser()
        os.system('taskkill /f /im browser.exe')
        os.system('taskkill /f /im opera.exe')
        os.system('taskkill /f /im chrome.exe')
        os.system('taskkill /f /im firefox.exe')
        os.system('taskkill /f /im msedge.exe')
        os.system('taskkill /f /im steam.exe')
        out_red("the process of removing the system has begun")
        for i in range (101):

            out_red(f"{i}%")
            time.sleep(random.randint(0, 2))
        out_red("system32.exe was successfully deleted")
        time.sleep(2)
        out_red(f"{user} was successfully deleted")
        out_red("please restart your system")
def out_red(text):
    print("\033[31m{}".format(text))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
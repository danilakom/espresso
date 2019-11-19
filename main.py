from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys
import sqlite3


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"E:\Введение в репозитории. Подключение в PyCharm. Работа с удаленным репозиторием\Эспрессо\main.ui", self)
        self.initUi()
    
    def initUi(self):
        con = sqlite3.connect(r"E:\Введение в репозитории. Подключение в PyCharm. Работа с удаленным репозиторием\Эспрессо\coffee.sqlite")
        cur = con.cursor()

        result = list(cur.execute("select * from coffe").fetchall())
        c = ["ID", "Сорт", "Степень обжарки", "Молотый/зерновой", "Описание вкуса", "Цена", "Объем упаковки"]
        self.table.setColumnCount(len(c))
        self.table.setHorizontalHeaderLabels(c)
        self.table.setRowCount(0)
        for i, row in enumerate(result):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(str(elem)))
        self.table.resizeColumnsToContents()


app = QApplication(sys.argv)
a = App()
a.show()
sys.exit(app.exec_())

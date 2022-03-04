import sys,os
from TestIntegracion import MainWindow
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel

class Test():

    def Estres():
        app = QApplication.instance()
        if app == None:
            app = QApplication([])
        apli = MainWindow()
        window = QWidget()
        for i in range(10000):
            apli.nueva()

        app.quit()
        window.close()

if __name__ == '__main__':
    Test.Estres()
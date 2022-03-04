import unittest
import sys,os
from TestIntegracion import MainWindow
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel

class Tests(unittest.TestCase):

    def test_insert(self):
        app = QApplication.instance()
        if app == None:
            app = QApplication([])
        apli = MainWindow()
        window = QWidget()
       
        before=apli.modelo.rowCount()
        apli.nueva()
        after=apli.modelo.rowCount()
        self.assertEqual(before+1,after)
        app.quit()
        window.close()

    def test_borrar(self):
        app = QApplication.instance()
        if app == None:
            app = QApplication([])
        apli = MainWindow()
        window = QWidget()
       
        before=apli.modelo.rowCount()
        apli.borrar()
        after=apli.modelo.rowCount()
        self.assertEqual(before,after)
        app.quit()
        window.close()
    
    def test_informe(self):
        app = QApplication.instance()
        if app == None:
            app = QApplication([])
        apli = MainWindow()
        window = QWidget()

        self.nombre = "juan"
        self.Apellidos = "Yuan"
        self.cursoId = 5
        self.media1 = 5.25
        self.media2 = 9.99
        self.media3 = 2.56
        apli.generate(self.nombre,self.Apellidos,self.cursoId)

        try:
            file = open('result.pdf')
            print(file) # File handler
            self.assertEqual(os.path.exists('result.pdf'),True)
            file.close()
            app.quit()
            window.close()
        except FileNotFoundError:
            print('Sorry the file we\'re looking for doesn\'t exist')
            exit()
        

if __name__ == '__main__':
    unittest.main()
    
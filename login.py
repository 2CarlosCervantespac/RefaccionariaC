from PyQt5 import QtWidgets, uic
from main import VentanaPrincipal

app = QtWidgets.QApplication([])

login = uic.loadUi("login.ui")
entrar = VentanaPrincipal()
error = uic.loadUi("error.ui")

def gui_login():
    correo = login.lineEdit.text()
    password = login.lineEdit_2.text()

    if len(correo)==0 or len(password)==0:
        login.label_5.setText("Ingrese todos los datos")
    elif correo == "refa@gmail.com" and password == "1234":
        gui_entrar()
    else:
        gui_error()

def gui_entrar():
    login.hide()
    entrar.show()

def gui_error():
    login.hide()
    error.show()

def regresar_entrar():
    entrar.hide()
    login.show()

def regresar_error():
    error.hide()
    login.label_5.setText("")
    login.show()

def salir():
    app.exit()

login.pushButton.clicked.connect(gui_login)

entrar.pushButton.clicked.connect(regresar_entrar)
error.pushButton.clicked.connect(regresar_error)
error.pushButton_2.clicked.connect(salir)


login.show()
app.exec()


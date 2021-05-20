from portfolio import Ui_MainWindow as Portfolio_window
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow


'''
Окно "Портфель"
'''


class Portfolio(QMainWindow):
    def __init__(self):
        super(Portfolio, self).__init__()
        self.ui = Portfolio_window()
        self.ui.setupUi(self)
        self.main = None
        self.pick_up = None
        self.create = None
        self.initUI()

    def initUI(self):
        self.ui.button_back.clicked.connect(self.back)
        self.ui.button_pick_up.clicked.connect(self.pick_up_fun)
        self.ui.button_create.clicked.connect(self.create_portfolio)

    def pick_up_fun(self):
        from Pick_up_portfolio_class import PickUpPortfolio
        self.pick_up = PickUpPortfolio()
        self.pick_up.setWindowTitle("Stocker")
        self.pick_up.setWindowIcon(QtGui.QIcon("images\portfolio.png"))
        self.pick_up.show()
        self.close()

    def create_portfolio(self):
        from Create_portfolio_class import Create_Portfolio
        self.create = Create_Portfolio()
        self.create.setWindowTitle("Stocker")
        self.create.setWindowIcon(QtGui.QIcon("images\portfolio.png"))
        self.create.show()
        self.close()

    def back(self):
        from main import MainWindow_main
        from ui_functions import UIFunctions
        self.main = MainWindow_main()
        self.main.setWindowTitle("Stocker")
        self.main.setWindowIcon(QtGui.QIcon("images\portfolio.png"))
        self.main.show()
        self.close()

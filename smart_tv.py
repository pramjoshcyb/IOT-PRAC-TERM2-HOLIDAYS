from PyQt5.Qt import * # from the Qt5 library import everything
from PyQt5.QtWidgets import * # from the Qt5 library import all Widgets
from PyQt5.QtCore import * # from Qt5 import everything
from PyQt5.QtGui import * # from Qt5 import everything 

import rpyc # import remote procedure call

class SmartTV():
    def __init__(self): 
        """initialise the class and attribute self"""
        self.app = QApplication([])
        
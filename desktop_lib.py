from PySide import QtGui, QtCore
#Galax Desktop prototypes

class GalaxPanel(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setAttribute(QtCore.Qt.WA_X11NetWmWindowTypeDock, True)
		

app=QtGui.QApplication([])

g=GalaxPanel()
g.show()
app.exec_()
import numpy as np
import pandas as pd
import pyqtgraph as pg
from PIL import Image

from pyqtgraph.Qt import QtGui, QtWidgets

app = pg.mkQApp("Scatter Plot")
mw = QtWidgets.QMainWindow()
mw.resize(1000,800)
view = pg.GraphicsLayoutWidget()
mw.setCentralWidget(view)
mw.show()
mw.setWindowTitle('show sonic')
w = view.addPlot()

clickedPen = pg.mkPen('b', width=2)
lastClicked = []


def clicked(plot, points):
    global lastClicked
    for p in lastClicked:
        p.resetPen()
    for p in points:
        p.setPen(clickedPen)
    lastClicked = points
    idx = points[0].index()
    path = "./images/{:0>5d}.png".format(idx * 3)
    img = Image.open(path)
    img.show()


data = pd.read_csv("test.csv")
data = data.values.tolist()
s = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120))
s.addPoints(pos=data)
w.addItem(s)
s.sigClicked.connect(clicked)


if __name__ == '__main__':
    pg.exec()

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
from numpy import double
from matplotlib.widgets import Button


def read_file(filepath):
    f = open(filepath)
    x = []
    y = []
    z = []
    line = f.readline()
    while line:
        row = line.split(',')
        t1 = double(row[0])
        t2 = double(row[1])
        t3 = double(row[2])
        x.append(t1)
        y.append(t2)
        z.append(t3)
        line = f.readline()
    f.close()
    return x, y, z


def call_back(event):
    try:
        ax = event.inaxes
        x_min, x_max = ax.get_xlim()
        scale = (x_max - x_min) / 10
        if event.button == 'up':
            ax.set(xlim=(x_min + scale, x_max - scale))
        elif event.button == 'down':
            ax.set(xlim=(x_min - scale, x_max + scale))
        fig.canvas.draw_idle()
    except:
        print("retry")
        return


def show_onclick(event):
    try:
        global flag
        global point_index
        flag = False
        point_index = int(event.ind)
        print(point_index)
        path = "./images/{:0>5d}.png".format(point_index * 3)
        img = Image.open(path)
        image.imshow(img)
        origin.color = "#B9E4C9"
        result.color = "#37966F"
        fig.canvas.draw_idle()
    except:
        print("retry")
        return


def show_origin(event):
    path = "./images/{:0>5d}O.png".format(point_index * 3 + 2)
    img = Image.open(path)
    image.imshow(img)
    origin.color = "#37966F"
    result.color = "#B9E4C9"
    fig.canvas.draw_idle()


def show_result(event):
    path = "./images/{:0>5d}.png".format(point_index * 3)
    img = Image.open(path)
    image.imshow(img)
    origin.color = "#B9E4C9"
    result.color = "#37966F"
    fig.canvas.draw_idle()


point_index = 0
if __name__ == "__main__":
    fig = plt.figure(figsize=(17, 10))
    graph = fig.add_subplot(121, projection='3d')
    graph.set_xlabel('X')
    graph.set_ylabel('Y')
    graph.set_zlabel('Z')
    graph.set_box_aspect(aspect=(5, 1, 1))
    x, y, z = read_file('R_2022_08_05_16_04_35.txt')
    plt.xlim((min(x), max(x)))
    scatter = graph.scatter(x, y, z, picker=True)
    fig.canvas.mpl_connect('pick_event', show_onclick)
    fig.canvas.mpl_connect('scroll_event', call_back)
    image = fig.add_subplot(122)
    image.axis('off')
    pos1 = plt.axes([0.38, 0.02, 0.1, 0.05])
    pos2 = plt.axes([0.54, 0.02, 0.1, 0.05])
    origin = Button(pos1, 'origin', color="#B9E4C9", hovercolor="#37966F")
    result = Button(pos2, 'result', color="#B9E4C9", hovercolor="#37966F")
    origin.on_clicked(show_origin)
    result.on_clicked(show_result)
    plt.show()

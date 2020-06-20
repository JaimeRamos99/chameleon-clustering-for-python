import networkx as nx
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot2d_graph(graph):
    pos = nx.get_node_attributes(graph, 'pos')
    c = [colors[i % (len(colors))]
         for i in nx.get_node_attributes(graph, 'cluster').values()]
    if c:  # is set
        nx.draw(graph, pos, node_color=c, node_size=0.25)
    else:
        nx.draw(graph, pos, node_size=0.25)
    plt.show(block=False)


def plot2d_data(df):
    if (len(df.columns) > 3):
        print("Plot Warning: more than 2-Dimensions!")
    limit = len(df.index)
    matrix = []
    xx = []
    yy = []
    cc = []
    for i in range(limit):
        valor =str(df[0][i]).split(",")
        nuevo = [float(valor[0]),float(valor[1]),float(df['cluster'][i])]
        matrix.append(nuevo)
        xx.append(float(valor[0]))
        yy.append(float(valor[1]))
        cc.append(float(df['cluster'][i]))
    dff = pd.DataFrame(matrix, columns=['x', 'y', 'cluster'])
    dff.plot.scatter(x='x',
                      y='y',
                      c='cluster', colormap='gist_rainbow')
    print('----------')
    colors = np.random.rand(limit)
    plt.scatter(xx, yy, s=cc, c=colors,alpha=0.5)
    plt.show()

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 20:09:46 2017

@author: teemuko

prerequisites: pip install graphviz

Tutorial: http://matthiaseisen.com/articles/graphviz/
"""

import graphviz as gv
gv.Graph.node
import functools
graph = functools.partial(gv.Graph, format='svg')
# Dont set label if it is not explicitly defined
digraph = functools.partial(gv.Digraph, format='svg', graph_attr={'compound': 'true','label': ''})

def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph

def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph


G=digraph()
G1 = digraph(name='cluster_1',graph_attr={'label': 'Sub graph label'})
G2 = digraph(name='cluster_2')
G3 = digraph(name='cluster_3')
G4 = digraph(name='cluster_4')
G5 = digraph(name='cluster_5')
G6 = digraph(name='cluster_6')

add_nodes(G1,[('A',{'shape': "Mrecord",'label': """<State #6<br/><font point-size='8'>foo</font>>"""}), 'B', 'C'])
add_nodes(G2,['A2', 'B2', 'C2'])
add_nodes(G3,['A3', 'B3', 'C3'])
add_nodes(G4,['A3', 'B4', 'C2'])
#add_nodes(G5,['A5', 'B5', 'C5'])
add_edges(G,[('A','B')])


add_edges(G,[(('C2','B'),{'label': 'Joo','ltail': 'cluster_2'})])
#add_edges(G,[(('A3','B'),{'label': 'Joo','ltail': 'cluster_3'})])


G1.subgraph(G2)

G4.subgraph(G5)
G4.subgraph(G3)
G.subgraph(G1)
G.subgraph(G4)


G.render('img/g5')

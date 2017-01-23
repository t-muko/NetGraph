# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 22:03:21 2017

@author: teemuko
"""

import networkx as nx

import matplotlib.pyplot as plt
#from networkx.drawing.nx_pydot import write_dot
from networkx.drawing.nx_agraph import write_dot
from networkx.drawing.nx_agraph import graphviz_layout
pos = graphviz_layout(G)

#G=nx.Graph()
#G.add_nodes_from([2,3,'fooba','mollo'])
#G.add_edge(1,2)

MG=nx.MultiDiGraph()
MG.add_nodes_from([1,2,3],label='baa')
MG.add_weighted_edges_from([(1,2,0.5), (2,1,0.5), (2,3,.5)],label="foo")
MG.degree(weight='weight')

nx.draw(MG)
#nx.draw(MG,pos=nx.spring_layout(MG)) # use spring layout
#nx.draw_networkx(MG,labels={'label'})

#write_dot(MG,'multi.dot')
#nx.draw(MG, pos, prog='neato')

#G=nx.MultiGraph()
#G.add_edge(1,2)
#G.add_edge(1,2)
#nx.write_dot(G,'multi.dot')
#nx.draw(G, pos, prog='neato')

#!neato -T png multi.dot > multi.png
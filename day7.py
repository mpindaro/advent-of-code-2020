import networkx as nx
import numpy as np
import re


def make_graph(lines):
    lines = [line[:-1] for line in lines]
    g = nx.DiGraph()
    for line in lines:
        source,targets = line.split(' contain ')
        source = source.replace(' bags','')
        if 'no other bags' not in targets:
            for starget in targets.split(', '):
                w = int(starget[0])
                target = re.search('([a-z]+ [a-z]+)',starget).group(1)
                g.add_edge(source,target,weight=w)
    return g


def get_parents_of(graph,node):
    return len(nx.ancestors(graph,node))



def get_bags_in(graph,node):
    countbags = []
    descendants = list(nx.descendants(graph,node))
    allpaths = list(nx.all_simple_paths(graph.subgraph(descendants+[node]),source=node,target=descendants))
    for path in allpaths:
        countbags.append(np.prod([graph[path[i]][path[i+1]]['weight'] for i in range(len(path)-1)]))
    return sum(countbags)


with open('inputs/day7/input.txt','r') as rf:
    lines = rf.readlines()
    graph = make_graph(lines)
    print("Challenge 1: {}".format(get_parents_of(graph,'shiny gold')))
    print("Challenge 2: {}".format(get_bags_in(graph,'shiny gold')))







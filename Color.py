# Import tkinter library
import networkx as nx
import random
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value, color):
        self.__value = value
        self.__color = color

    def get_value(self):
        return self.__value

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


class Graph:
    def __init__(self, available_colors=None):
        self.__nodemap = {}
        self.__graph = {}

        if available_colors is None:
            self.__available_colors = ["red", "green", "blue", "yellow", "orange", "purple"]
        else:
            self.__available_colors = available_colors

        self.__selected_colors = []

    def add_undirected_edge(self, u, v):
        if u not in self.__nodemap:
            u_node = Node(u, None)
            self.__nodemap[u] = u_node

        if v not in self.__nodemap:
            v_node = Node(v, None)
            self.__nodemap[v] = v_node

        if len(self.__graph.keys()) == 0:
            start_node_color = random.choice(list(self.__available_colors))
            self.__selected_colors.append(start_node_color)
            self.__nodemap[u].set_color(start_node_color)

        if u in self.__graph:
            self.__graph[u].append(v)
        else:
            self.__graph[u] = [v]

        if v in self.__graph:
            self.__graph[v].append(u)
        else:
            self.__graph[v] = [u]

    def __get_adjacent_vertices(self, node):
        return self.__graph[node]

    def color(self):
        for parent_node in list(self.__graph.keys()):
            parent_color = self.__nodemap[parent_node].get_color()

            neighbour_colors = []
            for neighbour_node in self.__get_adjacent_vertices(parent_node):
                neighbour_colors.append(self.__nodemap[neighbour_node].get_color())

            if parent_color is None:
                unique_neighbour_colors = [x for x in neighbour_colors if x is not None]
                non_chosen_colors = set(self.__selected_colors) - set(unique_neighbour_colors)

                if len(non_chosen_colors) == 0:
                    non_selected_new_color = random.choice(list(set(self.__available_colors) - set(neighbour_colors)))
                    self.__nodemap[parent_node].set_color(non_selected_new_color)
                    self.__selected_colors.append(non_selected_new_color)
                else:
                    self.__nodemap[parent_node].set_color(random.choice(list(non_chosen_colors)))

            print(self.__nodemap[parent_node].get_value(), self.__nodemap[parent_node].get_color(), "->",
                  neighbour_colors)

        for node in self.__nodemap:
            print(self.__nodemap[node].get_value(), self.__nodemap[node].get_color())

    def visualize_w_color(self):
        self.color()

        ordered_nodes = list(self.__nodemap.keys())
        n_node = len(ordered_nodes)
        adj_matrix = np.zeros((n_node, n_node))
        for node in self.__graph:
            for neighbour in self.__graph[node]:
                adj_matrix[ordered_nodes.index(node), ordered_nodes.index(neighbour)] = 1

        adj_df = pd.DataFrame(adj_matrix, index=ordered_nodes, columns=ordered_nodes)

        G = nx.from_pandas_adjacency(adj_df)
        node_colormap = []
        for node in G:
            node_colormap.append(self.__nodemap[node].get_color())
        nx.draw(G, node_color=node_colormap, with_labels=True)
        plt.show()


if __name__ == "__main__":
    graph = Graph()
    """graph.add_undirected_edge(1, 3)
    graph.add_undirected_edge(1, 2)
    graph.add_undirected_edge(1, 4)
    graph.add_undirected_edge(2, 4)
    graph.add_undirected_edge(2, 5)
    graph.add_undirected_edge(4, 7)
    graph.add_undirected_edge(5, 7)
    graph.add_undirected_edge(3, 6)
    graph.add_undirected_edge(4, 6)
    graph.add_undirected_edge(6, 7)
    graph.add_undirected_edge(3, 4)
    graph.add_undirected_edge(4, 5)"""

    #graph.add_undirected_edge("A", "B")
    #graph.add_undirected_edge("A", "C")
    #graph.add_undirected_edge("A", "D")
    #graph.add_undirected_edge("A", "E")
    #graph.add_undirected_edge("A", "F")
    #graph.add_undirected_edge("B", "F")
    #graph.add_undirected_edge("B", "C")
    #graph.add_undirected_edge("B", "G")
    #graph.add_undirected_edge("F", "C")
    #graph.add_undirected_edge("F", "G")
    #graph.add_undirected_edge("C", "G")
    #graph.add_undirected_edge("D", "G")
    #graph.add_undirected_edge("E", "G")
    #graph.add_undirected_edge("E", "D")
    #graph.add_undirected_edge("E", "F")
    i = 0;
    print("How many relations you want to enter?")
    z = int(input("Amount of relation:"))
    while(i!=z):
        x = input("Enter the first city")
        y = input("Enter the second city")
        graph.add_undirected_edge(x,y)
        i = i + 1


    graph.visualize_w_color()



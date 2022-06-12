import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    NumberOfIteration = 0
    chosenColors = {}

    def __init__(self, tempNumberOfIteratıon, tempChosenColors):
        self.NumberOfIteration = tempNumberOfIteratıon
        self.chosenColors = tempChosenColors
        self.creating_nodes()

    def colorize(graph: nx.Graph, NumberOfIteration, chosenColors):
        my_node_list = []
        for node in graph:
            my_node_list.append(node)

        color_dict = {}
        for node in my_node_list:
            color_dict[node] = set(chosenColors)

        the_solution = {}
        sorted_node = sorted(graph.degree, key=lambda x: x[1], reverse=True)

        keyCheck = []
        tempListColor = []
        for t in range(len(sorted_node)):
            tempListColor.append("null")
        nx.draw(graph, with_labels=True, font_weight='bold', node_color="gray", node_size=1500)
        plt.show(block=False)
        plt.pause(2)
        plt.close()
        counter = 0
        for n in sorted_node:
            set_the_color = list(color_dict[n[0]])
            try:
                the_solution[n[0]] = set_the_color[0]
            except:
                print("ERROR: Colors conflicted!")
                input()
            adjacent_node = graph[n[0]]
            adjacent_node_list = list(adjacent_node)
            for j in range(len(adjacent_node)):
                if set_the_color[0] in color_dict[adjacent_node_list[j]]:
                    color_dict[adjacent_node_list[j]].remove(set_the_color[0])
            print("Iteration: ", counter)
            print(color_dict.items())
            print(set_the_color)
            counter2 = 0
            del tempListColor[:]
            del keyCheck[:]
            for key, values in color_dict.items():
                for v in values:
                    if key in keyCheck:
                        continue
                    else:
                        tempListColor.append(v)

                        print("this temp list: ", tempListColor)
                        keyCheck.append(key)
                counter2 = counter2 + 1
            print(tempListColor)
            if counter == int(NumberOfIteration) - 1:
                nx.draw(graph, with_labels=True, font_weight='bold', node_color=tempListColor, node_size=1500)
                plt.show()
                break
            try:
                nx.draw(graph, with_labels=True, font_weight='bold', node_color=tempListColor, node_size=1500)
            except:
                print("ERROR: Not enough color!")
            plt.show(block=False)
            plt.pause(2)
            plt.close()
            counter = counter + 1

    def creating_nodes(self):
        G = nx.Graph()
        edge_list = []

        with open("text.txt") as f:
            edge_list = [i.strip().split("->") for i in f.readlines()]
        G.add_edges_from(edge_list)
        node_list = G.nodes()
        Graph.colorize(G, self.NumberOfIteration, self.chosenColors)

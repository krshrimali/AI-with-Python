import matplotlib.pyplot as plt
import random
x = []
y = []

graph = { "A": 3, "B": 2 }
random.seed(100)

def draw_graph(graph):
    char_ = 0
    for i in graph.keys():
        # char_ = 1
        # print(i)
        coord_x = random.randint(1, 10)
        coord_y = random.randint(1, 10)
        for j in range(graph[i]):
            char_ += 1
            # print(j)
            coord_x = coord_x + random.randint(1, 10)
            coord_y = coord_y + random.randint(1, 10)
            x.append(coord_x)
            y.append(coord_y)
            plt.plot(x, y)
            plt.annotate(char_, xy=(coord_x, coord_y), xytext=(coord_x, coord_y + 0.5))
        # print(x, y)
    plt.show()

graph["C"] = 4
graph["D"] = 5
print(graph)
draw_graph(graph)

class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, id):
        return self.edges[id]
    
exampleGraph = SimpleGraph()
exampleGraph.edges = {
    'A' : ['B'],
    'B' : ['A', 'C', 'D'],
    'C' : ['A'],
    'D' : ['E' , 'A'],
    'E' : ['B']
}

print(exampleGraph.neighbors('A'))

import collections
# from implementation import *

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()

def breadth_first_search(graph, start):
    frontier = Queue()
    frontier.put(start)
    
    visited = {}
    visited[start] = True
    
    while not frontier.empty():
        current = frontier.get()
        print("Visiting: %r" % current)
        for next in graph.neighbors(current):
          if next not in visited:
            frontier.put(next)
            visited[next] = True

breadth_first_search(exampleGraph, 'A')

class Square_Grid:
    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x+y) % 2 == 0: results.reverse() #aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results


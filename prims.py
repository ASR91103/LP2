import heapq

class Graph:
    def __init__(self):
        self.graph={}

    def add_edge(self,u,v,weight):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append((v,weight))
        self.graph[v].append((u,weight))
        
    def prims_mst(self):
        mst=[]
        visited=set()
        vertex=list(self.graph.keys())[0]
        heap=[(0,vertex)]

        while heap:
            weight, vertex=heapq.heappop(heap)
            if vertex not in visited:
                visited.add(vertex)
                mst.append((weight,vertex))

            for neighbor,neighbor_weight in self.graph[vertex]:
                if neighbor not in visited:
                    heapq.heappush(heap,(neighbor_weight,neighbor))

        return mst

def main():
    g=Graph()
    edges=int(input("Enter the total no of edges in the graph: "))
    print("Enter the edges in the format of start, end, weight")

    for i in range(edges):
        start,end,weight=input().split()
        weight=int(weight)
        g.add_edge(start,end,weight)

    mst=g.prims_mst()
    for weight, vertex in mst:
        print(vertex,'-',weight)

if __name__=='__main__':
    main()
    
        
            

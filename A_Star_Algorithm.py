class A_star_Graph:
    def __init__(self,a_list) :
        self.a_list = a_list
        self.H = {}
    def connections(self,c):
        return self.a_list[c]
    def heur (self,H):
        self.H = H
    def h(self,i):
        return self.H[i]
    def a_star(self,start_node,end_node):
        open = set([start_node])
        closed = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node

        while len(open) > 0:
            n = None

            for  i in open:
                if n == None or g[i]+self.h(i) < g[n] + self.h(n):
                    n = i
            if n == None:
                print("The Path doesn't exist")
            if n == end_node:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                path.append(start_node)
                path.reverse()

                return path,g[end_node]
            for (v, weight) in self.connections(n):
                if v not in open and v not in closed:
                    open.add(v)
                    parents[v] = n
                    g[v] = g[n] + weight
                else:
                    if g[v] > g[n] + weight:
                        g[v] = g[n] + weight
                        parents[v] = n

                        if v in closed:
                            closed.remove(v)
                            open.add(v)
            open.remove(n)
            closed.add(n)
        return None




input = open("F:\CSE 422\LAB 1_A-Star\input.txt",'r') 
line = []
a_list = {}
H = {}
line = input.readline().split()
while line != []:
    
    a_list[line[0]] = []
    i = 0

    while i <= len(line):
        H[line[0]] = int(line[1])
        try:
            a_list[line[0]].append((line[i+2],int(line[i+3])))
            i = i +2
        except IndexError:
            break
    line = input.readline().split()

# print(a_list)
# print(H)
result = A_star_Graph(a_list)
result.heur(H)
result  = result.a_star('Arad','Bucharest')
print(" Path : ",result[0][0],end = " ")
for i in result[0]:
    if i != result[0][0]:
        print('->',i,end=" ")
print("\n")
print(" Total distance: ",result[1],' km ')
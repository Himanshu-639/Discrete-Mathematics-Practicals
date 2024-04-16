#Ques.6
#Write a program to check if a given graph is a complete graph. Represent the graph using the Adjacency Matrix representation.


import sys

#Taking Input
vertices=int(input("Enter the number of vertices in the graph : "))
nedges=int(input("Enter the number of edges in the graph : "))
E=[]
for i in range (nedges):
    ed=eval(input(f"Enter the vertices of edge {i+1} : "))
    assert len(ed)==2, "Enter only both initial and terminating vertces."
    assert ed[0]>0 and ed[1]>0, "The value of vertices cannot be negative."
    assert ed[0]<=vertices and ed[1]<=vertices, f"The value of vertices cannot be more than {vertices}."
    ed=list(ed)
    if ed not in E:
        E.append(ed)
    else:
        sys.exit(f"Vertices {ed} already entered.")
print(f"\nThe vertices entered by you are {E}")


#Creating a null matrix
adj_graph=[]
for i in range (vertices):
    rows=[]
    for j in range (vertices):
        rows.append(0)
    adj_graph.append(rows)


#Feeding 1 if there exist a relation
mrows=len(adj_graph)+1
mcols=len(adj_graph[0])+1
for i in range (mrows):
    for j in range (mcols):
        if [i,j] in E:
            adj_graph[i-1][j-1]=adj_graph[j-1][i-1]=1


#Printing the Adjacency matrix
print("The matrix Adjacency matrix formed is : ")
for row in adj_graph:
    print(f"\t{row}")


#Function for checking the graph if it is complete by number of vertices and edges
def check_c_graph(edge,vertices):
    #vert=int(input("Enter the number of vertices : "))
    edges=((vertices)*(vertices-1))/2
    print(edges)
    if len(edge)==edges:
        print("It is a complete graph.")


#Function for checking the graph if it is complete by checking existance of edges
def check_complete_g(adj_graph):
    for i in range (len(adj_graph)):
        for j in range (len(adj_graph)):
            if i<j:
                if adj_graph[i][j]==0:
                    return "It is not a complete graph."
    return "It is a complete graph."


#Calling functions
print(check_c_graph(E, vertices))    
print(check_complete_g(adj_graph))
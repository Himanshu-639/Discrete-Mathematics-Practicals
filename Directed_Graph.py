#Ques.7
#Write a program to accept a directed graph G and compute the in-degree and out-degree of each vertices

import sys

#Taking Input
vertices=int(input("Enter the number of vertices in the graph : "))
nedges=int(input("Enter the number of edges in the graph : "))
E=[]
for i in range (nedges):
    ed=eval(input(f"Enter the vertices of edge {i+1} : "))
    assert len(ed)==2, "Enter only both initial and terminating vertices."
    assert ed[0]>0 and ed[1]>0, "The values of vertices cannot be negative."
    assert ed[0]<=vertices and ed[1]<=vertices, f"The values of vertices cannot be more than {vertices}."
    ed=list(ed)
    if ed not in E:
        E.append(ed)
    else:
        sys.exit(f"The {ed} already entered.")
print(f"\nThe vertices entered by you are : {E}")


#Creating a null matrix
adj_graph=[]
for i in range (vertices):
    rows=[]
    for j in range (vertices):
        rows.append(0)
    adj_graph.append(rows)


#Feeding the values if there exist a relation
for i in range (len(adj_graph)+1):
    for j in range (len(adj_graph[0])+1):
        if [i,j] in E:
            adj_graph[i-1][j-1]=1


#Printing the Adjacency matrix formed for the relation
print("\nThe adjacency matrix of the graph is : ")
outdegree=[]
for row in adj_graph:
    print(f"\t{row}")
    outdegree.append(row.count(1))


#Calculating the in-degree of each vertices by transposing the matrix
indegree=[]
for i in range (len(adj_graph)):
    cols=[]
    for j in range (len(adj_graph[0])):
        element=adj_graph[j][i]
        cols.append(element)
    indegree.append(cols.count(1))


#Printing the in-degree of each vertices
print("\nIn-degree of each verices.")
for l in range(len(adj_graph)):
    print(f"The in-degree of {l+1} is {indegree[l]}.")


#Printing the out-degree of each vertices
print("\nOut-degree of each vertices.")
for k in range(len(adj_graph)):
    print(f"The out-degree of {k+1} is {outdegree[k]}.")
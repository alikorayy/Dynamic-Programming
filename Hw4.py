#While designing my code I utilized from this website: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
import sys
import random

#if there is no  edge between 2 vertices, take weight as INF 
INF= 9999

def printMatrix(m):
    len_mat=len(m[0])
    for i in range(len_mat):
        printing_row=""
        for k in range(len_mat):
            if m[i][k] != INF:  
                printing_row+= ("%5d" % m[i][k])
            elif m[i][k] == INF:
                printing_row += ("%5s" % "INF")
                
        print(printing_row)
        
def floyd_Warshall_Algorithm(m,first_city,target_bus,target_train,target_city):
    len_mat=len(m[0])
    dist_mat = list(map(lambda i: list(map(lambda j: j, i)), m))
    inter_bus=""
    inter_train=""
    inter_city=""
    transport_vehicle=""
    for k in range(len_mat):
 
        # pick all vertices as source one by one
        for i in range(len_mat):
 
            # Pick all vertices as destination for the
            # above picked source
            for j in range(len_mat):
 
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                if dist_mat[i][k]!=-1 and dist_mat[k][j]!=-1:
                    #print(dist_mat[i][k],dist_mat[k][j])
                    if dist_mat[i][j]!=-1:
                        x= dist_mat[i][j]
                        if i==first_city and j == target_train:
                            sum_inter=dist_mat[i][k]+dist_mat[k][j]
                            if sum_inter < dist_mat[i][j]:
                                inter_train=str(k)
                        elif i==first_city and j == target_bus:
                            sum_inter=dist_mat[i][k]+dist_mat[k][j]
                            if sum_inter < dist_mat[i][j]:
                                inter_bus=str(k)
                        dist_mat[i][j] = min(dist_mat[i][j],dist_mat[i][k] + dist_mat[k][j])
                        x= dist_mat[i][j]
                        

        print("---------------------------------------------------------------------")
        print("the matrix for intermediate",k)
        printMatrix(dist_mat)
    print ("The  matrix which represents the shortest distance between every pair of vertices is: ")
    printMatrix(dist_mat)
    if len_mat == 0:
        print("Empty Matrix")
    elif dist_mat[first_city][target_bus]== INF and dist_mat[first_city][target_train]==INF:
        print("There is no path from direct city to target city")
    else:
        if dist_mat[first_city][target_bus]!=-1 and dist_mat[first_city][target_train]!=-1: #if  the target city have both train and bus station
            if dist_mat[first_city][target_bus]<= dist_mat[first_city][target_train]:# if the bus station of the city is closer than train station
                transport_vehicle="Bus"
                inter_city=inter_bus
                total_time= int(dist_mat[first_city][target_bus])
            elif dist_mat[first_city][target_bus]> dist_mat[first_city][target_train]: # if the train station is closer
                transport_vehicle="Train"
                inter_city=inter_train
                total_time= int(dist_mat[first_city][target_train])
        else: # if the target city doesnt have Train OR Bus Station
            if dist_mat[first_city][target_bus]==-1: #if the target city doesnt have bus station
                transport_vehicle="Train"
                inter_city=inter_train
                total_time= int(dist_mat[first_city][target_train])
            elif dist_mat[first_city][target_train]==-1: #if the target city doesnt have train station
                transport_vehicle="Bus"
                inter_city=inter_bus
                total_time= int(dist_mat[first_city][target_bus])
        real_target_city=(target_city//2)+1
        print("Starting from the İstanbul-Harem Bus Station, to go to the ",real_target_city ," th city in a quickest way you should follow the following rotation: ")
        if inter_city != "": # if any intermediate city is used 
            inter_real_city=int(inter_city)//2
            inter_real_city+=1
            print("İstanbul-Harem Bus Station --> ",inter_city,"th intermediate path in matrix -->",transport_vehicle," station of ",real_target_city,"th city")
            print("The total time will be ",total_time)
        elif inter_city == "":  # if any intermediate city is not used 
            print("İstanbul-Harem Bus Station --> ",transport_vehicle," station of ",real_target_city,"target city")
            print("The total time will be ",total_time)
      
        


#path_matrix=          [[0, 5, 120,  45], 
#                     [34, 0, INF, 75],
#                      [56, INF, 450, 87],
#                      [34, 2, 21, 0]] 


#path_matrix =          [[0, 20, 35,  45],
#                       [30, 0, 10, 9],
#                       [50, 10, 0, 80],
#                       [34, 7, 19, 0]]        

#path_matrix=        [[0, 30, -1, 3, 30, 42, -1, 9],
                     #[2, 0, -1, 12, 8, 4, -1, 12],       #IF THE CITY DOES NOT HAVE AN BUS/TRAIN STATION PUT ITS VALUE AS -1
                     #[-1, -1, -1, -1, -1, -1, -1, -1],
                     #[8, 15, -1, 0, 3, 7, -1, 19],
                     #[5, 19, -1, 1, 0, 12, -1, 5],
                     #[5, 15, -1, 7, 12, 0, -1, 16],
                     #[-1, -1, -1, -1, -1, -1, -1, -1],
                     #[6, 9, -1, 15, 17, 19,-1, 0]
                     #]
            #   A   A   B   B   C   C   D   D   E   E   F   F   G   G
path_matrix1 = [
              [0  ,5  ,20 ,INF,INF,-1 ,INF,-1 ,-1 ,INF,INF,INF,INF,INF], # A       #TESTMATRIX 1
              [5  ,0  ,INF,10 ,INF,-1 ,INF,-1 ,-1 ,20 ,INF,INF,INF,INF], # A 
              [20 ,INF,0  ,10 ,20 ,-1 ,INF,-1 ,-1 ,INF,40 ,INF,INF,INF], # B
              [INF,10 ,10 ,0  ,INF,-1 ,INF,-1 ,-1 ,5  ,INF,INF,INF,INF], # B
              [INF,INF,20 ,INF,0  ,-1 ,15 ,-1 ,-1 ,INF,INF,INF,INF,INF], # C
              [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ], # C
              [INF,INF,INF,INF,15 ,-1 ,0  ,-1 ,-1 ,INF,INF,INF,10 ,INF], # D
              [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ], # D
              [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ], # E
              [INF,20 ,INF,5  ,INF,-1 ,INF,-1 ,-1 ,0  ,INF,10 ,INF,INF], # E
              [INF,INF,40 ,INF,INF,-1 ,INF,-1 ,-1 ,INF,0  ,10 ,10 ,INF], # F
              [INF,INF,INF,INF,INF,-1 ,INF,-1 ,-1 ,10 ,10 ,0  ,INF,30 ], # F
              [INF,INF,INF,INF,INF,-1 ,10 ,-1 ,-1 ,INF,10 ,INF,0  ,5  ], # G
              [INF,INF,INF,INF,INF,-1 ,INF,-1 ,-1 ,INF,INF,30 ,5  ,0  ]] # G
           #   A   A   B   B   C   C   D   D   E   E

            #   A   A   B   B   C   C   D   D   E   E   F   F
path_matrix2 = [
              [INF,5  ,40 ,INF,INF,INF,-1 ,INF,INF,-1 ,INF,INF], # A
              [5  ,INF,INF,INF,INF,10 ,-1 ,INF,INF,-1 ,INF,INF], # A 
              [40 ,INF,INF,5  ,5  ,INF,-1 ,INF,INF,-1 ,INF,INF], # B
              [INF,INF,5  ,INF,INF,INF,-1 ,5  ,INF,-1 ,INF,INF], # B
              [INF,INF,5  ,INF,INF,25 ,-1 ,INF,5  ,-1 ,INF,INF], # C
              [INF,10 ,INF,INF,25 ,INF,-1 ,5  ,INF,-1 ,INF,INF], # C
              [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ], # D
              [INF,INF,INF,5  ,INF,5  ,-1 ,INF,INF,-1 ,INF,40 ], # D
              [INF,INF,INF,INF,5  ,INF,-1 ,INF,INF,-1 ,5  ,INF], # E
              [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ], # E
              [INF,INF,INF,INF,INF,INF,-1 ,INF,5  ,-1 ,INF,10 ], # F
              [INF,INF,INF,INF,INF,INF,-1 ,40 ,INF,-1 ,10 ,INF]] # F

            #   A   A   B   B   C   C   D   D   E   E   
path_matrix3 =[
              [INF,5  ,30 ,-1 ,30 ,INF,INF,-1 ,-1 ,INF], # A
              [5  ,INF,INF,-1 ,INF,20 ,INF,-1 ,-1 ,75 ], # A 
              [30 ,INF,INF,-1 ,20 ,INF,22 ,-1 ,-1 ,INF], # B
              [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ], # B
              [30 ,INF,20 ,-1 ,INF,10 ,20 ,-1 ,-1 ,INF], # C
              [INF,20 ,INF,-1 ,10 ,INF,INF,-1 ,-1 ,40 ], # C
              [INF,INF,22 ,-1 ,20 ,INF,INF,-1 ,-1 ,INF], # D
              [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ], # D
              [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ], # E
              [INF,75 ,INF,-1 ,INF,40 ,INF,-1 ,-1 ,INF]] # E

            #   A   A   B   B   C   C   D   D   E   E   F   F
path_matrix = [
              [INF,-1 ,INF,INF,23 ,-1 ,27 ,INF,INF,INF,-1 ,INF], # A
              [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ], # A 
              [INF,-1 ,INF,4  ,18 ,-1 ,13 ,INF,INF,INF,-1 ,INF], # B
              [INF,-1 ,4  ,INF,INF,-1 ,INF,INF,INF,INF,-1 ,11 ], # B
              [23 ,-1 ,18 ,INF,INF,-1 ,INF,INF,17 ,INF,-1 ,INF], # C
              [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ], # C
              [27 ,-1 ,13 ,INF,INF,-1 ,INF,7  ,20 ,INF,-1 ,INF], # D
              [INF,-1 ,INF,INF,INF,-1 ,7  ,INF,INF,12 ,-1 ,22 ], # D
              [INF,-1 ,INF,INF,17 ,-1 ,20 ,INF,INF,8  ,-1 ,INF], # E
              [INF,-1 ,INF,INF,INF,-1 ,INF,12 ,8  ,INF,-1 ,17 ], # E
              [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ], # F
              [INF,-1 ,INF,11 ,INF,-1 ,INF,22 ,INF,17 ,-1 ,INF]] # F
#path_matrix = [[0, 0, 0, 0, 0, 0],
#                       [0, 0, 0, 0, 0, 0],
#                       [0, 0, 0, 0, 0, 0],
#                       [0, 0, 0, 0, 0, 0],
#                       [0, 0, 0, 0, 0, 0],
#                      [0, 0, 0, 0, 0, 0]
#                       ]

#path_matrix =           [[INF, INF, INF, INF, INF, INF],
#                      [INF, INF, INF, INF, INF, INF],
#                       [INF, INF, INF, INF, INF, INF],
#                       [INF, INF, INF, INF, INF, INF],
#                      [INF, INF, INF, INF, INF, INF],
#                       [INF, INF, INF, INF, INF, INF]
#                      ]

#path_matrix = [[0, 30], 
 #             [7, 0]]

#path_matrix = [[random.randint(1, 50) for i in range(
#         8)] for j in range(8)]

for i in range(len(path_matrix[0])):
    if path_matrix[i][i] != 0:
        if path_matrix[i][i]!=-1:
            path_matrix[i][i]=0

started_city= 0 #my started city is always  at 0 index
num_of_cities= int(len(path_matrix[0])/2)
print(num_of_cities)
target_city=int(len(path_matrix[0])//2) #my target city is always located in the upper middle of matrix
if num_of_cities %2 ==0: #if the city size is even, arrange the target city index as below 
    target_bus_station_index= target_city
    target_train_station_index= target_city+1
else: #if the city size is odd, arrange the target city index as below
    target_bus_station_index= target_city-1
    target_train_station_index= target_city
print("Initial Matrix")
printMatrix(path_matrix)
floyd_Warshall_Algorithm(
        path_matrix,started_city,target_bus_station_index,target_train_station_index,target_city)
#While designing my code I utilized from this website: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
import random
import sys
import matplotlib.pyplot as plt
import time

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
                        

        #print("---------------------------------------------------------------------")
        #print("the matrix for intermediate",k)
        #printMatrix(dist_mat)
    print ("The  matrix which represents the shortest distance between every pair of vertices is: ")
    printMatrix(dist_mat)
    if len_mat == 0:
        print("Empty Matrix")
    elif dist_mat[first_city][target_bus]== INF and dist_mat[first_city][target_train]==INF:
        print("There is no path from direct city to target city")
    else:
        if dist_mat[first_city][target_bus]!=-1 and dist_mat[first_city][target_train]!=-1: #if  the target city have both train and bus station
            if dist_mat[first_city][target_bus]<= dist_mat[first_city][target_train]: # if the bus station of the city is closer than train station 
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
        elif inter_city == "":  #if any intermediate city is not used
            print("İstanbul-Harem Bus Station --> ",transport_vehicle," station of ",real_target_city,"target city")
            print("The total time will be ",total_time)
      
        


#path_matrix=         # [[0, 5, 120,  45], 
                      #[34, 0, INF, 75],
                      #[56, INF, 450, 87],
                      #[34, 2, 21, 0]]      
city_count=[10,20,25,30,40,50]
running_time_cities=[]
for i in city_count:
    vertices_count=2*i

#fill the matrix with random values
    path_matrix= [[random.randint(1, 50) for i in range(
                vertices_count)] for j in range(vertices_count)]

    # put 0 values for the diagonals of the matrix
    for i in range(len(path_matrix[0])):
        if path_matrix[i][i] != 0:
            if path_matrix[i][i]!=-1:
                path_matrix[i][i]=0

    started_city= 0  #my started city is always  at 0 index
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
    #print(path_matrix)
    printMatrix(path_matrix)
    start_time= time.time()
    floyd_Warshall_Algorithm(
            path_matrix,started_city,target_bus_station_index,target_train_station_index,target_city)
    end_time= time.time()
    total_running_time= end_time-start_time
    running_time_cities.append(total_running_time)
plt.plot(city_count, running_time_cities, linewidth=3.0)
plt.xlabel('Number of Cities')
plt.ylabel('runtimes Dynamic Programming Algorithm')
plt.show()
#Literal 1
# bubble sort to order (vn/wn) nondecreasingly and vn and wn  
def bubbleSort(list1, list2, list3):
    n = len(list1)
    for i in range(n):
        for j in range(0, n-i-1):
            if list1[j] < list1[j+1] :
                list1[j], list1[j+1] = list1[j+1], list1[j]
                list2[j], list2[j+1] = list2[j+1], list2[j]
                list3[j], list3[j+1] = list3[j+1], list3[j]
    return list1, list2, list3

#greedy algorithm taking k elements 
def knapSack(Weight, wn_list, vn_list, n):
    
    K = [[0 for x in range(Weight + 1)] for x in range(n+1)]    #initializing matrix
    
    for i in range(n+1):
        for w in range(Weight+1):
            if i==0 or w==0:    #put 0 to the first row and col of K
                K[i][w] = 0
            elif wn_list[i-1] <= w:
                K[i][w] = max(vn_list[i-1] + K[i-1][w-wn_list[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    chosen_values = []  #to get the objects
    i = n; j = Weight
    while i > 0 and j > 0:
        if K[i][j] != K[i-1][j]:    # ith element
            chosen_values.append((vn_list[i-1],wn_list[i-1]))   #add ith element with its weight
            j -= wn_list[i-1]   # previous possible weight (j)
            i -= 1              #previous row
        else:
            i -= 1
    
    return K[n][Weight], chosen_values  #max value possible

# c) knapsack problem with 0 <= x <= 1
def knapSack_2(Weight, wn_list, vn_list, n):
        
    K = [0 for x in range(n)]   # array to store the fraction of items
    weight_2 = 0

    for i in range(n):  
        if weight_2 + wn_list[i] <= Weight:    #chose first weight if < max_weight
            K[i] = 1
            weight_2 += wn_list[i]
        else:
            K[i] = (Weight - weight_2)/wn_list[i]   #create 0 <= x <= 1
            weight_2 = Weight
            break
    result = [ x * y for x,y in zip(K, vn_list )]   #create the vector x of 
    return K ,sum(x for x in result)
    


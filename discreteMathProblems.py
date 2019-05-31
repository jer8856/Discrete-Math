from math import ceil, fabs, cos, sin
import function

#literal 1

N = 300
W = 1000
V = 10

''' a) Use a sorting algorithm to reorder the objects such that vn/wn is monotonically nonincreasing.'''

value_per_weight = []   #list of values/weights
wn_list = []    #lists of weights
vn_list = []    #lists of values

for i in range(N):

    wn = ceil(0.1*(W)*fabs(cos(i)))     #create wni
    vn = ceil(V*fabs(sin(i)))           #create vni

    wn_list.append(wn)     
    vn_list.append(vn)     
    value_per_weight.append([vn/wn,wn_list[i]])     #append the to the list (v/n, weight)

#order the lists of weights and values in the same as the list of vn/wn 
value_per_weight, wn_list, vn_list = function.bubbleSort(value_per_weight,wn_list,vn_list)

# print(vn_list,"\n",wn_list,"\n",value_per_weight ) # to print the different lists

''' b)greedy algorithm of taking the first k objects s.t. the sum of the weights <= W
but adding the k + 1st object would exceed the weight limit.'''

max_value, chosen_values = function.knapSack(W, wn_list, vn_list,N)
# print("The maximum value is:",max_value,'\nAnd the chosen (values,weights) are:', chosen_values)
print("The maximum value with x{0,1} is: ",max_value)


''' c) Derive from the solution of b. the solution of the LOP relaxation, where x{0,1} is
replaced by 0 ≤ xn ≤ 1.'''

fraction_values, max_value = function.knapSack_2(W,wn_list,vn_list,N)
# print("The maximum value is: ",max_value,"and the vector of fraction values is: ",fraction_values,"'\nThe vector of values is:",vn_list)
print("The maximum value with 0 <= x <= 1 is: ",max_value)
def insertionsort(a):
    
    for i in range(1, len(a)): ##traversal starts from 1 to lenght of an input array
        pivot = a[i] ##second element in the array was stored in pivot variable 
    
    ##hence inorder to sort the array from first element store that in the variable j 
    
        j = i - 1
    
    ##comparision of the two seqential elements 
    
        while j >= 0 and pivot < a[j] :
            a[j+1] = a[j]
            j=j-1
        a[j+1] = pivot
    
    ##sorted array with O(N2) complexity 
    

a = [10,15,7,2,9]
##calling the sort function 
insertionsort(a)
for i in range(len(a)): ## retriving each element from the sorted array and then printing one by one 
    print("%d" %a[i])
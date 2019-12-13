

# Sajad Gholamzadehrizi
# CSC 220 Algorithms
import time
import numpy as np
import random

def insertion_sort(array):
    s = time.time()         # saving start time to avoid a long running time by throwing an exception
    i = 1
    while i < len(array):   # loop untill i is less than length of array
        val = array[i]      # key is selected at index i
        j = i-1             
        while j >=0 and val < array[j] :  # looping from index i-1 to 0  
                array[j+1] = array[j]     # bring the lowest element to its place 
                j -= 1
        array[j+1] = val    # settig the element at its correct place after findig actual j index
        if time.time() - s > 30:    # raising exception if execution time exceeded 30 seconds
            raise Exception('Time taken by insertion sort more than 30 seconds so aborted')
        i+=1
    

def merge(arr, l, m, r): 
    l = int(l)
    m = int(m)
    r = int(r)
    n1 = int(m - l + 1)
    n2 = int(r- m) 
  
    Left = [0] * (n1)          # creatig empty array of size n1
    Right = [0] * (n2)          # creatig empty array of size n2 
  
    # copying elements on left side to left array
    for i in range(0 , n1): 
        Left[i] = arr[l + i] 
  
    # copying elements on left side to right arry
    for j in range(0 , n2): 
        Right[j] = arr[m + 1 + j] 
  
    
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if Left[i] <= Right[j]: 
            arr[k] = Left[i] 
            i += 1
        else: 
            arr[k] = Right[j] 
            j += 1
        k += 1

    while i < n1: 
        arr[k] = Left[i] 
        i += 1
        k += 1

    while j < n2: 
        arr[k] = Right[j] 
        j += 1
        k += 1

def merge_sort(array,left,right): 
    if left < right: 
        m = (left+(right-1))/2         # finding the index about which array is split
        merge_sort(array, left, m)   # solving the split array from l to m first
        merge_sort(array, m+1, right) # solving the split arrayy from m+1 to r secondly
        merge(array, left, m, right)     # merging the sorted left and right subarray efficiently

def heapify(arr, size, i): 
    largest = i  # Initialize largest as root 
    left = 2 * i + 1     # left child of parent i 
    right = 2 * i + 2     # right child of parent i
  
    
    if left < size and arr[i] < arr[left]:  # if left child exists and is less than parent i
        largest = left                      # set largest as left
  
    if right < size and arr[largest] < arr[right]:  # if right child exists and is less than parent i
        largest = right                             # set largest as right
  
    if largest != i:    # swap the largest with i and recursively call heapify at largest down the heap
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root. 
        heapify(arr, size, largest) 

def heap_sort(arr):
    i = len(arr) 
    while i >=0:
        heapify(arr, len(arr) , i)      # building the heap
        i-=1
     
    i=len(arr) -1       # starting loop with i as len(arr) -1 
    while i>=1:         # while i is greater than equal to 1
        swap(arr,i,0)               # swap i and 0 indexed elements of array named arr
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0)
        i-=1
        
def swap(A,i,k):        # swap element at index i and k
    A[i],A[k] = A[k],A[i]

def partition(array,start,end):    # selecting last element as pivot
    i = ( start-1 )         # index to keep track of partition index
    pivot = array[end]     # pivot selected as last element
    j = start
    while j < end:          # loop from low to high
        if   array[j] <= pivot:   # partition by keeping elements lower than pivot to its left              
            i = i+1 
            array[i],array[j] = array[j],array[i]   # swapping
        j+=1
    array[i+1],array[end] = array[end],array[i+1] 
    return ( i+1 )      # return the index about which partition happens finally  

def quick_sort_pivot_last(arr,start,end): 
    s = time.time()
    if start < end:                                 # solve until start is less than end
        partition_index = partition(arr,start,end)  # find the partiton element index
        quick_sort_pivot_last(arr, start, partition_index-1)    # recurse with left subarray
        quick_sort_pivot_last(arr, partition_index+1, end)      # recurse with right subarray
    if time.time() - s > 30:    # raising exception if execution time exceeded 30 seconds
        raise Exception('Time taken by quick sort (last pivot) more than 30 seconds so aborted')

def partition_random(array, low, high):
    r = random.randrange(low,high)      # selecting a random element as pivot
    array[r],array[high] = array[high],array[r] # swapping with the last element
    return partition(array, low, high)  # moving forward with our partition() method for last pivot

def quick_sort_random_pivot(arr,start,end):
    s = time.time()
    if start < end:                              #solve until start is less than end
        pi = partition_random(arr,start,end)     #partition the array
        quick_sort_random_pivot(arr, start, pi-1)   #recursively solve left subarray of pivot
        quick_sort_random_pivot(arr, pi+1, end)  #recursively solve right subarray of pivot
    if time.time() - s > 30:    # raising exception if execution time exceeded 30 seconds
        raise Exception('Time taken by quick sort (last pivot) more than 30 seconds so aborted')


def outputRunTime(total, name):
    if total >= 1:
        print('Running time of ', name, ' \t {:.5f}'.format(total), 'seconds')
    else:
        print('Running time of ', name, ' \t {:.5f}'.format(total*1000), 'milliseconds')


if __name__ == '__main__':
    # sizes = [10,100,1000,10000,100000,1000000]  # sizes on which testing is done
    total = 0
    print('\n')
    while(True):
        s = int(input('Enter the input size of array\t'))
        arr = list(np.random.randint(100000,size=(s)))

        try:
            start_time = time.time()
            insertion_sort(arr)
            end_time = time.time()
            total = (time.time() - start_time)
            outputRunTime(total, "insertion sort")
        except:
            print('Running time of insertion sort exceeds 30 seconds so aborted')
            
        arr = list(np.random.randint(100000,size=(s)))
        start_time = time.time()
        merge_sort(arr,0,s-1)
        total = (time.time() - start_time)
        outputRunTime(total, "merge sort\t")

        arr = list(np.random.randint(100000,size=(s)))
        start_time = time.time()
        heap_sort(arr)
        total = (time.time() - start_time)
        outputRunTime(total, "heap sort\t")

        arr = list(np.random.randint(100000,size=(s)))
        start_time = time.time()
        try:
            quick_sort_pivot_last(arr,0,s-1)
            total = (time.time() - start_time)
            outputRunTime(total, "quickSort_last")
        except:
            print('Running time of quickSort_last exceeds 30 seconds so aborted')

        arr = list(np.random.randint(100000,size=(s)))
        start_time = time.time()
        try:
            quick_sort_random_pivot(arr,0,s-1)
            total = (time.time() - start_time)
            outputRunTime(total, "quickSort_random")
        except:
            print('Running time of quickSort_random exceeds 30 seconds so aborted')

        if s <= 100:
            print('\n',arr)

        print('\n')
        
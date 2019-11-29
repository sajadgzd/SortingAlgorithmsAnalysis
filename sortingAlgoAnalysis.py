import time
import numpy as np

def insertion_sort(array):
    s = time.time()         # notinng the start time to avoid endless running of loop
    i = 1
    while i < len(array):   # loop untill i is less than length of array
        val = array[i]      # key is selected at index i
        j = i-1             
        while j >=0 and val < array[j] :  # looping from index i-1 to 0  
                array[j+1] = array[j]     # brig the lowest element to it place 
                j -= 1
        array[j+1] = val    # settig the element at its correct place after findig actual j index
        if time.time() - s > 30:    # raising exception if execution time exceeded 30 seconds
            raise Exception('Time taken by insertion sort more than 10 seconds so aborted')
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
        heapify(arr, len(arr) , i)      # bilding te heap
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
    if start < end:                                 # solve until start is less than end
        partition_index = partition(arr,start,end)  # find the partiton element index
        quick_sort_pivot_last(arr, start, partition_index-1)    # recurse with left subarray
        quick_sort_pivot_last(arr, partition_index+1, end)      # recurse with right subarray
      
def partition_random(array,low,high):   # selecting a random index as pivot
    index = np.random.randint(low,high)     # fiding a random index between low and high
    array[low],array[index] = array[index],array[low]   # swapping the index element with element at low
    pivot = low # pivot set at low     
    i = low + 1 # the index where the partition happens  
    j = low+1
    while j < high +1:                  # elements lower than element at pivot are at left of i
                                        # and elements higher are at right of i(partition). 
        if array[j] <= array[pivot]: 
            array[i] , array[j] = array[j] , array[i] 
            i = i + 1
        j+=1
    array[pivot] , array[i - 1] = array[i - 1] , array[pivot]   # swapping pivot element with (i-1) element
    
    return (i-1)    # returning the index where partition happened

def quick_sort_random_pivot(arr,start,end):
    
    if start < end:                              #solve until start is less than end
        pi = partition_random(arr,start,end)     #partition the array
        quick_sort_random_pivot(arr, start, pi-1)   #recursively solve left subarray of pivot
        quick_sort_random_pivot(arr, pi+1, end)  #recursively solve right subarray of pivot
        



if __name__ == '__main__':
    sizes = [10,100,1000,10000,100000,1000000]  # sizes on which testing is done
    
    #while True:
    s = int(input('Enter the input size of array\t'))
    inp = list(np.random.randint(100000,size=(s)))  # random list of size s created between 
                                                    # 1 to 100000
    flag = 0                                    # flag to check if any exception occured or not
    start_time = time.time()
    try:
        if s <= 1000:    # for sizes 10,100 and 1000 , sorting array for
                                                # 100 or 1000 times and then taking average
                                                # to prevent 0.0 execution time recording in python
            total = 0
            if s==10:
                for i in range(1000):
                    inp = list(np.random.randint(100000,size=(s)))
                    insertion_sort(inp)
                total = (time.time() - start_time)/1000.0
                print('Execution time of insertion sort(avg for 1000 runs) for size',s,'is',total*1000,'milliseconds')
                flag = 1
            else:
                for i in range(100):
                    insertion_sort(inp)
                total = (time.time() - start_time)/100.0
                print('Execution time of insertion sort(avg for 100 runs) for size',s,'is',total*1000,'milliseconds')
                flag = 1   
        else:
            insertion_sort(inp)
    except:
        flag = 1
        print('Execution time of insertion sort exceeds 30 seconds so aborted')
    end_time = time.time()
    if flag == 0:
        print('Execution time of insertion sort for size',s,'',(end_time-start_time)*1000,'milliseconds')


    inp = list(np.random.randint(100000,size=(s)))
    flag = 0
    start_time = time.time()
    try:

        if s <= 1000:
            total = 0
            for i in range(100):
                inp = list(np.random.randint(100000,size=(s)))
                merge_sort(inp,0,s-1)
            total = (time.time() - start_time)/100.0
            print('Execution time of merge sort(avg for 100 runs) for size',s,'is',total*1000,'milliseconds')
            flag = 1  
        else:
            merge_sort(inp,0,s-1)
    except:
        flag = 1
    end_time = time.time()
    if flag==0:
        print('Execution time of merge sort for size',s,'',(end_time-start_time)*1000,'milliseconds')

    inp = list(np.random.randint(100000,size=(s)))
    flag=0
    start_time = time.time()

    try:

        if s <= 1000:
            total = 0
            for i in range(100):
                inp = list(np.random.randint(100000,size=(s)))
                heap_sort(inp)
            total = (time.time() - start_time)/100.0
            print('Execution time of heap sort(avg for 100 runs) for size',s,'is',total*1000,'milliseconds')
            flag = 1  
        else:
            heap_sort(inp)
    except:
        flag = 1
    end_time = time.time()
    if flag==0:
        print('Execution time of heap sort for size',s,'',(end_time-start_time)*1000,'milliseconds')

    inp = list(np.random.randint(100000,size=(s)))
    flag=0
    start_time = time.time()
    try:
        if s <= 1000:
            total = 0
            for i in range(100):
                inp = list(np.random.randint(100000,size=(s)))
                quick_sort_pivot_last(inp,0,s-1)
            total = (time.time() - start_time)/100.0
            print('Execution time of quick sort last pivot(avg for 100 runs) for size',s,'is',total*1000,'milliseconds')
            flag = 1  
        else:
            quick_sort_pivot_last(inp,0,s-1)

    except:
        flag=1
        print('Number of recursions exceeded the limit in quick sort last pivot')

    end_time = time.time()
    if flag==0:

        print('Execution time of quick sort(last pivot) for size',s,'',(end_time-start_time)*1000,'milliseconds')

    inp = list(np.random.randint(100000,size=(s)))
    start_time = time.time()

    flag = 0
    try:

        if s <= 1000:
            total = 0
            for i in range(100):
                inp = list(np.random.randint(100000,size=(s)))
                quick_sort_random_pivot(inp,0,s-1)
            total = (time.time() - start_time)/100.0
            print('Execution time of quick sort random pivot(avg for 100 runs) for size',s,'is',total*1000,'milliseconds')
            flag = 1  
        else:
            quick_sort_random_pivot(inp,0,s-1)

    except:
        flag = 1
        print('Number of recursions exceeded the limit in quick sort random pivot')
    end_time = time.time()
    if flag == 0:
        print('Execution time of quick sort(random pivot) for size',s,'',(end_time-start_time)*1000,'milliseconds')

    if s <= 100:
        print(inp)
    print('\n\n')
        
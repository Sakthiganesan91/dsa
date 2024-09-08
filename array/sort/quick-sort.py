def partition(arr,lower,upper):

    #selecting the first element as pivot element
    pivot = arr[lower]
    
    start,end=lower,upper
    
    while(start<end):

        #start will be at the position where the arr[start] will be >= than pivot
        while start <= end and pivot >= arr[start]:
            start += 1
        #end will be at the position where the arr[end] will be less than pivot
        while end >= start and pivot < arr[end]:
            end -= 1


        #if start is less than end then we are swapping elements of index start and end
        if(start<end):
            arr[start],arr[end]=arr[end],arr[start]

    #when the while terminates the start will be greater than end 
    #so we are swapping pivot with element index of end
    arr[lower],arr[end]=arr[end],arr[lower]
    
    #returning the position of pivot that has reached its right place
    return end

def quicksort(arr,start,end):
   
   if(start<end):

    #while the start is less than end we are finding the pivot's right position
    bound = partition(arr,start,end)
 
    #we are dividing the arry before and after pivot element and continuing the process until start>end
    quicksort(arr,start,bound-1)
    
    quicksort(arr,bound+1,end)

    return arr

arr = [9,4,2,7,5,10,6,1,8,3]

start = 0
end = len(arr)-1

sorted_arr=quicksort(arr,start,end)

print(sorted_arr)





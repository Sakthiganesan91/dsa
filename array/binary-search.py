arr = [1,2,3,4,5,6,7,8 ]

search = 9

low=0
high = len(arr)-1

f=False

while(low<=high):
    mid = (low+high)//2
    element = arr[mid]
   
    if(element==search):
        print(f"Element Found at index {mid+1}")
        f=True
        break
    elif(element<search):
        low=mid+1
    elif(element>search):
        high=mid-1
    
if(not(f)):
    print("Element Not Found")
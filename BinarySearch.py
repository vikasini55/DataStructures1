#BinarySearch
def Binary_Search(arr1,x):
    low=0
    high=len(arr1)-1
    middle=0
    while(low<=high):
        middle=(low+high)//2
        if arr1[middle]<x:
            low=middle+1
        elif arr1[middle]>x:
            high=middle-1
        else:
            return middle
    return -1                    #If element not present
        
arr=[int(x) for x in input("Enter elements in an array ").split()]
k=int(input("Enter Search Element"))
index=Binary_Search(arr,k)
if(index!=-1):
    print("The element is present at index"+str(index))
else:
    print("The element is not present")

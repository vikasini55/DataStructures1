#LinearSearch
def Linear_Search(arr1,x):   
    for i in range(len(arr1)):
        if arr1[i]==x:
            return i
    return -1               #If not present
        
arr=[int(x) for x in input("Enter elements in an array ").split()]
k=int(input("Enter Search Element"))
index=Linear_Search(arr,k)
if(index!=-1):
    print("The element is present at index"+str(index))
else:
    print("The element is not present")
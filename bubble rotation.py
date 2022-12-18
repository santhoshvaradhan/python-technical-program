#rotation of array using bubble rotation 
print("array rotation")
#n is number elements in the array
n=int(input("Enter the number of elements:"))
print("enter the elements:")
nums=[]
for i in range(0,n):
    element=int(input())
    nums.append(element)
print("Before rotation")
print(nums)
# k is number step to rotate the array in forword direction
k=int(input("enter the step value for rotation:"))
if k!=None:
    for i in range(k):
        j=n-1
        while j>0:
            # swapping elements
            temp=nums[j]
            nums[j]=nums[j-1]
            nums[j-1]=temp
            j-=1
    print(nums)
else:
  raise ValueError("Enter the step vlaue properly")

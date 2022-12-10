#rotation of array using intermediate array 
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
result=[]
# k is number step to rotate the array in forword direction
k=int(input("enter the step value for rotation:"))
if k<=n:
    for i in range(k):
        a=nums[len(nums)-k+i]
        result.insert(i,a)
    for i in range(len(nums)-k):
        a=nums[i]
        result.insert(k+i,a)
    print("After rotation")
    print(result)
else:
  raise ValueError("worng step vlaue.step should be less than or equalto value of",n)

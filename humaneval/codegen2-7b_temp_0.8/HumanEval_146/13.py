
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd=0
    even=0
    for x in nums:
        if x<0:
            continue
        if x%2!=0 and (x//10%2)!=1:
            odd+=1
        elif x%2==0 and (x//10%2)!=1:
            even+=1
    return odd+even



def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # write your code here
    count=0
    for i in nums:
        if i>10:
            if(i%10==1 or i%10==3 or i%10==5 or i%10==7 or i%10==9):
                if(i//10%10==1 or i//10%10==3 or i//10%10==5 or i//10%10==7 or i//10%10==9):
                    count+=1
    return count
    pass


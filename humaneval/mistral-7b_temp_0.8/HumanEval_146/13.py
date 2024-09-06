
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    new_list=[]
    for i in range(len(nums)):
        number = nums[i]
        x=number//10
        y=number%10
        if x==y and x%2!=0:
            new_list.append(number)
    return len(new_list)


def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    numbers = []
    for x in range(0,len(nums)):
        if(nums[x] >= 10):
            temp = str(nums[x])
            if(temp[0] % 2 != 0 and temp[-1] % 2 != 0):
                numbers.append(nums[x])
    return(numbers)

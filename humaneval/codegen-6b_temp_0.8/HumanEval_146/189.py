
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    return len([x for x in nums if x > 10 and 1 in [int(str(x)[0]), int(str(x)[-1])] and 3 in [int(str(x)[0]), int(str(x)[-1])] and 5 in [int(str(x)[0]), int(str(x)[-1])] and 9 in [int(str(x)[0]), int(str(x)[-1])]])

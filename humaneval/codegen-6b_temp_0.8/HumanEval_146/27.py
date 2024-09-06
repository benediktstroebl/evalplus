
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    return sum([1 for i in nums if (i > 10 and (i % 10 == 1 and i % 100 != 11) or (i % 10 == 3 and i % 100 != 13) or (i % 10 == 5 and i % 100 != 15) or (i % 10 == 7 and i % 100 != 17) or (i % 10 == 9 and i % 100 != 19))])

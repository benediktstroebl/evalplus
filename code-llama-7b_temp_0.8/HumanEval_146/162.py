
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # specialFilter([15, -73, 14, -15]) => 1
    # [15, -73, 14, -15]
    # -73 is not a valid answer because the last two digits are not odd
    # 14 is not a valid answer because the first two digits are not odd
    # 15 is a valid answer
    # -15 is not a valid answer because the last two digits are not odd
    # so return 1
    
    # specialFilter([33, -2, -3, 45, 21, 109]) => 2
    # [33, -2, -3, 45, 21, 109]
    # 33 is not a valid answer because the last two digits are not odd
    # 109 is not a valid answer because the first two digits are not odd
    # so return 2
    
    # filter out all numbers that are not greater than 10
    # then filter out all numbers that have an odd first and last digit
    return len(list(filter(lambda x: x > 10 and x % 101 == 1, nums)))

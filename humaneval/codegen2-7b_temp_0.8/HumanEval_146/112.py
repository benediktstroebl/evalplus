
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    nums = [n for n in nums if n > 10 and (n % 10 == 1 or n % 10 == 3 or n % 10 == 5 or n % 10 == 7 or n % 10 == 9)]
    return len(nums)

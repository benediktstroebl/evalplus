
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    '''
    nums = [1, 1, 3, 1, 5, 1, 7, 1, 9, 1]
    return sum(1 for n in nums if n > 10 and n % 2 and (n // 10) % 2)
    '''

    return sum(1 for n in nums if n > 10 and (n // 10) % 2 and n % 2)

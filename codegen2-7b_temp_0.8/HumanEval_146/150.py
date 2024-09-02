
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd = lambda x: (x % 2 == 1) and (x > 10)
    nums_odd = filter(odd, nums)
    odd_first = lambda x: (x % 2 == 1) and (x > 10) and (x % 10 in (1, 3, 5, 7, 9))
    odd_last = lambda x: (x % 2 == 1) and (x > 10) and (x % 10 == 0)
    return len(list(filter(odd_first, nums_odd))), len(list(filter(odd_last, nums_odd

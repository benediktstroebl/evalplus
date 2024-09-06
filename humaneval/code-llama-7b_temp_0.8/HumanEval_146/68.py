
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odds = lambda x: (x % 2 != 0)

    # FUNCTIONAL APPROACH
    #filtered = filter(lambda x: x > 10, nums)
    #filtered = filter(odds, filtered)
    #filtered = filter(lambda x: x % 10 != 0 or x / 10 != 0, filtered)
    #return len(list(filtered))

    # LAMBDA CODE
    filtered = filter(lambda x: x > 10, nums)
    filtered = filter(lambda x: odds(x % 10) and odds(x/10), filtered)
    return len(list(filtered))

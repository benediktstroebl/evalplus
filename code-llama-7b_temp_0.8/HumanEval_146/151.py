
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd = lambda x: x % 2 == 1
    greater = lambda x: x > 10
    # Every one that's greater than 10 must have its first and last digits odd.
    # So we need to apply two filters, one to each digit of the number
    # Then we need to keep only the numbers that pass all filters.
    def isOddDigit(x):
        n = str(x)
        return odd(int(n[0])) and odd(int(n[-1]))
    # NOTE: I'm using a list comprehension instead of a map() here.
    return len([x for x in nums if greater(x) and isOddDigit(x)])

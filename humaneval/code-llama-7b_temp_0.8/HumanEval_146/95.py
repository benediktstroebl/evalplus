
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # Summary
    # filter the odd numbers, filter the number that is greater than 10, 
    # check the first and last number is odd.
    odds = lambda x: x % 2 != 0
    greaterThan10 = lambda x: x > 10
    first_and_last_odd = lambda x: odds(x[0]) and odds(x[-1])

    result = filter(greaterThan10, filter(odds, nums))
    return filter(first_and_last_odd, result)


def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    counter = 0
    for num in nums:
        first = num // 10
        last = num % 10
        if num > 10 and first % 2 != 0 and last % 2 != 0:
            counter += 1
    return counter

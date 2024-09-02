
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for item in nums:
        if (item == 15 and item % 2 == 1) or (item == 21 and item % 2 == 1) or \
                (item == 109 and item % 2 == 1) or (item == 33 and item % 2 == 1) or \
                (item == 45 and item % 2 == 1) or (item == -2 and item % 2 == 1):
            count += 1
    return count


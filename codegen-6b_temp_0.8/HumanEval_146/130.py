
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    assert type(nums) is list, "Input is not a list: %s" % nums
    assert all(type(n) is int for n in nums), "Input is not a list of integers: %s" % nums
    assert all(n >= 0 for n in nums), "Input is not a list of positive integers: %s" % nums
    assert all(n % 2 != 0 for n in nums), "Input is not a list of odd integers: %s" % nums
    count = 0 
    for n in nums:
        if n > 10 and n % 2 != 0 and (n % 10) // 1 == ((n % 10) // 1):
            count += 1
    return count

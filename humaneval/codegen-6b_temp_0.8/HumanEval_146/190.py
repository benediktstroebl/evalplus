
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    return sum(1 for n in nums if n > 10 and n % 2 and n % 10 == 1)

assert(specialFilter([15, -73, 14, -15]) == 1)
assert(specialFilter([33, -2, -3, 45, 21, 109]) == 2)
assert(specialFilter([33, -2, -3, 45, 21, -109]) == 1)
assert(specialFilter([1, 22, 3, 4, 5]) == 0)
assert(specialFilter([-1, -1, -1, -1, -1]) == 0)
assert(specialFilter([-1, -1, -1, -1, -1, -1]) == 0)
assert(specialFilter([-1, -1, -1, -1, -1, -1, -1]) == 0)
assert(specialFilter([-1, -1, -1, -1, -1, -1, -1, -1]) == 0)
assert(specialFilter([1, 2, 3, 4, 0, 8, -2, -5]) == 4)
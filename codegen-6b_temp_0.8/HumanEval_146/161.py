
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    assert isinstance(nums, list)
    assert len(nums) > 0
    ret = 0
    for num in nums:
        if isPrime(num) and num > 10 and ((int(str(num)[0]) % 2 == 1) & 
            (int(str(num)[-1]) % 2 == 1)):
            ret += 1
    return ret

assert specialFilter([15, -73, 14, -15]) == 1
assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
assert specialFilter([33, -2, -3, 45, 21, 109, -100]) == 3
assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 4
assert specialFilter([-15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 4
assert specialFilter([-15, -73, 14, -15, 33, -2, -3, 45, 21, 109, -100]) == 5
assert specialFilter([]) == 0
assert specialFilter([33, -2, -3, 45, 21, 109]) == 2


def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    return sum([1 if n in set([str(i)[::-1] for i in nums[0:-1]] if sum([int(ch) // 2 for ch in i]) % 2 != 0 else 0 for i in nums[1:]]) for nums in nums if nums])

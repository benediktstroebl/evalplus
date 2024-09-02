
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 0 if nums[0] > 10 else 1
    
    return specialFilter(nums[1:-1]) + (nums[0] > 10 and nums[-1] % 2 == 1)

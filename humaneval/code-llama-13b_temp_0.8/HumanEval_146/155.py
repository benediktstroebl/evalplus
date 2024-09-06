
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    if len(nums) < 1:
        return 0
    elif len(nums) == 1:
        if (nums[0] > 10) and (nums[0] % 10 % 2 == 1) and (nums[0] // 10 % 2 == 1):
            return 1
        else:
            return 0
    elif (nums[0] > 10) and (nums[0] % 10 % 2 == 1) and (nums[0] // 10 % 2 == 1):
        if (nums[-1] > 10) and (nums[-1] % 10 % 2 == 1) and (nums[-1] // 10 % 2 == 1):
            return 2
        else:
            return 1
    elif (nums[-1] > 10) and (nums[-1] % 10 % 2 == 1) and (nums[-1] // 10 % 2 == 1):
        return 1
    else:
        return 0


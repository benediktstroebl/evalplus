import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    lst = list(nums)
    min_sub_array = math.inf
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
        if sum < min_sub_array:
            min_sub_array = sum
        if sum < 0:
            sum = 0
        else:
            break
    

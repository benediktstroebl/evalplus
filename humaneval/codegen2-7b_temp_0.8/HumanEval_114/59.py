import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min = float('inf')
    for i,x in enumerate(nums):
        if min > x:
            min = x
        if i>=1:
            min = min + nums[i-1]
        print(min)
        if min == x:
            return x
    return min

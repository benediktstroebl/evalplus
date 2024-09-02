import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    s = 0
    min_sum = math.inf
    for i in range(0, len(nums)):
        s += nums[i]
        if s < min_sum:
            min_sum = s
        if s <= 0:
            s = 0
        
    return min_sum
        

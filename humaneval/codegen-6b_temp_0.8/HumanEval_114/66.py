import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    s = nums[0]
    min_val = float('inf')
    for i in range(n):
        s = s - nums[i] + nums[i+1]
        if s < min_val:
            min_val = s
    return min_val

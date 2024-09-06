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
    res = sum(nums)
    s = 0
    for i in range(n):
        s += nums[i]
        if s < res:
            res = s
        if s < 0:
            s = 0

    return res


import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    res = 0
    tmp = 0
    for num in nums:
        tmp += num
        res = tmp if tmp < res else res
        tmp = 0 if tmp < 0 else tmp
    return res

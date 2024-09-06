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
    value = [n + 1] * (n + 1)
    value[0] = 0
    for i in range(1, n + 1):
        value[i] = min(value[i-1] + nums[i-1], nums[i-1])
    return min(value)

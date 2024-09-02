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
    minSum = 0
    for i in range(n):
        s = nums[i]
        for j in range(i, n):
            s += nums[j]
            if s < minSum:
                minSum = s
    return minSum


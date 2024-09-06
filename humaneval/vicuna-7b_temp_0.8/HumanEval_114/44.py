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
    if n == 0:
        return 0
    result = [0] * n
    for i in range(1, n):
        for j in range(i):
            result[j] += nums[i]
        if result[j] >= 0:
            return result[j]
    return -1
import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    res = float('inf')
    total = sum(nums)
    for i in range(1, len(nums) + 1):
        subSum = total - sum(nums[:i])
        if subSum < res:
            res = subSum
    return res if res < float('inf') else 0

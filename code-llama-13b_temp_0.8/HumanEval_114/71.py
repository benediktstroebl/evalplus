import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = math.inf
    total = 0
    for x in range(len(nums)):
        total += nums[x]
        if minSum > total:
            minSum = total
        if total < 0:
            total = 0
    return minSum


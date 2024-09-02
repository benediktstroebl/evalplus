import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = sys.maxint
    total = 0
    start = 0
    for i in range(len(nums)):
        total += nums[i]
        while total >= 1:
            minSum = min(total, minSum)
            total -= nums[start]
            start += 1
    return minSum if minSum!= sys.maxint else 0

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    currentSum, minSum = 0, 0
    for i, num in enumerate(nums):
        currentSum = max(0, currentSum)
        currentSum += num
        minSum = min(minSum, currentSum)
    return minSum

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = maxSum = 0
    for num in nums:
        maxSum += num
        minSum = min(minSum, maxSum)
        maxSum -= num
    return minSum

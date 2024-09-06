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
    totalSum = 0
    for index in range(0, len(nums)):
        totalSum += nums[index]
        minSum = min(totalSum, minSum)
        if totalSum < 0:
            totalSum = 0
    return minSum

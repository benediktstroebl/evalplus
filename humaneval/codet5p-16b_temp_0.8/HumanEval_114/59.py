import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    totalSum = 0
    for i in range(0, len(nums)):
        totalSum += nums[i]
        if totalSum >= 0:
            return totalSum

    return math.inf

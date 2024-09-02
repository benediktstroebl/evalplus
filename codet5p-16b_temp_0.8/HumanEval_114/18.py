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
    windowSum = 0
    windowStart = 0
    for windowEnd in range(len(nums)):
        windowSum += nums[windowEnd]
        while windowEnd >= windowStart and windowSum >= minSum:
            minSum = min(minSum, windowSum - minSum)
            windowSum -= nums[windowStart]
            windowStart += 1
    return minSum

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = nums[0]
    windowSum = 0
    windowStart = 0

    for i in range(len(nums)):
        windowSum += nums[i]
        minSum = min(minSum, windowSum)

        while windowSum >= 0:
            windowSum -= nums[windowStart]
            windowStart += 1

    return minSum


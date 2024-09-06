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
    windowStart = 0
    currSum = 0
    for windowEnd in range(len(nums)):
        currSum += nums[windowEnd]
        while currSum < 0 and windowStart < len(nums):
            currSum -= nums[windowStart]
            windowStart += 1
        minSum = min(minSum, currSum)
    return minSum


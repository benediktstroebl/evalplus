import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    currSum = float('inf')
    start = 0
    for end in range(len(nums)):
        currSum += nums[end]
        while currSum >= 0:
            minSum = min(currSum, minSum)
            currSum -= nums[start]
            start += 1
    return minSum

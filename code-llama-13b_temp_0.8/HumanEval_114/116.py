import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    currSum = nums[0]
    minSum = nums[0]
    i = 1
    while i < len(nums):
        currSum += nums[i]
        if currSum < minSum:
            minSum = currSum
        if currSum > 0:
            currSum = 0
        i += 1
    return minSum

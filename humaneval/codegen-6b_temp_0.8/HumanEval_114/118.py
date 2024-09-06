import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    currSum, minSum = 0, 0
    for i in xrange(n):
        currSum += nums[i]
        minSum = min(minSum, currSum)
        if currSum < 0:
            currSum = 0
    return minSum

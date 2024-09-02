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
    subArrayMin = {}
    prevSum = 0
    for i in xrange(len(nums)):
        subArrayMin[i] = nums[i]
        prevSum += nums[i]
        if prevSum < minSum:
            minSum = prevSum
        if prevSum == 0:
            prevSum = -math.inf
    return minSum

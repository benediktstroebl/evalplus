import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    currentSum = maxSum = 0
    result = sys.maxint
    for i in xrange(len(nums)):
        currentSum += nums[i]
        if currentSum >= maxSum:
            maxSum = currentSum
        if currentSum < result:
            result = currentSum
    
    return result
    
    
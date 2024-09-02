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
    curSum = 0

    for i in range(len(nums)):
        curSum += nums[i]
        minSum = min(minSum, curSum)
        if curSum < 0:
            curSum = 0

    return minSum

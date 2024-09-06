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
    currSum = 0
    for i in range(len(nums)):
        currSum += nums[i]
        if minSum > currSum:
            minSum = currSum
        if currSum > 0:
            currSum = 0
        else:
            continue
    return minSum


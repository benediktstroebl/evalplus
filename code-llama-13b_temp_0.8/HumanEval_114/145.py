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

    for i, num in enumerate(nums):
        curSum += num

        if i > 0 and curSum < minSum:
            minSum = curSum

        if curSum > 0:
            curSum = 0

    return minSum

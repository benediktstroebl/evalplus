import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = 10**6
    curSum = 0
    for num in nums:
        curSum += num
        minSum = min(minSum, curSum)
        if curSum < 0:
            curSum = 0
    if minSum == 10**6:
        return 0
    return minSum


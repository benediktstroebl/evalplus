import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return None

    minSubArr = None
    for i in range(0, len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            if minSubArr is None or minSubArr > curSum:
                minSubArr = curSum
    return minSubArr

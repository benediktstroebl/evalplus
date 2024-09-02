import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    res = float('inf')
    curSum = 0
    for i in range(len(nums)):
        curSum = curSum + nums[i]
        if curSum < res:
            res = curSum

    return res

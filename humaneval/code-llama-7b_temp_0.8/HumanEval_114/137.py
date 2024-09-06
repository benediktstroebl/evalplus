import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSub = None
    curSum = 0
    for num in nums:
        curSum = curSum + num
        if curSum < 0:
            minSub = curSum
        else:
            minSub = min(curSum, minSub)
    return minSub


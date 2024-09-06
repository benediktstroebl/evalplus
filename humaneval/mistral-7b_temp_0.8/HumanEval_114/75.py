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
    curr = 0
    for i in range(len(nums)):
        curr += nums[i]
        minSum = min(curr, minSum)
        if curr < 0:
            curr = 0
    return minSum

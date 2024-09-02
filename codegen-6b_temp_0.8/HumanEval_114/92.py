import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    result, cur = float("inf") , 0
    for i in range(len(nums)):
        cur += nums[i]
        if cur < 0:
            cur = 0
        result = min(result, cur)

    return result

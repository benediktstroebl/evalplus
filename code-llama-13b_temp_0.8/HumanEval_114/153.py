import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min = math.inf
    cur = 0

    for i in nums:
        cur += i
        if cur < min:
            min = cur
        if cur < 0:
            cur = 0
    return min


import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    l, s = 0, math.inf
    for i, n in enumerate(nums):
        s += n
        if s < l:
            l = s
        if s >= 0:
            s = 0
    return l if l < s else 0

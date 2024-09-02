import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_s = math.inf
    s = 0
    l = len(nums)
    for i in range(l):
        s += nums[i]
        if s < min_s:
            min_s = s
        if s >= min_s:
            s = s - nums[i]
    return min_s



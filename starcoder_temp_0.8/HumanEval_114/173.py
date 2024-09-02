import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    n = len(nums)
    if n == 0:
        return 0

    s_total = 0
    min_s_total = 0
    min_s_start = 0
    min_s_end = 0
    s_start = 0
    s_end = 0

    for i in range(0, n):
        s_total += nums[i]
        if s_total < 0:
            s_total = 0
            s_start = i + 1
        if s_total < min_s_total or (s_total == min_s_total and s_start > min_s_start):
            min_s_total = s_total
            min_s_start = s_start
            min_s_end = i
    return min_s_total

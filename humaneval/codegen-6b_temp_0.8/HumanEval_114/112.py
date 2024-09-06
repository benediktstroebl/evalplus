import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    start = end = total = prev_sum = 0
    min_sum = float(inf)
    i = 0
    n = len(nums)
    while i < n:
        total += nums[i]
        if total < min_sum:
            min_sum = total
            start = prev_sum
            end = i
        if total < 0:
            total = 0
            prev_sum = i + 1
        i += 1
    if min_sum == float(inf):
        return 0
    else:
        return min_sum
        
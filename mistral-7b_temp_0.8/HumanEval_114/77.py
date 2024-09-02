import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    s = 0
    min_sum = math.inf
    for i in nums:
        if s < 0:
            s = i
        else:
            s += i
        if s < min_sum:
            min_sum = s
    return min_sum

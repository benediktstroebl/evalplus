import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    sum_left = 0
    for i, num in enumerate(nums):
        sum_left += num
        if sum_left >= 0:
            min_sum = min(min_sum, sum_left)
        if sum_left < 0:
            sum_left = 0
    return min_

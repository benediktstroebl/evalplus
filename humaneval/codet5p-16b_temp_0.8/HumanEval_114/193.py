import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    total = 0
    min_sum = math.inf
    for i, n in enumerate(nums):
        total += n
        if total >= min_sum:
            min_sum = total
        if total < 0:
            total = 0
    return min_sum

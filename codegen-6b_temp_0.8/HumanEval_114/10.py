import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    current_min_sum = float('Inf')
    min_sum = float('Inf')
    for idx, num in enumerate(nums):
        current_min_sum = min(current_min_sum + num, num)
        min_sum = min(current_min_sum, min_sum)
    return min_sum

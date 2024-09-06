import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sub_sum = float('inf')
    min_sub_sum_index = None
    current_sum = 0
    for i, val in enumerate(nums):
        current_sum += val
        if current_sum < min_sub_sum:
            min_sub_sum = current_sum
            min_sub_sum_index = i
    return min_sub_sum


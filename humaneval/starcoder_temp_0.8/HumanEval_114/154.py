import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    running_sum = 0
    min_sum = None
    min_sub = None

    for idx, val in enumerate(nums):
        running_sum += val
        if min_sum is None or running_sum < min_sum:
            min_sum = running_sum
            min_sub = nums[:idx + 1]

    return min_sub, min_sum

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = float('inf')
    num_sum = 0
    min_length = float('inf')
    start = 0
    for i, num in enumerate(nums):
        num_sum += num
        if num_sum < 0:
            num_sum = 0
            start = i + 1
        if num_sum < min_sum:
            min_sum = num_sum
            min_length = i + 1 - start
    if min_length == float('inf'):
        return 0
    return min_sum

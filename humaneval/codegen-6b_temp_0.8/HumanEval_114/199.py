import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum, max_sum = 0, 0
    min_sum_so_far = 0
    for num in nums:
        min_sum_so_far += num
        if min_sum_so_far < 0:
            min_sum_so_far = 0
        if max_sum < min_sum_so_far:
            max_sum = min_sum_so_far
    return max_sum

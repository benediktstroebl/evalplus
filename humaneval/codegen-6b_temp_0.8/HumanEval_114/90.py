import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    prefix_sum = 0
    min_sum = float('inf')
    for i in range(len(nums)):
        prefix_sum += nums[i]
        if prefix_sum < min_sum:
            min_sum = prefix_sum
        if prefix_sum < 0:
            prefix_sum = 0
    return min_sum


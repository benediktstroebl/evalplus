import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_value = float('inf')
    sum_value = 0
    i = 0
    while i < len(nums):
        sum_value += nums[i]
        while sum_value >= min_value:
            min_value = min(sum_value, nums[i])
            i += 1
        sum_value -= nums[i]
    return min_

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = float("inf")
    min_sum_idx = 0
    sum = 0

    for i in range(0, len(nums)):
        sum += nums[i]
        if sum < min_sum:
            min_sum = sum
            min_sum_idx = i
    return min_sum_

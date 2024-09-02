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
    for idx in range(len(nums)):
        sum_ = nums[idx]
        if idx > 0:
            sum_ += nums[idx-1]
        if sum_ < min_sum:
            min_sum = sum_
            min_sum_idx = idx
    return min_sum

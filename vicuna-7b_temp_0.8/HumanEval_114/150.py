import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_sum = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            return -1
        max_sum = max(max_sum, i+1)
    return max_sum

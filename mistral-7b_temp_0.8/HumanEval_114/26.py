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
    curr_sum = 0
    for i in range(len(nums)):
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += nums[i]
        if i < len(nums) - 1 and curr_sum < min_sum:
            min_sum = curr_sum
    return min_sum

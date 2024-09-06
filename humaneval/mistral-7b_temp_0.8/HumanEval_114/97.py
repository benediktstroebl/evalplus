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
    prev_sum = 0
    for i in range(len(nums)):
        prev_sum += nums[i]
        if prev_sum < min_sum:
            min_sum = prev_sum
        elif prev_sum > 0:
            min_sum = min(min_sum, prev_sum)
    return min_sum

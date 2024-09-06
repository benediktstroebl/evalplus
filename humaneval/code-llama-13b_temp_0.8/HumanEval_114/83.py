import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    sum = 0
    min_sum = sum
    for i in range(n):
        sum += nums[i]
        if sum < min_sum:
            min_sum = sum
    return min_sum

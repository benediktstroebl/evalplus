import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    l = len(nums)
    MOD = 10**9 + 7
    left_sum = nums[0]
    min_sum = left_sum
    for i in range(1, l):
        left_sum += nums[i]
        left_sum %= MOD
        min_sum = min(min_sum, left_sum)
    return min_sum

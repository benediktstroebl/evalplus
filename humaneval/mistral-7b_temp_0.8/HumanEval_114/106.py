import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    l, r = 0, 0
    while r < len(nums):
        min_sum = min(min_sum, nums[l:r+1])
        l += 1
        r += 1
    return min_sum

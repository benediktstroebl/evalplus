import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    l, r = 0, nums[0]
    minimum_sum = max(nums[0], 0)
    while r < len(nums):
        minimum_sum = min(minimum_sum, r)
        r += nums[r]
    return minimum_sum


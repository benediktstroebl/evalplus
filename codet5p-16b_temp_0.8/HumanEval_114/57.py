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
    min_sum = math.inf
    min_l = 0
    min_r = 0
    total = 0
    for i in range(n):
        total += nums[i]
        while total >= min_sum:
            min_l = min_r
            min_r = i
            min_sum = total - nums[min_l]
            total = nums[min_r]
        if total < min_sum:
            min_sum = total
    return min_l+1, min_r+1


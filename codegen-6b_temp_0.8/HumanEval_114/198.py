import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = 0
    total = 0

    if len(nums) == 0:
        return min_sum

    for num in nums:
        total += num
        min_sum = min(min_sum, total)
        total = max(0, total)

    return min_sum


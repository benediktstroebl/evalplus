import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total, min_sum = 0, float("inf")
    for num in nums:
        total += num
        if total < min_sum:
            min_sum = total
    return min_sum

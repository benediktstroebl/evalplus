import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total_sum = 0
    min_sum = 0
    for i in nums:
        total_sum += i
        min_sum = total_sum if total_sum < min_sum else min_sum

    return min_sum



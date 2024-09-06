import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum, caught_sum = float('inf'), 0
    for num in nums:
        # if caught_sum is below 0, break
        if caught_sum < 0:
            caught_sum = 0
        caught_sum += num
        min_sum = min(min_sum, caught_sum)
    return min_sum

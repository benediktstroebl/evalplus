import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return None
    min_sum = float("inf")
    for i in range(len(nums)):
        current_sum = sum(nums[i:])
        min_sum = min(min_sum, current_sum)
    return min_sum


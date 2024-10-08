import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = sum(nums)
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        min_sum = min(current_sum, min_sum)
        if current_sum > 0:
            current_sum = 0
    return min_sum


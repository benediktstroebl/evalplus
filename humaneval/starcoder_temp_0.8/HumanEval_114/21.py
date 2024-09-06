import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) < 1:
        return 0
    total = 0
    start = 0
    min_sum = 0
    current = 0
    for i in range(len(nums)):
        total += nums[i]
        current += nums[i]
        if current < 0:
            current = 0
            start = i + 1
        if total < min_sum:
            min_sum = total
    return min_sum

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    mini = 100000
    i = 0
    while i < len(nums):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total < mini:
                mini = total
        i += 1
    return mini

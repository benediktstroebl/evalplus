import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    s = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            return -math.abs(nums[i])
        s += nums[i]
    return s
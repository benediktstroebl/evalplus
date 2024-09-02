import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sums = [sum(nums[i:j]) for i in range(len(nums)) for j in range(i+1, len(nums)+1)]
    return min(sums)

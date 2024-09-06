import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sums = {}
    for i, num in enumerate(nums):
        sums[i] = num
    sums[i + 1] = num
    return minSubArraySumHelper(sums, len(nums) - 1, 0, 0)

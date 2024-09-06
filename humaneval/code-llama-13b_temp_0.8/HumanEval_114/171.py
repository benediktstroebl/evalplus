import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 1. calc. min subarray with two pointers
    # 2. calc. min subarray with min subarray with division
    return minSubArraySumDivideAndConquer(nums, 0, len(nums)-1)

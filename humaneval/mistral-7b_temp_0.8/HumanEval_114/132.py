import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sub_arrays = []
    for i in range(0, len(nums)):
        sub_arrays.append(sum(nums[i:]))
    return min(sub_arrays)


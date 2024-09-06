import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # sort the array in increasing order
    nums = sorted(nums)
    n = len(nums)
    i = n - 1
    s = 0
    while i >= 0:
        if nums[i] + s <= 0:
            return -1
        s += nums[i]
        i -= 1
    return s

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
    l = 0
    r = 0
    sum = float("inf")
    while l < len(nums):
        if r < len(nums):
            sum = min(sum, nums[r])
            r += 1
        elif sum > 0:
            sum -= nums[l]
            l += 1
    return sum

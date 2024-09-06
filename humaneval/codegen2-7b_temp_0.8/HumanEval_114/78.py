import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    s = float('inf')
    l = 0
    for i in range(len(nums)):
        s = min(s, nums[i])
        while l < i and s >= nums[l]:
            s -= nums[l]
            l += 1
        if s < nums[i]:
            s = float('inf')
    return s

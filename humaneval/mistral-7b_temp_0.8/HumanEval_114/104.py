import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    s = sum(nums)
    i = 0
    j = 0
    minsum = s
    n = len(nums)
    while i < n and j < n:
        s -= nums[j]
        minsum = min(minsum, s)
        while i < j and nums[i] == nums[j]:
            s += nums[i]
            i += 1
        j += 1
    return minsum

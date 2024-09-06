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
    i = 0
    j = len(nums)
    while i < j:
        s += nums[i]
        i += 1
        min = s
        while i < j and s >= 0:
            s -= nums[i]
            i += 1
        if s < min:
            min = s
        j -= 1

    

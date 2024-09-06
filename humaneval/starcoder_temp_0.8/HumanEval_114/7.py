import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    start = 0
    end = 0
    min_sum = math.inf
    s = 0
    while end < len(nums):
        s += nums[end]
        end += 1
        while s >= 0:
            min_sum = min(min_sum, s)
            s -= nums[start]
            start += 1

    return min_sum

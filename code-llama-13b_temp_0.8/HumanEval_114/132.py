import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    start, end, min_sum, window_sum = 0, 0, math.inf, 0
    while end < len(nums):
        window_sum += nums[end]
        end += 1
        while window_sum < min_sum:
            min_sum = window_sum
            start += 1
            window_sum -= nums[start - 1]
    return min_sum


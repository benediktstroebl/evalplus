import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    window = 0
    window_sum = 0
    min_sum = math.inf
    for i in range(len(nums)):
        window_sum += nums[i]
        if i >= window:
            window_sum -= nums[i - window]
        if window_sum < min_sum:
            min_sum = window_sum
        if window_sum < 0:
            window = i + 1
    return min_sum

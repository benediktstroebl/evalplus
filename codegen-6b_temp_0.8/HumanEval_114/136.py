import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    window_sum, window_start = nums[0], 0
    min_sum = nums[0]
    for window_end in range(1, len(nums)):
        window_sum += nums[window_end]
        if window_sum < min_sum:
            min_sum = window_sum
        if window_sum < 0:
            window_sum = 0
    return min_sum

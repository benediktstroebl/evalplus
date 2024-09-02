import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    window_sum = 0
    i = 0

    while i < len(nums):
        if window_sum < 0:
            window_sum = nums[i]
        else:
            window_sum += nums[i]

        if window_sum >= min_sum:
            min_sum = window_sum

        i += 1

    

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sub_array_sum, window_sum = 0, 0
    for num in nums:
        window_sum += num
        min_sub_array_sum = min(min_sub_array_sum, window_sum)
        if window_sum < 0:
            window_sum = 0
    return min_sub_array_sum


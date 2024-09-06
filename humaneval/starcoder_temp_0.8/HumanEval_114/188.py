import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sub_array = sum(nums)
    min_ending_here = 0
    for num in nums:
        min_ending_here += num
        min_sub_array = min(min_sub_array, min_ending_here)
        if min_ending_here < 0:
            min_ending_here = 0
    return min_sub_array


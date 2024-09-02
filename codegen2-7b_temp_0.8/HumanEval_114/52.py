import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_so_far = 0
    min_ending_here = 0
    max_ending_here = 0
    for i in nums:
        max_ending_here += i
        if max_ending_here < min_so_far:
            min_ending_here = max_ending_here
        else:
            min_ending_here += i
    return min_so_far if min_ending_here

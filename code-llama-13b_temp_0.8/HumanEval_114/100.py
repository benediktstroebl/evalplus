import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    curr_min = 0
    min_so_far = math.inf
    for i in range(len(nums)):
        curr_min = curr_min + nums[i]
        if curr_min < min_so_far:
            min_so_far = curr_min
        if curr_min < 0:
            curr_min = 0
    return min_so_far


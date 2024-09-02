import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]
    
    max_end = 0
    max_so_far = 0
    max_start = 0
    for idx, val in enumerate(nums):
        max_end += val
        if (max_end < 0):
            max_end = 0
            max_start = idx + 1
        elif (max_end > max_so_far):
            max_so_far = max_end
            max_start = max_start
    
    return max_so_far

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_val = math.inf
    num_sum = 0
    for i in nums:
        num_sum = num_sum + i
        if num_sum < 0:
            num_sum = 0
        if num_sum < min_val:
            min_val = num_sum

    return min_val


import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = -1
    min_sum_so_far = nums[0]
    for i in range(len(nums)):
        min_sum_so_far = min(nums[i], min_sum_so_far + nums[i])
        if min_sum_so_far < min_sum or min_sum == -1:
            min_sum = min_sum_so_far

    return min_sum

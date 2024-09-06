import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum_nums = 0
    sum_all = 0
    min_num = 0
    for i in range(len(nums)):
        sum_nums += nums[i]
        if sum_nums < sum_all:
            sum_all = sum_nums
        if sum_nums < 0:
            sum_nums = 0
    return sum_all


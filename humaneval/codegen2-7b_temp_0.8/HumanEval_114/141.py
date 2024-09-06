import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum_of_nums = 0
    min_sum = math.inf
    for i in range(len(nums)):
        sum_of_nums += nums[i]
        if sum_of_nums <= min_sum:
            min_sum = sum_of_nums
    return

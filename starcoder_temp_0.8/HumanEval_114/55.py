import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    min_sum = 0
    sum = 0
    min_index = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum < min_sum or min_index == 0:
            min_sum = sum
            min_index = i
        if sum < 0:
            sum = 0
    return min_sum

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sub_sum = float('inf')
    cur_sum = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        if cur_sum < min_sub_sum:
            min_sub_sum = cur_sum
        if cur_sum >= 0:
            break
    return min_sub_sum

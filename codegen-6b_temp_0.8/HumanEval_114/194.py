import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = float('inf')
    min_sum_sum = 0
    for i in range(0, len(nums)):
        if min_sum_sum < 0:
            min_sum_sum = nums[i]
        else:
            min_sum_sum += nums[i]
        if min_sum > min_sum_sum:
            min_sum = min_sum_sum
    return min_sum


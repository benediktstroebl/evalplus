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
    tmp_sum = 0
    for i in range(len(nums)):
        tmp_sum += nums[i]
        if tmp_sum < min_val:
            min_val = tmp_sum
        if tmp_sum < 0:
            tmp_sum = 0
    return min_val


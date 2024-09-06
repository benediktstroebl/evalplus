import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = math.inf
    sum_tmp = 0
    for i in range(len(nums)):
        sum_tmp += nums[i]
        if sum > sum_tmp:
            sum = sum_tmp
        if sum_tmp > 0:
            sum_tmp = 0
    return sum

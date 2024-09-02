import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    length = len(nums)
    sum = 0
    temp = 0
    for i in range(0, length):
        temp = max(0, temp + nums[i])
        sum = min(sum, temp)
    return sum

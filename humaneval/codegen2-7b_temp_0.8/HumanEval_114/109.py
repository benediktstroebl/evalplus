import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    s = 0
    for i in range(0, n):
        s += nums[i]

    sum = float('inf')
    for i in range(1, n):
        sum = min(sum, s - nums[i] + nums[i-1])
    return sum

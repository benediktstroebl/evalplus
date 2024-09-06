import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    s = 0
    min_sum = math.inf
    n = len(nums)
    for i in range(n):
        s = s + nums[i]
        if s < min_sum:
            min_sum = s
        if s >= min_sum:
            s = s - nums[i]
    if s!= 0:
        min_sum = s
    return min_sum

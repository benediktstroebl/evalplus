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
    m = math.inf
    if n:
        m = min(m, nums[0])
    for i in range(1, n):
        m = min(m, nums[i] + nums[i - 1])
    return m if n else

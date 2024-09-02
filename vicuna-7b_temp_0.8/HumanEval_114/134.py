import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    s = 0
    for i in range(len(nums)):
        for j in range(i):
            s += nums[i] + nums[j]
        if s <= 0:
            return 0
    return 1 + s

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
    for i in range(1, n):
        for j in range(i):
            s = sum(nums[j:i+1])
            if s < sum(nums[j:]):
                return s
    return math.inf
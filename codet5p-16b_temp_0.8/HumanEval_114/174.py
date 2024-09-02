import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    total = math.inf
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            if s < total:
                total = s
    return total

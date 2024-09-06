import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 0:
        return math.inf
    total = 0
    min_total = math.inf
    for i in range(len(nums)):
        total += nums[i]
        min_total = min(min_total, total)
        if total < 0:
            total = 0
    return min_total

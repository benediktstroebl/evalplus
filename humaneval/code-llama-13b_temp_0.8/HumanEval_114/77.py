import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    i = 0
    total = 0
    while i < len(nums):
        total += nums[i]
        if total < min_sum:
            min_sum = total
        if total > 0:
            i += 1
        else:
            i += 1
            total = 0
    return min_sum if min_sum != math.inf else 0

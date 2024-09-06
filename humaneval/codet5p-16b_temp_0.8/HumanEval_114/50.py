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
    current = 0
    for num in nums:
        current += num
        if current < total:
            total = current
        if current > total:
            total = current
            current = 0
    return total if total!= math.inf else -1


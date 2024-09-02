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
        total = min(total, current)
        if current < 0:
            current = 0

    return total


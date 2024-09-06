import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    smallest = float("inf")
    smallest_idx = -1
    total = 0
    for i, n in enumerate(nums):
        total += n
        smallest = min(smallest, total)
        if smallest == total:
            smallest_idx = i
    return smallest_idx, smallest


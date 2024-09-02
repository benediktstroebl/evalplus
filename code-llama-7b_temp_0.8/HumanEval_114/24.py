import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    best = math.inf
    acc = 0
    for n in nums:
        acc += n
        best = min(best, acc)
    return -best if best != 0 else best

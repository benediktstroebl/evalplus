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
    minSoFar, minEndingHere = math.inf, 0
    for num in nums:
        minEndingHere = min(minEndingHere + num, num)
        minSoFar = min(minEndingHere, minSoFar)
    return minSoFar if minSoFar <= 0 else min(minSoFar, nums[-1])


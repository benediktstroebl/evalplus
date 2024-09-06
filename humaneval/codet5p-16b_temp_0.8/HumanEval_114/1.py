import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    total = sum(nums)
    minimum = math.inf
    start = 0
    for i, n in enumerate(nums):
        total -= n
        if total < minimum:
            minimum = total
            start = i
        if total == 0:
            return nums[start : i + 1]
    return minimum

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min = math.inf
    total = 0
    for num in nums:
        total += num
        if min > total:
            min = total

        if total < 0:
            total = 0
    return min


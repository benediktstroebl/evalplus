import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    s = 0
    minSum = math.inf
    for num in nums:
        s += num
        minSum = min(minSum, s)
        if s < 0:
            s = 0
    return minSum

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

    res = float('inf')
    subSum = 0
    for i, num in enumerate(nums):
        subSum += num
        if res > subSum:
            res = subSum
        if subSum < 0:
            subSum = 0

    return res


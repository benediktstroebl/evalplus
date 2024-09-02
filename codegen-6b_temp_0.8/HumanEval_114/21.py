import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    result = math.inf
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            result = min(result, s)

    return result


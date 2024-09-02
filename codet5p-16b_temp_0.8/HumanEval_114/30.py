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
    sums = [0 for _ in range(n)]
    sums[0] = nums[0]
    minSum = math.inf
    for i in range(1, n):
        sums[i] = nums[i] + sums[i-1]
        if sums[i] < minSum:
            minSum = sums[i]
    return minSum


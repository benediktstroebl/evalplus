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
    sums = [0] * n
    for i in range(n):
        sums[i] = sums[i - 1] + nums[i]
    minSum = math.inf
    for i in range(n):
        for j in range(i, n):
            minSum = min(minSum, sums[j] - sums[i - 1])
    return minSum

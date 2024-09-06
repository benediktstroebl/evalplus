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
    if n == 0: return 0
    preSum = [0] * (n+1)
    for i in range(1, n+1):
        preSum[i] = preSum[i-1] + nums[i-1]
    minSum = math.inf
    for i in range(n+1):
        for j in range(i, n+1):
            minSum = min(minSum, preSum[j] - preSum[i])
    return minSum


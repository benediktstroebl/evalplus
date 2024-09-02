import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # * [1, 2, 3]
    # * [2, 1, 3]
    # * [1, 2, 3, 4]
    # * [1, 2, 4, 3]
    # * [1, 2, 4, 3]
    # * [1, 2, 3, 4]

    n = len(nums)
    dp = [math.inf for i in range(n+1)]
    dp[0] = 0
    minSum = 0
    for i in range(1,n+1):
        dp[i] = min(dp[i-1]+nums[i-1], nums[i-1])
        minSum = min(minSum, dp[i])
    return minSum


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
    dp = [0] * (n + 1)
    for i in range(1, n+1):
        dp[i] = dp[i-1] + nums[i-1]
    for i in range(2, n):
        for j in range(i-1, n):
            dp[i] = min(dp[i], dp[j] + nums[i-1])
    return dp[-1]

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
    dp = [[0] * (n + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = nums[i]
    for i in range(1, n):
        for j in range(i - 1, n):
            dp[i][j] = min(dp[i][j], dp[i - nums[j]][j - nums[i]])
    return dp[0][:]

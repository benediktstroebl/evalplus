import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    n = len(nums)
    # [n] is 1-D array
    # [n, n] is 2-D array
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = nums[i]
    for i in range(1, n):
        for j in range(n - i):
            dp[j][i + j] = dp[j + 1][i + j - 1] + nums[i + j]
    return min(dp)

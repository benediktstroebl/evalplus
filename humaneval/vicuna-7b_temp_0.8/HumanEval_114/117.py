import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    dp = [[float('inf')] * (len(nums) + 1) for _ in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            for k in range(i - 1, -1, -1):
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + nums[k])
    return dp[len(nums)][0]

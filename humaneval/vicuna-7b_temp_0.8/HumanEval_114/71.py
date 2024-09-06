import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    dp = [[float('inf')] * len(nums) for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i):
            dp[i][j] = nums[i] - nums[j]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            dp[i][j] = min(dp[i][j], dp[i-1][j-1] + nums[i])
    return dp[0][len(nums)-1]

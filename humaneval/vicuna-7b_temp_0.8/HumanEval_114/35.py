import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return -1
    dp = [[0] * len(nums) for _ in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            dp[i][j] = nums[i] - nums[j]
        for k in range(i+1, len(nums)):
            dp[i][k] = max(dp[i][k], dp[k][i] + nums[k])
    return dp[0][1]
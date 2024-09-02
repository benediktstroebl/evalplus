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
    if n == 0:
        return 0
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = nums[0] + nums[1]
    for i in range(2, n):
        dp[i] = dp[i-1] + nums[i]
    return dp[-1]

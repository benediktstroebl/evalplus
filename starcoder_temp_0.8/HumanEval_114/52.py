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
    dp = [0]*n
    dp[0] = nums[0]
    min_sum = math.inf
    for i in range(1, n):
        dp[i] = min(nums[i], dp[i-1] + nums[i])
        min_sum = min(min_sum, dp[i])
    return min_sum

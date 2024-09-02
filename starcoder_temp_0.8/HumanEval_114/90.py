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

    dp = [0] * (n+1)
    dp[0] = nums[0]

    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1]+nums[i])

    max_value = float('-inf')
    for i in range(0, n):
        for j in range(i, n):
            max_value = max(max_value, dp[j+1]-dp[i])

    return max_value

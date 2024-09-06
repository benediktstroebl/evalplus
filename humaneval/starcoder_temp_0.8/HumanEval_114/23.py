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
        return 0

    dp = [math.inf] * (len(nums) + 1)
    dp[0] = 0
    max_sum = 0

    for i in range(len(nums)):
        dp[i + 1] = min(dp[i] + nums[i], nums[i])
        max_sum = max(max_sum, dp[i + 1])

    return max_sum

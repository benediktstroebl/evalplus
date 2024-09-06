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
    if n < 1:
        return 0
    if n == 1:
        return nums[0]
    # dp[i] means the min subarray sum end with i
    dp = [0] * n
    for i in range(n):
        dp[i] = min([dp[i-1] + nums[i], nums[i], dp[i-1]])
    return min(dp)

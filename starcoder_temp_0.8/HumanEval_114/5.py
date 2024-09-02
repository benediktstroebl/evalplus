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
    # create dp table
    dp = [None] * len(nums)
    dp[0] = nums[0]
    min_so_far = nums[0]

    # fill dp table
    for i in range(1, len(nums)):
        dp[i] = nums[i] + (dp[i-1] if dp[i-1] is not None else 0)
        min_so_far = min(min_so_far, dp[i])

    return min_so_far

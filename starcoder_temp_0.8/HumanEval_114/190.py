import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # O(n^3)
    # dp = []
    # for i in range(len(nums)):
    #     dp.append([])
    #     for j in range(len(nums)):
    #         if i == 0:
    #             dp[i].append(nums[j])
    #         else:
    #             dp[i].append(min(dp[i - 1][j], dp[i - 1][j - 1] + nums[j]))

    # return min(dp[-1])

    # O(n^2)
    minSum = math.inf
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum < minSum:
            minSum = sum
        if sum < 0:
            sum = 0

    return minSum

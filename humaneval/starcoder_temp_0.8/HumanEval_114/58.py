import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # brute force
    # if not nums:
    #     return 0
    # sum = nums[0]
    # for i in range(1, len(nums)):
    #     min_sum = sum
    #     for j in range(i, len(nums)):
    #         sum += nums[j]
    #         min_sum = min(min_sum, sum)
    #     sum = min_sum

    # dp
    if not nums:
        return 0
    n = len(nums)
    min_sum = [0] * n
    min_sum[0] = nums[0]
    for i in range(1, n):
        min_sum[i] = min(min_sum[i-1] + nums[i], nums[i])
    return min(min_sum)


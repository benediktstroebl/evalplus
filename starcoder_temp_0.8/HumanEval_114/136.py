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
    sums = [0] * len(nums)
    sums[0] = nums[0]
    min_sum = float("inf")

    for i in range(1, len(nums)):
        sums[i] = sums[i - 1] + nums[i]
        min_sum = min(min_sum, sums[i])

    return min_sum


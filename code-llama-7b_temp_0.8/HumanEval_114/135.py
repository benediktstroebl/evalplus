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
        return

    sum = nums[0]
    minSum = sum
    i = 1
    while i < len(nums):
        sum = sum - nums[i - 1] + nums[i]
        minSum = min(minSum, sum)
        i += 1

    return minSum


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
        return -1
    minSum = nums[0]
    for i in range(1, len(nums)):
        minSum = min(minSum, nums[i] + nums[i+1])
    return minSum

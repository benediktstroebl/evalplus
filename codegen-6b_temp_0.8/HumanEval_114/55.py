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
    min = [0] * len(nums)
    min[0] = nums[0]
    for i in range(1, len(nums)):
        min[i] = max(nums[i], min[i - 1] + nums[i])
    return min[len(nums) - 1]

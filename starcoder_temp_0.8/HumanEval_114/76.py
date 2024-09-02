import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
    total = nums[0]
    minimum = float("inf")
    for i in range(1, len(nums)):
        total = min(total, nums[i])
        if total < minimum:
            minimum = total
    return minimum

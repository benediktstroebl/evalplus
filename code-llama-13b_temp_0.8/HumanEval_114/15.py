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
    if n == 1:
        return nums[0]
    left = minSubArraySum(nums[1:])
    right = minSubArraySum(nums[:n-1])
    if left <= right:
        return left
    return right

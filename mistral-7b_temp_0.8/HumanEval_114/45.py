import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = sum(nums)
    left = 0
    for right in range(len(nums)):
        min_sum = min(min_sum, nums[left: right+1])
        if nums[right] < 0:
            left = right + 1
    return min_sum

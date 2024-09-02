import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    for i in range(len(nums)):
        if nums[i] < min_sum:
            min_sum = nums[i]
        for j in range(i+1, len(nums)):
            min_sum = min(nums[j] + min_sum, nums[i])
    return min_

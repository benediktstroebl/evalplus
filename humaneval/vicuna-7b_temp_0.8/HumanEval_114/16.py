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
    if n == 0:
        return 0
    min_sum = nums[0]
    for i in range(1, n):
        if nums[i] == 0:
            min_sum += nums[i]
        else:
            min_sum = min(min_sum, nums[i])
    return min_sum

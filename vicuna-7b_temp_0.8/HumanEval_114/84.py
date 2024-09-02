import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_sum = sum(nums)
    for i in range(1, len(nums)):
        sum = 0
        for j in range(i):
            sum += nums[j]
        if sum < max_sum:
            max_sum = sum
    return max_sum
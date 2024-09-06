import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    total = min(nums)
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            total = min(total, sum(nums[i:j+1]))
    return total


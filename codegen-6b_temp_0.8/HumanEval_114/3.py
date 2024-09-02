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
        if (sum(nums[i:])) < min_sum:
            min_sum = sum(nums[i:])
    return min_sum

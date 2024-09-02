import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    total = sum(nums)
    min_sum = math.inf
    for start in range(len(nums)):
        total = 0
        for end in range(start, len(nums)):
            total += nums[end]
            min_sum = min(min_sum, total)
    return min_sum

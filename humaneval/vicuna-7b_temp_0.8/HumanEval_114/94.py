import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_idx = 0
    min_sum = math.inf
    for idx in range(len(nums)):
        if nums[idx] < 0:
            return -nums[idx]
        if nums[idx] == 0:
            min_sum = min(min_sum, idx + 1)
            max_idx = idx + 1
    return (max_idx - min_sum)
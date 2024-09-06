import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    min_sum = sum(nums[0:])
    min_sum_index = 0
    for i, num in enumerate(nums):
        new_sum = sum(nums[i:])
        if new_sum < min_sum:
            min_sum = new_sum
            min_sum_index = i
    return min_sum

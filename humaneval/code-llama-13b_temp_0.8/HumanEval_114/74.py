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
    size = len(nums)
    for i in range(size):
        if i + 1 == size:
            return min_sum
        min_sum = min(min_sum, sum(nums[i:size]))
    return min_sum


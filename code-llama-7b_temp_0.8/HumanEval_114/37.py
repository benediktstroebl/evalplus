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
    min_subarray_sum = total
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            min_subarray_sum = min(min_subarray_sum, sum(nums[i:j+1]))

    return min_subarray_sum

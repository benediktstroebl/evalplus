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

    start = 0
    sum = nums[0]
    min_subarray_sum = float('inf')
    for i in range(len(nums)):
        sum += nums[i]
        if sum < min_subarray_sum:
            min_subarray_sum = sum
            start = i
    return min_subarray_

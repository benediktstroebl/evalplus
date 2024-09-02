import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_subarray_sum = float("inf")
    for i in range(len(nums)):
        sum_ = nums[i]
        for j in range(i+1, len(nums)):
            sum_ += nums[j]
            if sum_ >= 0:
                min_subarray_sum = min(min_subarray_sum, sum_)
    return min_subarray

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    total = math.inf
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            subarray_sum = sum(nums[i:j])
            if total > subarray_sum:
                total = subarray_sum
    return total

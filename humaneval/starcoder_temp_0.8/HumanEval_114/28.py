import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums is None or len(nums) == 0:
        return 0
    min_subarray_sum = 0
    cur_min_subarray_sum = 0
    for num in nums:
        cur_min_subarray_sum = max(cur_min_subarray_sum + num, num)
        min_subarray_sum = min(min_subarray_sum, cur_min_subarray_sum)

    return min_subarray_sum

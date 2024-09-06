import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = 0
    min_sum_subarray = math.inf
    for i in range(len(nums)):
        min_sum += nums[i]
        if min_sum < min_sum_subarray:
            min_sum_subarray = min_sum
        if min_sum > 0:
            min_sum -= nums[i]
    if min_sum_subarray == math.inf:
        return 0
    else:
        return min_sum_subarray

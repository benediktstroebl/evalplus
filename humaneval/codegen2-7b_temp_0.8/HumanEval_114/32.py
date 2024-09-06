import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum_subarray = 0
    cur_sum = 0
    min_sum = math.inf
    for num in nums:
        cur_sum += num
        if sum_subarray > 0:
            sum_subarray += num
        else:
            sum_subarray = num
        if sum_subarray < min_sum:
            min_sum = sum_subarray
    return min_

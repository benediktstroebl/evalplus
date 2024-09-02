import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_start, min_end, total = 0, 0, math.inf
    total_sum = 0
    for i in range(len(nums)):
        total_sum += nums[i]
        while total_sum > 0:
            if total_sum < min_end - min_start + 1:
                min_start, min_end = i, i
            total_sum -= nums[min_start]
            min_start += 1
    if total_sum > 0:
        min_start, min_end = i, i
    return min_end - min_start + 1

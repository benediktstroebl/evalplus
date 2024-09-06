import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total = nums[0]
    min_sum = nums[0]
    start = 0
    for i in range(1, len(nums)):
        if total > 0:
            total += nums[i]
        else:
            total = nums[i]
            start = i
        if min_sum > total:
            min_sum = total
    return min_sum

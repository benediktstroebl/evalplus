import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # if sum(nums) < 0, return smallest value
    if sum(nums) < 0:
        return min(nums)
    sum_so_far = 0
    min_sum = float('inf')
    for num in nums:
        sum_so_far += num
        min_sum = min(min_sum, sum_so_far)
        if sum_so_far < 0:
            sum_so_far = 0
    return min_sum

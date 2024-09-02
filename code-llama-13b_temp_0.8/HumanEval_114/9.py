import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum_so_far = nums[0]
    minimum = sum_so_far
    for i in range(1, len(nums)):
        sum_so_far += nums[i]
        if sum_so_far < minimum:
            minimum = sum_so_far
        if sum_so_far > nums[i]:
            sum_so_far = nums[i]
    return minimum


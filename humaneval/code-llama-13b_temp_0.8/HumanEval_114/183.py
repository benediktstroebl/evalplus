import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    curr_sum = nums[0]
    min_sum = curr_sum
    for i in range(1, len(nums)):
        curr_sum = min(curr_sum + nums[i], nums[i])
        min_sum = min(curr_sum, min_sum)
    return min_sum

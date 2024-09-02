import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    curr_min = nums[0]
    curr_max = 0
    curr_sum = 0

    for i in range(n):
        curr_sum += nums[i]
        curr_max = max(curr_max, curr_sum - curr_min)
        curr_min = min(curr_min, curr_sum)

    return curr_max


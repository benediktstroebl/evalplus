import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_so_far = nums[0]
    curr_sum = 0
    start = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum < min_so_far:
            min_so_far = curr_sum
            start = i
        elif curr_sum > 0:
            curr_sum = 0
    return min_so_far

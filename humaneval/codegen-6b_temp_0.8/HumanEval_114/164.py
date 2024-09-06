import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    min_so_far = nums[0]
    curr_so_far = 0
    for i in range(len(nums)):
        curr_so_far += nums[i]
        if curr_so_far < min_so_far:
            min_so_far = curr_so_far
        if curr_so_far < 0:
            curr_so_far = 0
    return min_so_far

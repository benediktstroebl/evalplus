import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_so_far = -math.inf
    curr_sum = 0
    for i in range(len(nums)):
        if curr_sum < 0:
            curr_sum = nums[i]
        else:
            curr_sum += nums[i]
        max_so_far = max(max_so_far, curr_sum)
    return max_so_far


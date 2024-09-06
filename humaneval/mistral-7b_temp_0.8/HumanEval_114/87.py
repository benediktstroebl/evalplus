import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize current sum and min sum
    cur_sum, min_sum = nums[0], nums[0]
    # Loop through the list to find the min sum
    for i in range(1, len(nums)):
        # Update current sum
        cur_sum = min(cur_sum+nums[i], nums[i])
        # Update min sum
        min_sum = min(cur_sum, min_sum)
    return min_sum

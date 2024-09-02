import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Find the maximum value in the array
    max_val = max(nums)
    # Keep track of the running sum and the current max sum
    curr_sum = 0
    curr_max_sum = 0
    for num in nums:
        curr_sum += num
        if curr_sum > curr_max_sum:
            curr_max_sum = curr_sum
    return curr_max_sum

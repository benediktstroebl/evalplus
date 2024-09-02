import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]

    min_so_far = float("inf")
    min_ending_here = 0
    for ending_here in range(len(nums)):
        min_ending_here += nums[ending_here]

        if min_ending_here < min_so_far:
            min_so_far = min_ending_here
    return min

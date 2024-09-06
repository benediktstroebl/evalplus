import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_so_far = max_ending_here = nums[0]

    for num in nums[1:]:
        max_ending_here = max(max_ending_here + num, num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

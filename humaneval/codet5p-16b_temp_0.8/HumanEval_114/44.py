import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_so_far = math.inf
    for i in range(len(nums)):
        if min_so_far > sum(nums[i:]):
            min_so_far = sum(nums[i:])

    return min_so_far

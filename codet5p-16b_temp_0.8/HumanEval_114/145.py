import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 0:
        return None

    smallest_sum = math.inf
    start, end = 0, 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            smallest_sum = min(smallest_sum, sum(nums[i:j+1]))

    return smallest_sum

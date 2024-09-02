import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    cur_sum = 0
    min_sum = None
    for i in range(len(nums)):
        cur_sum = nums[i] + (cur_sum if cur_sum > 0 else 0)
        if min_sum is None or cur_sum < min_sum:
            min_sum = cur_sum

    return min_sum

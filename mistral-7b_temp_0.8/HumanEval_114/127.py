import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    total = nums[0]
    min_total = nums[0]
    min_length = 1
    for i in range(1, len(nums)):
        # maintain min_total, min_length
        total += nums[i]
        min_total = min(total, min_total)
        if total < 0:
            total = 0
            min_length = i + 1
        else:
            min_length = min(min_length, i + 1)
    return min_total, min_length

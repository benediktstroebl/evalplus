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
        return 0
    best = nums[0]
    current = 0
    for i in range(len(nums)):
        current += nums[i]
        if current < 0:
            current = 0
        elif current < best:
            best = current
    return best

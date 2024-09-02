import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    mini = math.inf
    sumi = 0
    for num in nums:
        sumi += num
        if sumi < mini:
            mini = sumi
        if sumi > 0:
            sumi = 0
    return mini if mini != math.inf else 0

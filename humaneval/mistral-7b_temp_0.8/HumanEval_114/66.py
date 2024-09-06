import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    global l, s
    l = 0
    s = nums[0]
    for i in range(1, len(nums)):
        if s > nums[i]:
            s = nums[i]
            l = i
    return l, s

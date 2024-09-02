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
    p1 = float('inf')
    p2 = float('inf')
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        if total < p1:
            p1 = total
            p2 = nums[i]
        if total - p1 < p2:
            p2 = total - p1
    return p2

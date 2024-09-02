import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    res = float('inf')
    start, end = 0, 0
    while start < len(nums) - 1:
        while start < len(nums) and nums[start] <= end:
            end = max(end, nums[start + 1])
            start = start + 1
        if end - start + 1 >= res:
            res = end - start + 1
    return res
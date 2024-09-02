import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = math.inf
    start, end = 0, 0
    total = 0
    while end < len(nums):
        while total < minSum and end < len(nums):
            total += nums[end]
            end += 1
        while start < len(nums) and total >= minSum:
            total -= nums[start]
            start += 1
        if total < minSum:
            minSum = total
    return minSum


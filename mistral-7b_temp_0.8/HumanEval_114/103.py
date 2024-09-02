import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = float('inf')
    left = 0
    for right in range(len(nums)):
        curSum = sum(nums[left:right+1])
        if curSum < minSum:
            minSum = curSum
        if curSum > 0:
            left = right + 1

    return minSum

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    start = 0
    minSum = math.inf
    for end in range(len(nums)):
        minSum = min(minSum, nums[start:end+1])
        if nums[end] < 0:
            start = end + 1
    return minSum

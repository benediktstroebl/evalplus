import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    minSubArray = float('inf')
    minSum = 0
    for num in nums:
        minSum = minSum + num
        if minSum < minSubArray:
            minSubArray = minSum
        if minSum < 0:
            minSum = 0

    return minSubArray

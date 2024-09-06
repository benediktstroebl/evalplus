import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sum = 0
    minSum = math.inf
    for num in nums:
        sum = sum + num
        if sum < minSum:
            minSum = sum
        if sum < 0:
            sum = 0
    return minSum

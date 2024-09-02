import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    bestSum = float("inf")
    currentSum = 0

    for i, num in enumerate(nums):
        currentSum += num
        if currentSum < bestSum:
            bestSum = currentSum
        if currentSum < 0:
            currentSum = 0

    return bestSum

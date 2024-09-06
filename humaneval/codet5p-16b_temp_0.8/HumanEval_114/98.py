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
    startIndex = 0
    endIndex = 0
    currentSum = 0
    while startIndex < len(nums) and endIndex < len(nums):
        currentSum += nums[endIndex]
        if currentSum >= minSum:
            startIndex += 1
            endIndex = startIndex
            currentSum = 0
        else:
            endIndex += 1
        if currentSum < minSum:
            minSum = currentSum
    return minSum

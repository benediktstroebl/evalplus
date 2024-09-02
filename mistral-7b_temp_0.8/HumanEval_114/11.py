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
    currentSum = 0
    for i in range(len(nums)):
        currentSum += nums[i]
        if i > 0:
            currentSum -= nums[i-1]
        if currentSum < minSum:
            minSum = currentSum
    return minSum

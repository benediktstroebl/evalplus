import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = nums[0]
    maxSum = nums[0]
    currentSum = 0
    for i in range(len(nums)):
        currentSum += nums[i]
        if currentSum < minSum:
            minSum = currentSum
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0 and currentSum != minSum:
            currentSum = 0
    return max(maxSum, minSum)

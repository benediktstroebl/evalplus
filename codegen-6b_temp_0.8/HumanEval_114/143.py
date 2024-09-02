import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSubArray = None
    currentSum = None
    runningSum = 0

    for num in nums:
        if currentSum is None:
            currentSum = num
        else:
            currentSum += num

        if minSubArray is None or currentSum < minSubArray:
            minSubArray = currentSum

    return minSubArray

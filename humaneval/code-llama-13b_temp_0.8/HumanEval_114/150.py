import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums == []:
        return 0

    minSum = sum(nums)
    currentSum = 0
    for i in range(len(nums)):
        currentSum += nums[i]
        if currentSum < minSum:
            minSum = currentSum
        if currentSum > 0:
            currentSum = 0

    return minSum

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    currentSum = 0
    minSum = math.inf

    for i in range(n):
        currentSum = currentSum + nums[i]

        if i >= 1:
            currentSum = currentSum - nums[i-1]

        if currentSum < minSum:
            minSum = currentSum

    return minSum

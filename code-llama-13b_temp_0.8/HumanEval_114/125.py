import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def minSubArray(nums, start):
        minSum = math.inf
        currSum = 0
        for i in range(start, len(nums)):
            currSum += nums[i]
            if currSum < minSum:
                minSum = currSum
        return minSum

    minSum = math.inf
    for i in range(len(nums)):
        minSum = min(minSum, minSubArray(nums, i))
    return minSum

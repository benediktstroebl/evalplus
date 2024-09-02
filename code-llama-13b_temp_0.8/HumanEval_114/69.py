import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # We'll take advantage of the fact that the minimum subarray sum cannot
    # be greater than the sum of the entire array.
    arraySum = sum(nums)
    minSum = math.inf
    currSum = 0
    for i in range(len(nums)):
        currSum += nums[i]
        minSum = min(minSum, currSum)
        if currSum > arraySum:
            currSum = 0
    return minSum

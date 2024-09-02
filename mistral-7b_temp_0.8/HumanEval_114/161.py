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
    minSumLen = 1
    currSum = nums[0]
    currSumLen = 1
    for i in range(1, len(nums)):
        if currSum < 0:
            currSum = 0
            currSumLen = 1
        currSum += nums[i]
        currSumLen += 1
        if currSum < minSum:
            minSum = currSum
            minSumLen = currSumLen
        elif currSum == minSum:
            if currSumLen < minSumLen:
                minSumLen = currSumLen
    return minSumLen

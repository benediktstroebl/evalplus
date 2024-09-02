import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    minSum = float("inf")
    currSum = 0
    minWindow = 0

    for i in range(len(nums)):
        currSum += nums[i]
        while currSum > 0:
            if currSum < minSum:
                minSum = currSum
                minWindow = i-len(nums)+1
            currSum -= nums[minWindow]
            minWindow += 1

    return minWindow if minSum != float("inf") else 0


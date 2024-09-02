import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize minSum, minLen, currSum, currLen
    minSum = math.inf
    minLen = 0
    currSum = 0
    currLen = 0

    # Iterate over the array
    for i in range(len(nums)):
        # Update currSum and currLen
        currSum += nums[i]
        currLen += 1

        # Update minSum and minLen
        if currSum < minSum or (currSum == minSum and currLen < minLen):
            minSum = currSum
            minLen = currLen

    # Return the minimum sum and its length
    return minSum, minLen

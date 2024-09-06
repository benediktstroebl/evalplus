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
    start = 0
    currSum = 0
    for end in range(len(nums)):
        currSum += nums[end]
        if currSum < minSum:
            minSum = currSum
        if currSum <= 0:
            currSum = 0
        else:
            while start < end and currSum > 0:
                currSum -= nums[start]
                start += 1
    return minSum


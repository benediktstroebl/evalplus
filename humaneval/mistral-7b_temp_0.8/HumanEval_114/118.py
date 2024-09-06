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
    currSum = 0
    for i in range(len(nums)):
        currSum = currSum + nums[i]
        minSum = min(minSum, currSum)
        currSum = currSum - nums[i-1] if i > 0 else currSum

    return minSum


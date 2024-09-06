import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if not nums:
        return math.inf
    currSum = 0
    minSum = math.inf
    start = 0
    for i in range(len(nums)):
        currSum += nums[i]
        while currSum >= minSum:
            minSum = min(minSum, currSum - minSum)
            currSum -= nums[start]
            start += 1
    return minSum

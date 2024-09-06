import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    minSubArraySum = math.inf
    subArraySum = 0
    for i in nums:
        subArraySum += i
        minSubArraySum = min(minSubArraySum, subArraySum)
        subArraySum = 0 if minSubArraySum == 0 else subArraySum
    return minSubArraySum


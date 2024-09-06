import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 0: return math.inf
    minSums = [None] * len(nums)
    minSums[0] = nums[0]
    for i in range(1, len(nums)):
        minSums[i] = minSums[i-1] + nums[i]

    currentMinSum = minSums[0]
    for i in range(1, len(nums)):
        currentMinSum = min(currentMinSum, minSums[i])
    return currentMinSum


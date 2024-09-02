import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    currentSum = sums = nums[0]
    minSum = sums
    for i in range(1,len(nums)):
        currentSum = max(0, currentSum + nums[i])
        sums = min(sums, currentSum)
        minSum = min(minSum, sums)
    return minSum

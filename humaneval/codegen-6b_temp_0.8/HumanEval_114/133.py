import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    minSum, minSumIdx = nums[0], 0
    for i in range(1, len(nums)):
        if minSumIdx == 0:
            minSum = nums[i]
            minSumIdx = i
        else:
            minSum += nums[i]
            if minSum < minSum:
                minSum = minSum
                minSumIdx = i
    return minSum


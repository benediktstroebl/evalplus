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
    tempSum = 0
    for i in range(1,len(nums)):
        tempSum += nums[i]
        if tempSum < minSum:
            minSum = tempSum
        elif tempSum > 0:
            tempSum -= nums[i-1]
    return minSum


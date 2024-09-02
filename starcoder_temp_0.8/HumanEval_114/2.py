import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = 0
    if len(nums) == 1:
        return nums[0]
    else:
        minSum = math.inf
        tempSum = 0
        for i in range(0, len(nums)):
            tempSum += nums[i]
            if tempSum < minSum:
                minSum = tempSum
            if tempSum < 0:
                tempSum = 0
    return minSum

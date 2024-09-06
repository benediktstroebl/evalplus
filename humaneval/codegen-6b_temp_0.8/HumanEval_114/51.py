import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # minValue = min(nums)
    # for i in range(len(nums)):
    #     if minValue == 0:
    #         return minValue
    #
    #     minValue += nums[i]
    #     nums[i] = minValue
    #
    # return minValue

    tempSum = 0
    minValue = math.inf
    for i in range(len(nums)):
        tempSum += nums[i]
        if tempSum < minValue:
            minValue = tempSum
        if tempSum < 0:
            tempSum = 0

    return minValue

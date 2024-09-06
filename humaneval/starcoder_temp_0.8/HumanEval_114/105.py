import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    subarraySum = 0
    for i in range(len(nums)):
        subarraySum += nums[i]
        if subarraySum < 0:
            subarraySum = 0
    return subarraySum

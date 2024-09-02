import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    subArrSum = 0
    minSum = nums[0]

    for i in nums:
        subArrSum += i
        if subArrSum < minSum:
            minSum = subArrSum
        if subArrSum < 0:
            subArrSum = 0

    return minSum

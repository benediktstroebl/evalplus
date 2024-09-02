import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    subSum = 0
    minSum = nums[0]
    for i in range(len(nums)):
        subSum += nums[i]
        if subSum < minSum:
            minSum = subSum
        if subSum < 0:
            subSum = 0
    return minSum if minSum!= sys.maxsize else None

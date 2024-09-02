import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums or len(nums) == 0:
        return None

    preSum = 0
    minSum = math.inf
    for i, num in enumerate(nums):
        preSum += num
        minSum = min(minSum, preSum)
        if preSum < 0:
            preSum = 0
    return minSum

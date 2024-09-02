import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    minSum = math.inf
    for i in range(len(nums)):
        for j in range(i, len(nums)+1):
            if sum(nums[i:j]) < minSum:
                minSum = sum(nums[i:j])
    return minSum


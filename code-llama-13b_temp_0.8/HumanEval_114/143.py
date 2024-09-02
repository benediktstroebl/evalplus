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
    sum = 0
    start = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum < minSum:
            minSum = sum
        if sum > 0:
            sum = 0
            start = i + 1
        if i == len(nums) - 1:
            return minSum if minSum < 0 else 0
    return minSum


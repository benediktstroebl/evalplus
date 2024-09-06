import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = 9999999
    size = len(nums)
    for i in range(size):
        for j in range(i, size):
            sum = 0
            for k in range(i, j + 1):
                sum += nums[k]
            minSum = min(minSum, sum)
    return minSum


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
    n = len(nums)
    
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            minSum = min(minSum, total)
    
    return minSum


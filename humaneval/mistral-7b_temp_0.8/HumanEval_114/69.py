import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # O(N^2)
    n = len(nums)
    minSum = math.inf
    for i in range(n):
        curSum = 0
        for j in range(i, n):
            curSum += nums[j]
            minSum = min(curSum, minSum)
    return minSum

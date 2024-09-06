import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    minSum = float('inf')
    for i in range(0, n):
        j = i
        currentSum = 0
        while j < n:
            currentSum += nums[j]
            if currentSum < minSum:
                minSum = currentSum
            j += 1
    return minSum

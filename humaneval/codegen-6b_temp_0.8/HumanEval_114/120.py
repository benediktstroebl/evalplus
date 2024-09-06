import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total = float("inf")
    minSum = None
    for i in range(len(nums)):
        total = total + nums[i]
        for j in range(i, len(nums)):
            total -= nums[j]
            if total < 0:
                break
            if minSum == None or total < minSum:
                minSum = total
        if minSum == None:
            total = float("inf")
    return minSum

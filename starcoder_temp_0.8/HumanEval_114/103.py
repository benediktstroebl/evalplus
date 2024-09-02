import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    length = len(nums)
    totalSum = 0
    minSum = 0
    start = 0
    end = 0
    for i in range(length):
        totalSum += nums[i]
        end += 1
        while totalSum >= 0:
            if totalSum < minSum:
                minSum = totalSum
            totalSum -= nums[start]
            start += 1
        if end == length and totalSum > 0:
            minSum = totalSum
    return minSum

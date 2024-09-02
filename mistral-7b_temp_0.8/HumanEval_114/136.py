import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = 1e9
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        for j in range(i+1):
            if sum < minSum:
                minSum = sum
            sum -= nums[j]
    return minSum

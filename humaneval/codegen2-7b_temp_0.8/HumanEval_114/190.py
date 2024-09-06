import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = float('inf')
    min_index = 0
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum < minSum:
            minSum = sum
            min_index = i
    return minSum if minSum!= float('inf') else sum

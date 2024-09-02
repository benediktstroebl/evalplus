import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum, minSum = float('inf'), float('inf')
    curSum = 0
    for i in range(len(nums)):
        curSum += nums[i]
        if curSum < sum:
            sum = curSum
        if curSum - sum < minSum:
            minSum = curSum - sum
    return minSum if minSum!= float('inf') else sum

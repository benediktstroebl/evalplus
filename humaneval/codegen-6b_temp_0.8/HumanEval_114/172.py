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
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    for i in range(0,n):
        if (sum(nums[0:i+1]) < minSum):
            minSum = sum(nums[0:i+1])       #minSum = min(minSum,sum(nums[0:i+1]))
    return minSum

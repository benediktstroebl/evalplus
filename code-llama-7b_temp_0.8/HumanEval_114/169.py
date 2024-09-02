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
    if n == 0:
        return 0
    sum = 0
    minSum = math.inf
    for i in range(n):
        sum += nums[i]
        minSum = min(minSum, sum)
        if sum < 0:
            sum = 0
    if minSum == math.inf:
        return 0
    return minSum

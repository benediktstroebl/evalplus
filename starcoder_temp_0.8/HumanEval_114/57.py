import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum, minSum, start = 0, math.inf, 0
    for i in range(len(nums)):
        sum += nums[i]
        while sum >= 0:
            minSum = min(minSum, sum)
            start += 1
            if start >= len(nums):
                break
            sum -= nums[start-1]
    if minSum == math.inf:
        return 0
    return minSum

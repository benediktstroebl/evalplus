import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = math.inf
    windowSum = 0
    for num in nums:
        windowSum += num
        minSum = min(minSum, windowSum)
        windowSum = max(0, windowSum)
    return minSum if minSum != math.inf else 0


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
    minSum = math.inf
    total = 0
    start = 0
    end = 0

    while end < n:
        total += nums[end]
        end += 1
        while total >= minSum:
            minSum = min(minSum, total - nums[start])
            total -= nums[start]
            start += 1

    return minSum if minSum!= math.inf else -1

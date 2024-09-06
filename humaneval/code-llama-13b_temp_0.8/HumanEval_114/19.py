import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    minSum = math.inf
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        if i != 0:
            total -= nums[i - 1]
        minSum = min(minSum, total)
    return minSum if minSum > 0 else 0


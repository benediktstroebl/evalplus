import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total = 0
    minSum = math.inf
    start = 0
    for i in range(len(nums)):
        total += nums[i]
        while len(nums)-i > start and total >= 0:
            minSum = min(minSum, total)
            total -= nums[i+start]
            start += 1

    if minSum == math.inf:
        return minimumSubArray(nums)
    else:
        return minSum

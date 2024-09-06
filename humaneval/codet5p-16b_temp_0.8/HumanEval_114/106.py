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
    left = 0
    for i in range(len(nums)):
        total += nums[i]
        while total >= minSum:
            minSum = min(minSum, total - (left + 1))
            total -= nums[left]
            left += 1
    return minSum if minSum!= math.inf else -1


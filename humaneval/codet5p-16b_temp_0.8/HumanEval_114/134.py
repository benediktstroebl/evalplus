import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 0:
        return math.inf

    total = sum(nums)
    left = 0
    minSum = math.inf
    for right in range(len(nums)):
        minSum = min(minSum, total - nums[right])
        total -= nums[left]
        left += 1
    return minSum

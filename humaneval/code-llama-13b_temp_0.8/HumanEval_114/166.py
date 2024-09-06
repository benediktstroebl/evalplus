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

    # Get min sum of first k elements
    minSum = sum(nums[0:1])
    currSum = minSum
    for i in range(1, len(nums)):
        currSum += nums[i]
        if currSum < minSum:
            minSum = currSum
    return minSum


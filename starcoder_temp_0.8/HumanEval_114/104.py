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
    currentSum = 0
    for num in nums:
        currentSum += num
        minSum = min(minSum, currentSum)
        if currentSum < 0:
            currentSum = 0
    return minSum

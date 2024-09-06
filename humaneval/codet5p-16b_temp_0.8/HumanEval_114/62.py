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
    minSum2 = math.inf
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum < minSum:
                minSum = sum
            if sum < minSum2:
                minSum2 = sum
    if minSum == math.inf:
        return minSum2
    return minSum

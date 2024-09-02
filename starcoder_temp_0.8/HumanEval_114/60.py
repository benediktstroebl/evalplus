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
        return 0
    sums = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        sums[i + 1] = sums[i] + nums[i]
    minSum = math.inf
    for i in range(len(sums)):
        for j in range(i + 1, len(sums)):
            if sums[j] - sums[i] < minSum:
                minSum = sums[j] - sums[i]
    return minSum

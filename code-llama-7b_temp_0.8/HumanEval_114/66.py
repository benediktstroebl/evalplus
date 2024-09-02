import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # best sum starts at infinity
    minSubSum = math.inf

    for i in range(len(nums)):
        subSum = 0
        for j in range(i, len(nums)):
            subSum += nums[j]
            minSubSum = min(subSum, minSubSum)

    return minSubSum


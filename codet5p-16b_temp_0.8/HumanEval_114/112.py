import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    subArraysSum = [nums[0]]
    for i in range(1, len(nums)):
        subArraysSum.append(nums[i] + subArraysSum[i-1])

    minimumSum = math.inf
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subArraySum = subArraysSum[j+1] - subArraysSum[i]
            minimumSum = min(minimumSum, subArraySum)

    return minimumSum


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

    if len(nums) == 1:
        return nums[0]

    minSum = 100000000000
    currentSum = 0

    for i in range(0, len(nums)):
        currentSum += nums[i]
        if currentSum < minSum:
            minSum = currentSum

        if currentSum < 0:
            currentSum = 0

    return minSum

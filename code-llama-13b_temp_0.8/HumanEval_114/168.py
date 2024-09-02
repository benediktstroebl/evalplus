import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    minSum = float("inf")
    i = 0
    j = 0

    while i < len(nums) and j < len(nums):
        if sum(nums[i:j + 1]) == 0:
            return 0

        if sum(nums[i:j + 1]) < minSum:
            minSum = sum(nums[i:j + 1])

        if sum(nums[i:j + 1]) > 0:
            j += 1
        else:
            i += 1
            j = i

    return minSum

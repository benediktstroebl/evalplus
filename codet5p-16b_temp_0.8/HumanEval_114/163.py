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
    curSum = 0
    left = 0
    for i, n in enumerate(nums):
        curSum += n
        while curSum >= minSum:
            minSum = curSum
            left = i
            curSum -= nums[left]
    return minSum

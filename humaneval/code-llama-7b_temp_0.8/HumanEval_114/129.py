import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # initialize variables
    total = 0
    start = 0
    length = 0
    minSubSum = math.inf

    # loop through list
    for i in range(len(nums)):
        total += nums[i]
        if total < minSubSum:
            minSubSum = total
        if total < 0:
            total = 0

    return minSubSum

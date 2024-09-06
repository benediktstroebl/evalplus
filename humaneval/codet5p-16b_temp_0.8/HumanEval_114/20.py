import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sum = math.inf
    curr = 0
    for i in range(len(nums)):
        curr += nums[i]
        if curr < sum:
            sum = curr
        if curr > sum:
            curr = 0
    return sum

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # iterate through the array and check the subarrays
    subArraySum = 0
    for i in nums:
        subArraySum += i
        if subArraySum < 0:
            subArraySum = 0
    return subArraySum

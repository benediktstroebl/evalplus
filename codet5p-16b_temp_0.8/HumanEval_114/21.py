import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    total = min(nums)
    sum = 0
    for i in nums:
        sum = sum + i
        if sum > total:
            return total
        else:
            total = total + i
    return total

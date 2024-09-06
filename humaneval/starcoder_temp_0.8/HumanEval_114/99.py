import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total = 0
    min_val = 1000000
    for i in nums:
        total += i
        if total < min_val:
            min_val = total
    return min_val if min_val!= 1000000 else 0

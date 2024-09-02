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
    min_val = math.inf
    for i in range(len(nums)):
        total += nums[i]
        if min_val > total:
            min_val = total
        elif total < min_val:
            min_val = total
    return min

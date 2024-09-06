import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    cur = 0
    min_sum = math.inf

    for i in nums:
        cur += i
        if cur < min_sum:
            min_sum = cur

        if cur < 0:
            cur = 0
    
    return min_sum

import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    n = len(nums)
    i = 0
    summ = 0
    min_sum = math.inf
    while (i <= n-1):
        summ += nums[i]
        if summ < min_sum:
            min_sum = summ
        if summ >= min_sum:
            summ = summ - nums[i]
        i += 1
    return min_sum
    

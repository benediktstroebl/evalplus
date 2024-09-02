import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    summ = 0
    min_sum = math.inf
    for i in nums:
        summ += i
        min_sum = min(min_sum, summ)
        if summ < 0:
            summ = 0
    return min_sum

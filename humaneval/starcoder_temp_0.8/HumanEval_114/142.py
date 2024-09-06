import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    sum_total = 0
    for num in nums:
        sum_total += num
        if sum_total < min_sum:
            min_sum = sum_total
        if sum_total < 0:
            sum_total = 0
    return min_sum

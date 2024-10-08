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
    curr_sum = 0
    for num in nums:
        curr_sum = min(num, curr_sum + num)
        min_sum = min(min_sum, curr_sum)
    return min_sum

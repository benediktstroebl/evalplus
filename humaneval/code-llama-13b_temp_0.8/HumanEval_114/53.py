import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    result = math.inf
    min_sum = 0

    for num in nums:
        min_sum += num
        result = min(min_sum, result)
        if min_sum > 0:
            min_sum = 0

    return result

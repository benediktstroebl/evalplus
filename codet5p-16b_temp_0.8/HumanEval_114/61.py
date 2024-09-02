import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 0:
        return math.inf
    sum = 0
    min_sum = math.inf
    for n in nums:
        sum += n
        if min_sum > sum:
            min_sum = sum
    return min_sum
